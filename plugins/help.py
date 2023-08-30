from config import OWNER
from pyrogram import filters, Client
from config import *

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
async def help_handler(Client, m):
  chat_id = m.chat.id
  await m.reply(HELP_TEXT)
  
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

TEXT = f'''This bot is made by @{OWNER} A full time python developer

Our channel :- @movie_artss
Our selling channel :- @platimostore

Want to make any kink of bot & tool dm @{OWNER}'''

@Client.on_message(filters.command("about"))
async def about_handle(_,m):
  chat_id = m.chat.id
  await m.reply(TEXT)