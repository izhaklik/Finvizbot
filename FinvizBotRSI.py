from pyfinviz.screener import Screener
import requests

# Token and Chat ID
TOKEN = ''
CHAT_ID = ''

# Function to send messages on telegram
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response

# Parameters from Finviz
options = [
    Screener.IndexOption.S_AND_P_500,  # S&P 500
    Screener.RSI14Option.OVERSOLD_30,  # RSI מתחת ל-30
    Screener._200DaySimpleMovingAverageOption.PRICE_ABOVE_SMA200  # מחיר מעל ה-SMA200
]

screener = Screener(filter_options=options, view_option=Screener.ViewOption.VALUATION, pages=[x for x in range(1, 2)])

for page_num, df in screener.data_frames.items():
    if df.empty:
        message = f" ללא מניות בטקטיקת הRSI היום"
    else:
        # Filter to show only tiker of stocks
        tickers = df['Ticker'].to_string(index=False)  # Convert to Str
        message = f"  נמצאו המניות הבאות בטקטיקה\n{tickers}"

    # send messages on telegram
    send_telegram_message(message)
