import logging
from datetime import datetime 
import asyncio 
from config import *
from pyrogram import *

# Initialize logging
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"),
              logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger(__name__)

# Initialize clients
User = Client(name="user", session_string=SESSION)

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "bot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    async def start(self):                        
        try:
            await super().start()
            await bot.send_message(CHAT_ID, "ALIVE")
            await User.start()
            Popen("python3 -m utils.delete", shell=True)       
            LOGGER.info("Bot Started ⚡")
        except Exception as e:
            LOGGER.exception("Error while starting bot: %s", str(e))
    async def stop(self, *args):
        try:
            await super().stop()
            LOGGER.info("Bot Stopped")
        except Exception as e:
            LOGGER.exception("Error while stopping bot: %s", str(e))