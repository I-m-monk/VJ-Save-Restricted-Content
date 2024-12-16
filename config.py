import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26785305"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "25538181a4a9229070515dd3ae8c7f5f")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6853144930"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://customcard007700:EZdXwaASDzVjMXwT@cluster0.ywxil.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "LovyouBunnybot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
