import pyperclip
import time
import requests
from pyautogui import press, hotkey

INIT_STARTUP_TIME = 20
SEC_IN_FIVE_MINS = 60*60*5

resp = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY=9e7f9363-6fab-4d64-87ab-eb4fbd806d67&symbol=burger&convert=AUD')
priceData = resp.json()['data']['BURGER']['quote']['AUD']
print(priceData['price'])

time.sleep(INIT_STARTUP_TIME)

while True:
    time.sleep(SEC_IN_FIVE_MINS)
    
    resp = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY=9e7f9363-6fab-4d64-87ab-eb4fbd806d67&symbol=burger&convert=AUD')
    priceData = resp.json()['data']['BURGER']['quote']['AUD']
    
    pyperclip.copy('The text to be copied to the clipboard.')

    hotkey('ctrl', 'v')
    press('enter')