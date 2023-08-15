import asyncio
from config import *
from pyrogram import enums
from pymongo.errors import DuplicateKeyError
from pyrogram.errors import UserNotParticipant
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton

dbclient = MongoClient(DATABASE_URI)
db = dbclient["Filter-Bot"]
grp_col = db["USERS"]
grp_col_1 = db["GROUPS"]

async def add_user(user_id):
  data = {
    "_id": user_id
  }
  try:
    await grp_col.insert_one(data)
  except DuplicateKeyError:
    pass

async def add_group(group_id, user_id):
  data = {
    "_id": user_id,
    "chat": group_id
  }
  try:
    await grp_col_1.insert_one(data)
  except DuplicateKeyError:
    pass