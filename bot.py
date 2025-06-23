import os
import requests
import time
import telebot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize bot
TOKEN = os.getenv('7276811839:AAHzIbQP-EwJVgd9YgdvlXm4bMWdjRScPlU')
CHANNEL_ID = os.getenv('@trx1minsg')
bot = telebot.TeleBot(TOKEN)

def get_latest_block_hash():
    """Fetch latest TRON block hash from Tronscan API"""
    url = "https://api.tronscan.org/api/block?sort=-number&limit=1"
    try:
        response = requests.get(url)
        data = response.json()
        if data['data']:
            return data['data'][0]['hash']
        return None
    except Exception as e:
        print(f"API Error: {e}")
        return None

def main():
    last_sent_hash = None
    
    while True:
        current_hash = get_latest_block_hash()
        
        if current_hash and current_hash != last_sent_hash:
            message = f"🔄 TRON Latest Block Hash:\n\n{current_hash}"
            try:
                bot.send_message(CHANNEL_ID, message)
                last_sent_hash = current_hash
                print(f"Sent update: {current_hash}")
            except Exception as e:
                print(f"Telegram Error: {e}")
        
        time.sleep(60)  # Check every 1 minute

if name == "main":
    print("🤖 TRON Block Hash Bot Started!")
    main()
