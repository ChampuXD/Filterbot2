from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *


@Client.on_message(filters.command("start"))
async def start_handle(_, m):
  user = m.from_user
  START_MSG = f'''Hey {user.mention}    
    
I am the first & best ever Filter Bot ! 
I will filter your channel posts automatically and send it in your group chat when someone needs it.

Press /help for more info!
Press /buy to purchase a subscription!

your chat id = {user.id}'''
  await add_user(id=user.id, name=user.username)
  await m.reply(START_MSG)




