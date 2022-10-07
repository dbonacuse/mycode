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

btc_dominance = str(round(btc_dominance, 2))+ '%'

eth_dominance = str(round(eth_dominance, 2))+ '%'

tmc_rounded = (round(total_market_cap, 2))
total_market_cap = local_symbol + f'{tmc_rounded:,}'

total_volume_24h = local_symbol + f'{total_volume_24h:,}'

print()
print("The global market cap for all cryptocurrencies is " + total_market_cap +
" and the global 24 hour volume is " + total_volume_24h + ".")
print()
print("Bitcoin makes up " + btc_dominance + " of the total crypto market cap " +
"and Ethereum makes up " + eth_dominance + ".")
print()



# answer = str(round(answer, 2))



# while True:

#     # base URLs for application
#     globalURL = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"

#     tickerURL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

#     # get data from globalURL
#     request = requests.get(globalURL)
#     results = request.json()
#     globalMarketCap = results['data']['quotes']['USD']['total_market_cap']

#     #menu
#     print()
#     print("Welcome")
#     print("Global cap of all cryptocurrencies: $" + str(globalMarketCap))
#     print("Enter 'all' or 'name of crypto' (i.e. bitcoin) to see the name of the top 100 currencies")
#     print()
#     choice = input("Your choice: ")

#     if choice == "all":
#         request = requests.get(tickerURL)
#         results = request.json()

#         for x in data:
#             ticker = x['symbol']
#             price = x['quote']['USD']['price']

#             print(ticker + ":\t\t$" + price)
#         print()

#     else:
#         tickerURL += '/' + choice + '/'
#         request = requests.get(globalURL)
#         results = requests.json()

#         ticker = data[0]['symbol']
#         price = data[0]['quote']['USD']['price']

#         print(ticker + ":\t\t$" + price)
#         print()
    
#     choice2 = input("Again? (y/n)")
#     if choice2 == "y":
#         continue
#     if choice2 == "n":
#         break
        

