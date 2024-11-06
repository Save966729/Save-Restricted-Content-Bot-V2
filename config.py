# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28509278"))
API_HASH = getenv("API_HASH", "1e3f3e92b5f04130a901c044efe10f24")
BOT_TOKEN = getenv("BOT_TOKEN", "7887170368:AAGkQXN8766XCzRzhab2KiLvP_t5DELetoE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6648234579").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://save966729:wHyoMzBSFT6A5ej6@cluster0.feual.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002486546788")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002381505263"))
