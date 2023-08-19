from time import time
from datetime import datetime 
import time 
from db import *
from pyrogram import *

dbot = Client("testbot", api_id=API_ID,
              api_hash=API_HASH,
              bot_token=BOT_TOKEN)

'''async def check_up(bot):
    _time = int(time())  # Use int(time()) instead of int(time.time())
    all_data = await get_all_dlt_data(_time)
    for data in all_data:
        try:
            chat_id = data["chat_id"]
            message_id = data["message_id"]
            await bot.delete_messages(chat_id=chat_id, message_ids=message_id)
            print(f"Deleted message_id {message_id} from chat_id {chat_id}")
        except Exception as e:
            print(f"Error deleting message_id {message_id} from chat_id {chat_id}: {str(e)}")
            pass
    await delete_all_dlt_data(_time)'''

async def main():
  try:
    # Get current time
    oki = datetime.now()
    current_time = oki.replace(second=0,microsecond=0).strftime("%y-%m-%d %H:%M")
    print(current_time)
    d_find = del_find(current_time)
    if current_time >= d_find['time']:
      print(dati)
      chat_id = d_find["chat_id"]
      message_id = d_find["message_id"]

      # Delete the message
      await dbot.delete_messages(chat_id, message_id)

      # Remove the message data from MongoDB
      del_col.delete_one({"_id": del_find["_id"]})

  except Exception as e:
    print("Error:", e)

    await asyncio.sleep(30)

# Main function to run the check_up function
'''async def run_check_up():
    async with bot:
        await check_up(bot)
        await asyncio.sleep(1)'''
            
if __name__ == "__main__":
    dbot.start()
    asyncio.get_event_loop()
    
