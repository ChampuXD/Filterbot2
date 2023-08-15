from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *

MSG_TO = "This Is Auth Module"

@Client.on_message(filters.command("auth") & filters.private)
async def auth_handle(_, m):
  chat_id = m.chat.id
  