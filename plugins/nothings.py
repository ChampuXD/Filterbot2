from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *



@Client.on_message(filters.command("info"))
async def info_handle(_, m):
  id = m.from_user.id
  group = await check_plan(id)
  group_id = group["_id"]
  plan = group["plan"]
  print(plan)
  name = m.from_user.mention
  if plan != "":
    await m.reply(f"Hey {name} Your Plan Validity {plan}")
  else:
    await m.reply(f"Hey {name} You Didn't Purchase Any Plan")
  
@Client.on_message(filters.command("index"))
async def index_handle(_,m):
  chat_id = m.chat.id 
  await m.reply("connecting ...")
  
@Client.on_message(filters.command("remove"))
async def remove_handle(_, m): 
  chat_id = m.chat.id
  await m.reply("error")