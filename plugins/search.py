import asyncio
from time import time
from datetime import datetime, timedelta 
from bot import Client, YaaraOP
from db import *
from config import *
from pyrogram import *
from pyrogram.errors import FloodWait
import time

MESSAGE_LENGTH = 4096

ignore_words = ["in", "and", "hindi", "movie", "tamil", "telugu", "dub", "hd", "man", "series", "full", "dubbed", "kannada", "season", "part", "all", "2022", "2021", "2023", "1", "2", "3", "4", "5", "6", "7" ,"8", "9", "0", "2020", "2019", "2018" , "2017", "2016", "2014", "all", "new", "2013", "()", "movies", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002", "2001", "1999", "1998", "1997", "1996", "1995", "-+:;!?*", "language", "480p", "720p", "1080p", "south", "Hollywood", "bollywood", "tollywood",] # words to ignore in search query

async def should_ignore(word):
    # checks if a word should be ignored in the search query
    return word.lower() in ignore_words

async def clean_query(query):
    # cleans the search query by removing ignored words
    words = query.split()
    cleaned_words = [word for word in words if not await should_ignore(word)]
    return " ".join(cleaned_words)


@Client.on_message(filters.text & filters.group & filters.incoming & ~filters.command(["auth", "index", "id"]))
async def search(bot, message):
  chat_id = message.chat.id
  star = time.time()
  f_sub = await force_sub(bot, message)
  if f_sub == False:
      return
  veri = await get_group(chat_id)
  verified = veri["verified"]
  if verified == False:
    return
  channels = veri['channels']
  if not channels:
      return
  if message.text.startswith("/"):
      return
  query = await clean_query(message.text)
  max_unique_results = 8
  unique_results = set() 
  results = ""
  quri = query.split()
  for chk in channels:
    async for msg in YaaraOP.search_messages(int(chk), query=query, limit=8):
      if msg.caption or msg.text:
        name = (msg.text or msg.caption).split("\n")[0]
        result_entry = f"{name}\n {msg.link}\n\n"
        if not result_entry in unique_results: 
          if len(unique_results) >= max_unique_results:
            break
          else:
            unique_results.add(result_entry)
            results += result_entry
    for omk in quri:
      async for msg in YaaraOP.search_messages(int(chk), query=omk, limit=8):
        
        if msg.caption or msg.text:
          name = (msg.text or msg.caption).split("\n")[0]
          result_entry = f"{name}\n {msg.link}\n\n"
          if not result_entry in unique_results:
            if len(unique_results) >= max_unique_results:
              break
            else:
              unique_results.add(result_entry)
              results += result_entry  
    
  if results:
          end = time.time()
          omk = end - star
          timee = f"Result Searched in {omk:.2f} sec"  
          msg = await message.reply(f" {results} {timee}", disable_web_page_preview=True)
          _time = int(time.time()) + (5 * 60)
          try:
            message_id = msg.id
            if veri['auto_del'] == True:
              await save_dlt_message(chat_id, _time, message_id)
          except FloodWait as e:
            print(e)
      
  else:
      xx = await message.reply("No Results Found 🔎")
      await asyncio.sleep(20)
      await xx.delete()
      
      
