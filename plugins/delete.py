import asyncio
from db import *
from config import *
from time import time
from bot import dbot
import time 
from datetime import datetime 

plan = ""
async def check_up(bot):   
    _time = int(time.time()) 
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

async def plan_update():
  while True:
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    timestamp = current_date.strftime("%Y-%m-%d")
    info_data = await see_plan(timestamp)
    for data in info_data: 
      try:
        chat_id = data["_id"]
        user_id = data["user_id"]
        plan = data["plan"]
        await update_group(id=chat_id, new_data={"verified": False, "plan": plan})
        msg = await dbot.send_message(chat_id, f"Your Plan Expired Today Now Contact To My Owner @{OWNER}")
        await dbot.pin_chat_message(
    chat_id,
    message_id=msg.id
)
      except Exception, e:
        raise e
    

dbot.start()
asyncio.create_task(run_check_up())
asyncio.create_task(plan_update())