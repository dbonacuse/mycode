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

global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

# calling the requests library and getting data from API, passing in global url
# headers = headers dictionary
request = requests.get(global_url, headers=headers)

# cmc has sent us global metrics, now sorting data w json
results = request.json()

# print(json.dumps(results, sort_keys = True, indent = 4))

data = results["data"]

btc_dominance = data["btc_dominance"]
eth_dominance = data["eth_dominance"]
total_market_cap = data["quote"][local_currency]["total_market_cap"]
total_volume_24h = data["quote"][local_currency]["total_volume_24h"]

btc_dominance_str = str(round(btc_dominance, 2))+ '%'

eth_dominance_str = str(round(eth_dominance, 2))+ '%'

tmc_rounded = (round(total_market_cap, 2))
total_market_cap_str = local_symbol + f'{tmc_rounded:,}'

total_volume_24h_str = local_symbol + f'{total_volume_24h:,}'

print()
print("The global market cap for all cryptocurrencies is " + total_market_cap_str +
" and the global 24 hour volume is " + total_volume_24h_str + ".")
print()
print("Bitcoin makes up " + btc_dominance_str + " of the total crypto market cap " +
"and Ethereum makes up " + eth_dominance_str + ".")
print()

