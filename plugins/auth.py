from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *
from datetime import datetime, timedelta 

MSG_TO = "This Is Auth Module"
CHECKING = "Please Provide Me In Correct Format /check -chat id"


@Client.on_message(filters.command("check") & filters.user(OWNER_ID))
async def chat_id_check(bot:Client, m):
  chat_id = m.chat.id
  if m.text == "/check":
    await m.reply(CHECKING)
  else:
    n_id = int(m.text.split(None,1)[1])
    group = await bot.get_chat(n_id)
    uname = group.username 
    await m.reply("You Giving Me @" + uname + " Chat ID")
  
@Client.on_message(filters.command("auth") & filters.private & filters.user(OWNER_ID))
async def auth_handle(bot:Client, m):
  if m.text == "/auth":
    await m.reply("Please Provide Group ID And Time Period like /auth Group ID Time ")
  chat_id = int(m.text.split(None,2)[1])
  group = await get_group(chat_id)
  user_id = group["user_id"]
  user_name = group["user_name"]
  verified = group["verified"]
  if verified == True:
    await m.reply(f"user id: {user_id}\n username: @{user_name} group chat is already verified!")
  elif verified == False:
    id = chat_id
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = int(m.text.split(None, 2)[-1])
    ok = current_date + timedelta(days=end_time)
    timestamp = ok.strftime("%Y-%m-%d")
    await update_group(id, {"verified": True, "plan": timestamp})
    await m.reply(f"user id: {user_id}\n username: @{user_name} group chat is verified!")
    await bot.send_message(chat_id, f"hey @{user_name} Purchase A Plan For {end_time}days ")
  else:
    await m.reply("Verification Request Failed !!\nPlease Give Me Command in correct format\n **`/auth Group ID Time`**")
  
