import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")

CHANNEL = os.getenv("CHANNEL")

LOT_SIZE = float(os.getenv("LOT_SIZE", "0.10"))
