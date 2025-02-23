
import time
from pyrogram import Client

# Force synchronization before starting the bot
app = Client("my_account")

async def sync_time():
    await app.connect()
    await app.get_me()  # Sync time with Telegram servers
    await app.disconnect()

app.run(sync_time())

from InlineBot import CodeXBotz
CodeXBotz().run()