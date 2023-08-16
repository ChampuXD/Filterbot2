import asyncio
from time import time 
from bot import Client, YaaraOP
from db import *
from config import *
from pyrogram import *
from pyrogram.errors import FloodWait
import time
import urllib.parse

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

  channels = (await get_group(chat_id))["channels"]
  if not channels:
      return

  if message.text.startswith("/"):
      return
    
  query = await clean_query(message.text)
  query_words = query.split()

  results = ""
  for chk in channels:
      for word in query_words:
          async for msg in YaaraOP.search_messages(int(chk), query=word, limit=10):
              if msg.caption or msg.text:
                  name = (msg.text or msg.caption).split("\n")[0]
                  if name in results:
                      continue
                  new_results = f"{name}\n {msg.link}\n\n"
                  if len(results) + len(new_results) > MESSAGE_LENGTH:
                      await message.reply(f"{results}", disable_web_page_preview=True)
                  results = ""
                  results += new_results
    
  if results:
      end = time.time()
      omk = end - star
      timee = f"Result Searched in {omk:.02} sec"
      await message.reply(f" {results}\n {timee}", disable_web_page_preview=True)
  else:
      await message.reply("No Movie Found 🔎")
      _time = int(time()) + (120 * 60)
      await save_dlt_message(msg, _time)
