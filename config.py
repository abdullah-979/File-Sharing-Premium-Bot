import os
import logging
from logging.handlers import RotatingFileHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7940588823:AAHlIGzWYb0-IT14LLtLJi71hAmQnJGOpKc")
API_ID = int(os.environ.get("API_ID", "2817222"))
API_HASH = os.environ.get("API_HASH", "aed9f2af23e0df07d7f34011e8a3c86f")

OWNER_ID = int(os.environ.get("OWNER_ID", "1994781564"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://cidtamil2:SMietwIr91WmCEf8@cluster0.gbtwinc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "cidtamil2")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002746802139"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001676008024"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

try:
    ADMINS=[1994781564]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention}\n\nI can store private files in Specified Channel and other users can access it from special link.</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {mention}\n\nYou Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")
ADMINS.append(OWNER_ID)
ADMINS.append(1994781564)

LOG_FILE_NAME = "cidtamil2.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

