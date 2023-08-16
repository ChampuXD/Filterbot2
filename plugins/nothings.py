from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *



@Client.on_message(filters.command("info"))
async def info_handle(_, m):
  chat_id = m.chat.id
  await m.reply("You Didn't Purchase Any Plan")
  
@Client.on_message(filters.command("index"))
async def index_handle(_,m):
  chat_id = m.chat.id 
  await m.reply("connecting ...")
  
@Client.on_message(filters.command("remove"))
async def remove_handle(_, m): 
  chat_id = m.chat.id
  await m.reply("error")