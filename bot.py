import requests
import time
import telebot
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = telebot.TeleBot(BOT_TOKEN)

def get_latest_block_hash():
    url = "https://apilist.tronscanapi.com/api/block/latest"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get('hash')
    except Exception as e:
        print("API Error:", e)
        return None

last_sent_hash = None

while True:
    block_hash = get_latest_block_hash()
    if block_hash and block_hash != last_sent_hash:
        message = f"🔗 Tron Latest Block Hash:\n`{block_hash}`"
        bot.send_message(CHANNEL_ID, message, parse_mode='Markdown')
        last_sent_hash = block_hash
    time.sleep(60)
