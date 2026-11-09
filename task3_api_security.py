import hashlib
import hmac
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ---------------------------------
# 1. Load environment variables
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

print("API_KEY loaded:", bool(API_KEY))
print("WEBHOOK_SECRET loaded:", bool(WEBHOOK_SECRET))


# ---------------------------------
# 2. Configure API retries
# ---------------------------------

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET"],
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)


# ---------------------------------
# 3. Fetch users from API
# ---------------------------------

url = "https://jsonplaceholder.typicode.com/users"

response = session.get(url, timeout=20)
response.raise_for_status()

users = response.json()

print("\nFirst 5 users:")

for user in users[:5]:
    print(f'{user.get("id")} - ' f'{user.get("name")} - ' f'{user.get("email")}')


# ---------------------------------
# 4. Read nested data using .get()
# ---------------------------------

first_user = users[0] if users else {}

address = first_user.get("address", {})
geo = address.get("geo", {})
company = first_user.get("company", {})

print("\nFirst User Details:")
print("City:", address.get("city", "Not Available"))
print("Latitude:", geo.get("lat", "Not Available"))
print("Zip:", address.get("zip", "Not Available"))
print("Company:", company.get("name", "Not Available"))


# ---------------------------------
# 5. Verify HMAC-SHA256 signature
# ---------------------------------


def verify_signature(payload: bytes, signature: str, secret: str) -> bool:

    expected_signature = hmac.new(
        secret.encode("utf-8"), payload, hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, signature)


# ---------------------------------
# 6. Test signature verification
# ---------------------------------

payload = b"employee_id=123"
secret = WEBHOOK_SECRET or ""

# Generate a valid signature
valid_signature = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()

# Generate a signature using a wrong secret
wrong_secret_signature = hmac.new(b"wrong_secret", payload, hashlib.sha256).hexdigest()

# Test all three cases
print("\nHMAC Signature Tests:")

print("Valid signature:", verify_signature(payload, valid_signature, secret))

print(
    "Tampered payload:", verify_signature(b"employee_id=999", valid_signature, secret)
)

print("Wrong secret:", verify_signature(payload, wrong_secret_signature, secret))
