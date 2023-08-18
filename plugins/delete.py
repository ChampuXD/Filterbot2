from time import time 
import time 
from bot import dbot as bot
from db import * 

async def check_up(bot):
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
    await delete_all_dlt_data(_time)

# Main function to run the check_up function
async def run_check_up():
    async with bot:
        await check_up(bot)
        await asyncio.sleep(1)
            
if __name__ == "__main__":
    asyncio.run(run_check_up())
