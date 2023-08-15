from config import * 
from bot import Client
from pyrogram import *
from pyrogram.types import *
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

Get ID of current chat - /getid

Auto_delete : use /Auto_delete command to enable or disable
              auto message delete system.
'''

PLAN_USD = '''These are the prices in USD:

    `1.2 USD` - per Month 
    `6.2 USD` - per 6 Months
    `12.3 USD` - per Year

    Click on the Buy button to contact the owner'''
    
PLAN_INR = '''**These are the prices in INR:**

    `99 INR` - per Month 
    `599 INR` -  per 6 Months
    `1000 INR` -  per Year

    Click on the `Buy` button to contact the owner'''
BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="Buy",url="t.me/@{OWNER}"),
  InlineKeyboardButton(text="USD PRICE",callback_data="usd_p")
  ]])

@Client.on_message(filters.command("help"))
async def help_handler(_, m):
  chat_id = m.chat.id
  await m.reply(HELP_TEXT)

@Client.on_message(filters.command("buy")) 
async def buy_handle(_ ,m):
  chat_id = m.chat.id
  await m.reply(PLAN_INR,BUTTON)
  
@Client.on_callback_query()
async def cb_help(_, q):
  data = q.data
  BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="Buy",url="t.me/@{OWNER}"),
  InlineKeyboardButton(text="INR PRICE",callback_data="inr_p")
  ]])
  if data == "inr_p": 
    await q.message.edit(PLAN_INR,reply_markup=BTN)
  elif data == "usd_p": 
    await q.message.edit(PLAN_USD,reply_markup=BUTTON)