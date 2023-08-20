from datetime import datetime, timedelta
import asyncio
from pyrogram import *
from db import *
from bot import dbot as bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def delete_messages():
    while True:
        try:
            # Get current time
            oki = datetime.now()
            current_time = oki.replace(second=0, microsecond=0).strftime("%y-%m-%d %H:%M")
            print(current_time)
            
            # Query MongoDB for data
            d_find = await del_find(current_time)
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

        await asyncio.sleep(10)  # Wait for 1 minute

async def plan_update():
    current_time = datetime.now().replace(second=0,microsecond=0).strftime("%y-%m-%d %H:%M")
    data = del_find(current_time)
    if current_time > data: 
      print(data)
    
scheduler = AsyncIOScheduler()
scheduler.add_job(plan_update, "interval", seconds=3)

scheduler.start()
