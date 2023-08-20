from datetime import datetime, timedelta
import asyncio
from pyrogram import Client
from db import *

API_ID = "your_api_id"
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

bot = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def delete_messages():
    while True:
        try:
            # Get current time
            oki = datetime.now()
            current_time = oki.replace(second=0, microsecond=0).strftime("%y-%m-%d %H:%M")
            print(current_time)
            
            # Query MongoDB for data
            d_find = del_find(current_time)
            if d_find and current_time >= d_find['time']:
                print(d_find)
                chat_id = d_find["chat_id"]
                message_id = d_find["message_id"]

                # Delete the message
                await bot.delete_messages(chat_id, message_id)

                # Remove the message data from MongoDB
                del_col.delete_one({"_id": d_find["_id"]})
        except Exception as e:
            print("Error:", e)

        await asyncio.sleep(60)  # Wait for 1 minute

if __name__ == "__main__":
    bot.start()
    asyncio.get_event_loop().create_task(delete_messages())
    bot.idle()
