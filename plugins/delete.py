from datetime import datetime, timedelta
import asyncio
from pyrogram import *
from db import *
from bot import dbot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger





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
                await dbot.delete_messages(chat_id, message_id)

                # Remove the message data from MongoDB
                del_col.delete_one({"_id": d_find["_id"]})
        except Exception as e:
            print("Error:", e)

        await asyncio.sleep(10)  # Wait for 1 minute

async def plan_update():
    current_time = datetime.now().replace(second=0,microsecond=0).strftime("%y-%m-%d %H:%M")
    data = del_find(current_time)
    if current_time = data: 
      print(data)

async def check_up(bot):   
    _time = int(time()) 
    all_data = await get_all_dlt_data(_time)
    for data in all_data:
        try:
           await bot.delete_messages(chat_id=data["chat_id"],
                                     message_ids=data["message_id"])           
        except Exception as e:
           err=data
           err["❌ Error"]=str(e)
           print(err)
    await delete_all_dlt_data(_time)

async def run_check_up():
    async with dbot as bot: 
        while True:  
           await check_up(bot)
           await asyncio.sleep(1)
    
if __name__=="__main__":   
   asyncio.run(run_check_up())
   
async def run_check_up():
    async with dbot as bot:
        scheduler = AsyncIOScheduler()
        scheduler.add_job(
            check_up, 
            trigger=IntervalTrigger(seconds=1),  # Change interval as needed
            args=[bot],
            max_instances=1,  # To ensure only one instance runs at a time
        )
        scheduler.start()
        try:
            await asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()

if __name__ == "__main__":
    asyncio.run(run_check_up())

