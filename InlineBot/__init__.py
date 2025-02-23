
import time
import datetime
from pyrogram import Client
import os

# Force time synchronization
print("Server Time:", datetime.datetime.utcnow())

# Add a delay to allow time sync
time.sleep(5)

# Pyrogram client setup
API_ID = int(os.getenv("API_ID", "123456"))  # Replace with actual API_ID if needed
API_HASH = os.getenv("API_HASH", "your_api_hash_here")  # Replace with actual API_HASH
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")  # Replace with actual BOT_TOKEN

CodeXBotz = Client(
    "CodeXBotz", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN
)

CodeXBotz.start()
