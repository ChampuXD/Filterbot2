import asyncio
from time import time 
from bot import Client, YaaraOP
from db import *
from config import *
from pyrogram import *
from pyrogram.errors import FloodWait
import time
import urllib.parse

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
    start_time = time.time()  # Start measuring elapsed time
    f_sub = await force_sub(bot, message)
    if f_sub == False:
        return

    channels = (await get_group(message.chat.id))["channels"]
    if not channels:
        return

    if message.text.startswith("/"):
        return

    quer = await clean_query(message.text)
    bas_yaar = quer.split()
    results = ""
    try:
        for channel in channels:
          for query in bas_yaar:
              async for msg in YaaraOP.search_messages(chat_id=channel, query=query):
                  name = (msg.text or msg.caption).split("\n")[0]
                  if name in results:
                    continue
                  results += f" {name}\n {msg.link}\n\n"

            if not results:
              no_results_message = f"No Results Found 🔎 \n\n"
            
              msg = await message.reply_text(text=no_results_message, disable_web_page_preview=True)
              _time = int(time()) + (2 * 60)
              await save_dlt_message(msg, _time)
              return

        elapsed_time = time.time() - start_time
        t_time = f"Searched in {elapsed_time:.2f} sec." # Add the duration to the footer
        msg = await message.reply_text(text=results + t_time, disable_web_page_preview=True)
        _time = int(time()) + (120 * 60)
        await save_dlt_message(msg, _time)
    Exception as e:
        print(e)
