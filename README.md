# Finvizbot

Project: Finviz Stock Screener Telegram Bot
This Python script scrapes stock data from Finviz based on specific filtering criteria (in this case, using the RSI strategy), and sends updates via a Telegram bot. If no stocks meet the criteria, the script sends a message indicating that no stocks are found for the day.

# Prerequisites
Make sure you have the following installed:

1. Python 3.x
2. pyfinviz for stock data scraping
3. requests for making HTTP requests to the Telegram API
   
# Install
pip install pyfinviz requests

# Functionality
Stock Filtering:
1. The script uses Finviz's stock screener to find stocks from the S&P 500 that meet the following criteria:
2.     RSI (14) is below 30 (indicating oversold conditions).
3.     Stock price is above the 200-day simple moving average (SMA), signaling a potential uptrend.

   
# Telegram Integration:
Once the stock filtering is complete, the script sends the filtered stock tickers (if any) to your specified Telegram chat/channel.
If no stocks match the criteria, you'll receive a message indicating that no stocks were found for the day based on the RSI strategy.


# How to Use

Set up a Telegram Bot:

To get started, you will need to create a bot on Telegram via BotFather.
After creating your bot, you'll receive a token for accessing Telegram's API.
Get your Telegram Chat ID:

You can use the following URL to get your chat ID:
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
Replace <YOUR_BOT_TOKEN> with the actual token you received from BotFather.

# Configure the Script:

Replace the placeholders for TOKEN and CHAT_ID in the script with your actual bot token and chat ID, respectively.
Run the Script:

Execute the Python script in your terminal:
python screener_telegram.py
Code Overview
python
Copy code
from pyfinviz.screener import Screener
import requests


Schedule the script to run daily using a task scheduler

License
**This project is open source under the MIT License.**

