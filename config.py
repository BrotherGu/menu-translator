import os
from dotenv import load_dotenv

# constants
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
# iPhone photos are often mislabeled image/jpeg while actually HEIC;
# real format is verified/converted server-side in main.py via pillow-heif.
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp", "image/heic", "image/heif"}

# Gemini API key
if os.getenv("RENDER") != "true":
    load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

GEMINI_BATCH_SIZE = int(os.getenv("GEMINI_BATCH_SIZE"))
if not GEMINI_BATCH_SIZE:
    raise ValueError("GEMINI_BATCH_SIZE not found. Please check your .env file.")
