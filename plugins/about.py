from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *

TEXT = '''This bot is made by @owner_21 A full time python developer

Our channel :- @movie_artss
Our selling channel :- @platimostore

Want to make any kink of bot & tool dm @owner_21'''

@Client.on_message(filters.command("about"))
async def about_handle(_,m):
  chat_id = m.chat.id
  await m.reply(TEXT)