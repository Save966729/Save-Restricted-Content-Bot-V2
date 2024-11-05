# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28509278"))
API_HASH = getenv("API_HASH", "1e3f3e92b5f04130a901c044efe10f24")
BOT_TOKEN = getenv("BOT_TOKEN", "7596876781:AAEc48Dm8gHa5YMSKplEWGEibXSr3B2AF3g")
OWNER_ID = int(getenv("OWNER_ID", "6648234579"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://save966729:i0jGnqVqwGxK2Pfa@cluster0.feual.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "1002486546788"))
FORCESUB = getenv("FORCESUB", "1002381505263")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested
