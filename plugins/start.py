from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *


@Client.on_message(filters.command("start") & filters.private)
async def start_handle(_, m):
  user = m.from_user
  START_MSG = f'''Hey {user.mention}    
    
I am the first & best ever Automediafilterbot ! 
I will filter your channel posts automatically and send it in your group chat when someone needs it.

Press /help for more info!
Press /buy to purchase a subscription!

your chat id = {user.id}'''
  await add_user(id=user.id, name=user.username)
  await m.reply(START_MSG)


@Client.on_message(filters.command("id"))
async def id_handle(_, m):
  chat_id = m.chat.id
  user = m.from_user
  MSG = f"This Chat ID : `{chat_id}`\n"
  
  if m.reply_to_message:
    user_id = m.reply_to_message.from_user.id
    MSG += f"Reply User ID: `{user_id}`"
    await m.reply(MSG)
  else:
    user_id = m.from_user.id
    MSG += f"Your ID: `{user_id}`"
    await m.reply(MSG)

