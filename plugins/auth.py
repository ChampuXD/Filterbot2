from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *

MSG_TO = "This Is Auth Module"
CHECKING = "Please Provide Me In Correct Format /check <chat id>"


@Client.on_message(filters.command("check") & filters.user(OWNER_ID))
async def chat_id_check(bot:Client, m):
  chat_id = m.chat.id
  nid = m.text.split(None,1)[1]
  group = await bot.get_chat(nid)
  uname = group.user_name
  if nid ==None:
    await m.reply(CHECKING)
  else:  
    await m.reply("You Giving Me" + uname + "Chat ID")
  
@Client.on_message(filters.command("auth") & filters.private)
async def auth_handle(_, m):
  chat_id = m.text.split(None,1)[1]
  group = await get_group(chat_id)
  user_id = group["user_id"]
  user_name = group["user_name"]
  verified = group["verified"]
  if verified == True:
    return await message.reply("This @{user_name} user group is already verified!")
  else:
    try:
      id = chat_id
      await update_group(id,{"verified": True})
      await app.send_message(chat_id, f"This Group Verified By @{OWNER}")
    except:
      await m.reply("Verification Request Failed !!\nPlease Give Me Command in correct format\n **`/auth Group ID Time`**")
  