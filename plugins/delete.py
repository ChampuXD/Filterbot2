from datetime import datetime, timedelta
import asyncio
from pyrogram import Client
from db import *
from bot import dbot as bot


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
async def update_documents():
  while True:
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    timestamp = current_date.strftime("%Y-%m-%d")
    # Find documents with the "plan" field less than or equal to the current date
    documents_to_update = grp_col.find({"plan": {"$lte": timestamp}})
    
    for doc in documents_to_update:
        await grp_col.update_one({"_id": doc["_id"]}, {"$set": {"verified": False}})
        id = await grp_col.find({"user_id":doc[user_id]})
        await bot.send_message(id,"Hey Your Plan Expired Today Now")

bot.start()
asyncio.create_task(update_documents())
asyncio.get_event_loop().create_task(delete_messages())
bot.idle()
