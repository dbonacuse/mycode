#!/usr/bin/env python3
""" Bitcoin Industries | Duncan Bonacuse
        Cryptocurrency data application """

import requests
from requests import Request, Session
import pprint
import json

#  https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
       'start' : '1',
       'limit' : '10',
       'convert' : 'USD'
        }

headers = {
        'X-CMC_PRO_API_KEY' : 'a4bfc9df-0ed7-4370-83a9-cc73eeb08dfc' ,
        'Accepts' : 'application/json'
        }

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

""" def symbol_finder(coins):
        symbols = []
        for x in coins:
                req = requests.get(x)
                decodedjson = req.json()
                symbols.append(decodedjson.get("symbol"))

        return symbols """

def main():

        search_input = input("Please search for a cryptocurrency: ")

        for search_input in coins :
                 print(search_input['cmc_rank'], search_input['symbol'], search_input['quote']['USD']['price'])

main()
# session = Session()
# session.headers.update(headers)

# response = session.get(url, params=parameters)

# print(json)
