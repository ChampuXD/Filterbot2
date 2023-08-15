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

async def add_user(user_id):
  data = {
    "_id": user_id
  }
  grp_col.insert_one(data)
