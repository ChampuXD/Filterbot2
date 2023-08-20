from config import * 
from bot import Client
from pyrogram import *
from pyrogram.types import *
from db import *

@Client.on_message(filters.command("db") & filters.private)
async def db_retrieve(_, m):
  chat_id = m.text.split(None,1)[1]
  results = "Your Data Here\n"
  ok = del_finds(chat_id)
  for data in ok:
    results += data
  print(results)