from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *

MSG_TO = "This Is Auth Module"

@Client.on_message(filters.command("auth") & filters.private)
async def auth_handle(_, m):
  chat_id = m.text.split(None,2)[1]
  group = await get_group(chat_id)
  user_id = group["user_id"]
  user_name = group["user_name"]
  verified = group["verified"]
  if verified == True:
    return await message.reply("This @{user_name} user group is already verified!")
  else:
    try:
      period = m.text.split(None,2)[2]
      await update_group(chat_id,{"verified": True}, period)
      await app.send_message(chat_id, f"This Group Verified By @{OWNER}")
    except:
      await m.reply("Verification Request Failed !!\nPlease Give Me Command in correct format\n **`/auth Group ID Time`**")
  
