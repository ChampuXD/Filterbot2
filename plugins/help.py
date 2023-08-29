from config import * 
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from db import *

HELP_TEXT = f'''😇How To use  me

press /buy to purchase a subscription.

Index a group with - /index 
EXAMPLE: /index -100xxxxxxxxxxx
Add me in the channel. And make sure I have all the permissions!


Remove a Channel with - /remove -100xxxxxxxxxxx
this will help you to remove a indexed channel from your group.


Get indexed channels list with - /viewlist 

Check your information with - /info
Gives your information and validity of your subscription

Get ID of current chat - /id

Auto_delete : use /autodel command to enable or disable
              auto message delete system.
'''




@Client.on_message(filters.command("help"))
async def help_handler(bot: Client, m):
  chat_id = m.chat.id
  await m.reply(HELP_TEXT)

@Client.on_message(filters.command("buy")) 
async def buy_handle(bot: Client,m):
  BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="USD PRICE",callback_data="usd_p"),
  InlineKeyboardButton(text="INR PRICE",callback_data="inr_p")
  ]])
  await m.reply(text="All The Available Plans",reply_markup=BUTTON)
  
@Client.on_callback_query()
async def cb_help(bot: Client, callback_query):
  data = callback_query.data
  PLAN_USD = '''These are the prices in USD:\n\n2 USD - per Month\n6 USD - per 6 Months\n10 USD - per Year\n\nClick on the Buy button to contact the owner'''
  PLAN_INR = '''These are the prices in INR:\n\n150 INR - per Month\n400 INR - per 6 Months\n800 INR - per Year\n\nClick on the Buy button to contact the owner'''
  BTN_1 = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Buy", url=f"t.me/{OWNER}"),
            InlineKeyboardButton(text="USD PRICE", callback_data="inr_p")
        ]
    ])
  BTN_2 = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Buy", url=f"t.me/{OWNER}"),
            InlineKeyboardButton(text="INR PRICE", callback_data="usd_p")
        ]
    ])
    
  if data == "inr_p":
    await callback_query.message.edit(PLAN_INR, reply_markup=BTN_1)
  elif data == "usd_p":
    await callback_query.message.edit(PLAN_USD, reply_markup=BTN_2)

    
 

@Client.on_message(filters.command("id"))
async def id_handle(bot:Client , m):
  chat_id = m.chat.id
  user = m.from_user
  MSG = f"This Chat ID : `{chat_id}`\n"
  if m.reply_to_message:
    user_id = m.reply_to_message.from_user.id
    MSG += f"Reply User ID: `{user_id}`"
  elif m.from_user:
    user_id = m.from_user.id
    MSG += f"Your ID: `{user_id}`"
  else:
    None
  await m.reply(MSG)
