import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv('7276811839:AAHzIbQP-EwJVgd9YgdvlXm4bMWdjRScPlU')
    CHANNEL_ID = os.getenv('https://t.me/trx1minsg')
    INTERVAL = int(os.getenv('INTERVAL_MINUTES', 1))
