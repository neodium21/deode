# Copyright (c) 2025
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------------------------------------------
# Cookies Section — Paste Your Cookies Below
# ------------------------------------------

# Instagram cookies (required for certain scraping/download operations)
INST_COOKIES = """
# Paste your Instagram cookies here
"""

# YouTube cookies (required for private/download-restricted content)
YTUB_COOKIES = """
# Paste your YouTube cookies here
"""

# ------------------------------------------
# Environment Variables (from .env file)
# ------------------------------------------

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "")
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")

# Optional: Telegram session string for userbots or assistant
STRING = os.getenv("STRING", None)

# Telegram group/channel IDs (must start with -100 for supergroups)
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1001234456"))
FORCE_SUB = int(os.getenv("FORCE_SUB", "-10012345567"))

# Owner ID(s) — Space-separated list, converted to integer list
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))

# Encryption keys for secure session handling
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F")

# Fallback cookies from environment or string block
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)

# Usage limits for freemium and premium users
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))

# ------------------------------------------
# Debug (optional): print critical config
# ------------------------------------------
if not API_ID or not API_HASH or not BOT_TOKEN:
    print("Warning: API_ID, API_HASH, or BOT_TOKEN is missing!")

if not OWNER_ID:
    print("Warning: No OWNER_IDs defined!")

# Optional: Debug print
# print(f"Loaded config: DB={DB_NAME}, OwnerIDs={OWNER_ID}, Limits(F/P)={FREEMIUM_LIMIT}/{PREMIUM_LIMIT}")
