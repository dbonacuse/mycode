#!/usr/bin/env python3

import requests
import json

local_currency = 'USD'
local_symbol = '$'

headers = {
        'X-CMC_PRO_API_KEY' : 'a4bfc9df-0ed7-4370-83a9-cc73eeb08dfc' ,
        'Accepts' : 'application/json'
        }

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

# calling the requests library and getting data from API, passing in global url
# headers = headers dictionary
request = requests.get(global_url, headers=headers)

# cmc has sent us global metrics, now sorting data w json
results = request.json()

# print(json.dumps(results, sort_keys = True, indent = 4))

data = results["data"]
for currency in data:
    name = currency['name']
    symbol = currency['symbol']

    rank = currency['cmc_rank']
    price = currency['quote'][local_currency]['price']
    percent_change_24h = currency['quote'][local_currency]['percent_change_24h']
    market_cap = currency['quote'][local_currency]['market_cap']

    price = round(price, 2)
    percent_change_24h = round(percent_change_24h, 2)
    market_cap = round(market_cap, 2)

    rank_str = str(rank)
    price_str = local_symbol + f'{price:,}'
    percent_change_24h_str = '%' + f'{percent_change_24h:,}'
    market_cap_str = local_symbol + f'{market_cap:,}'

    print('Coinmarketcap Rank: ' + rank_str)
    print(name + ' (' + symbol + ')')
    print('Price: ' + price_str)
    print('24hr Change: ' + percent_change_24h_str)
    print('Market Cap: ' + market_cap_str)
    print()
