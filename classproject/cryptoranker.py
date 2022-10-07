#!/usr/bin/env python3

import requests
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = 'USD'
local_symbol = '$'

headers = {
        'X-CMC_PRO_API_KEY' : 'a4bfc9df-0ed7-4370-83a9-cc73eeb08dfc' ,
        'Accepts' : 'application/json'
        }

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("CoinMarketCap Explorer Menu")
print()
print("1 - Top 100 sorted by market cap")
print("2 - Top 100 sorted by 24 hour percent change")
print("3 - Top 100 sorted by 24 hour trading volume")
print("0 - Exit")

choice = input("What is your choice (1-3): ")

sort = ""


if choice == '1':
    sort = 'market_cap'
if choice == '2':
    sort = 'percent_change_24hr'
if choice == '3':
    sort = 'volume_24hr'
if choice == '0':
    exit(0)
# else:
#     print("Please enter a number (0-4)")

quote_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency + '&sort=' + sort

request = requests.get(quote_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

table = PrettyTable(['Asset', 'Price', 'Market Cap', 'Volume', '1h', '24hr', '7d'])

print()
for currency in data:
    name = currency['name']
    symbol = currency['symbol']

    quote = currency['quote'][local_currency]
    market_cap = quote['market_cap']
    hour_change = quote['percent_change_1h']
    day_change = quote['percent_change_24h']
    week_change = quote['percent_change_7d']
    price = quote['price']
    volume = quote['volume_24h']

    if hour_change != None:
        hour_change = round(hour_change, 2)
    
    if day_change != None:
        day_change = round(day_change, 2)

    if week_change != None:
        week_change = round(week_change, 2)
    
    if volume != None:
        volume_str = '{:,}'.format(round(volume,2))
    
    if market_cap != None:
        market_cap_str = '{:,}'.format(round(market_cap,2))

    price_str = '{:,}'.format(round(price,2))

    table.add_row([name + '(' + symbol + ')',
                local_symbol + price_str,
                local_symbol + market_cap_str,
                local_symbol + volume_str,
                str(hour_change),
                str(day_change),
                str(week_change)])

print()
print(table)
print()

