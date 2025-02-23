# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

import os

API_HASH = os.environ.get("API_HASH", None)
APP_ID = int(os.environ.get("APP_ID", "0"))
DB_URI = os.environ.get("DATABASE_URL", None)
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
TG_BOT_WORKERS = int(os.environ.get("BOT_WORKERS", '4'))
DB_NAME = os.environ.get("DATABASE_NAME", "InlineFilterBot")
thumb = os.environ.get('THUMBNAIL_URL', 'https://telegra.ph/file/516ca261de9ebe7f4ffe1.jpg')
OWNER_ID = int(os.environ.get('OWNER_ID', '0'))
CUSTOM_START_MESSAGE = os.environ.get('START_MESSAGE','')
FILTER_COMMAND = os.environ.get('FILTER_COMMAND', 'add')
DELETE_COMMAND = os.environ.get('DELETE_COMMAND', 'del')
IS_PUBLIC = os.environ.get('IS_PUBLIC', 'True').lower() == 'true'
try:
    ADMINS=[OWNER_ID]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

if not API_HASH or not APP_ID or not BOT_TOKEN:
    raise ValueError("Missing API_HASH, APP_ID, or BOT_TOKEN. Please check environment variables.")

#---------- ---------- ---------- ----------

import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "codexbotz.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#---------- ---------- ---------- ----------
from pyrogram import Client

class CodeXBotz(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "InlineBot/plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.LOGGER(__name__).info(f"@{bot_details.username}  started!")
        self.LOGGER(__name__).info("Created by 𝘾𝙤𝙙𝙚 𝕏 𝘽𝙤𝙩𝙯\nhttps://t.me/CodeXBotz")
        self.bot_details = bot_details

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
        
#---------- ---------- ---------- ----------

from pyrogram import filters
from pyrogram.types import (
    Message,
    InlineQuery,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedDocument
)

def is_owner(_, __, update):
    try:
        user_id = update.from_user.id
    except:
        return False

    return user_id == OWNER_ID

def is_admin(_, __, update):
    try:
        user_id = update.from_user.id
    except:
        return False

    return user_id in ADMINS

def check_inline(_, __, update):
    try:
        user_id = update.from_user.id
    except:
        return False

    return IS_PUBLIC or user_id in ADMINS

filters.admins = filters.create(is_admin)
filters.owner = filters.create(is_owner)
filters.inline = filters.create(check_inline)

#---------- Koyeb Deployment Steps ----------
# 1. Create an account on Koyeb (https://www.koyeb.com/)
# 2. Create a new service and select GitHub as the deployment source.
# 3. Connect your GitHub repository containing this bot.
# 4. Set the environment variables (API_HASH, APP_ID, DB_URI, BOT_TOKEN, etc.)
# 5. Choose Python as the runtime and install the dependencies using 'requirements.txt'.
# 6. Set the start command as 'python3 -m InlineBot'.
# 7. Deploy and monitor logs for any errors.
# 8. Your bot is now running on Koyeb!
