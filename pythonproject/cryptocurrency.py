#!/usr/bin/env python3
""" Bitcoin Industries | Duncan Bonacuse
        Cryptocurrency data application """

import requests
# from requests import Request, Session
import pprint
import json

#  https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest

# API url
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Dictionary of GET parameters to send with request
params = {
       'start' : '1',
     #  'limit' : '10',
       'convert' : 'USD'
        }

# Dictionary of HTTP headers to send with request
headers = {
        'X-CMC_PRO_API_KEY' : 'a4bfc9df-0ed7-4370-83a9-cc73eeb08dfc' ,
        'Accepts' : 'application/json'
        }

# json data that is being returned
json = requests.get(url, params=params, headers=headers).json()

# parsing 'data' object
coins = json['data']

# main function
def main():

        # Asking user to input a symbol for a listed cryptocurrency
       # search_input = input("Please search for a cryptocurrency: ")


        for x in coins :
        # if x['symbol'] == 'BTC' :
                print (x['cmc_rank'], x['symbol'], x['quote']['USD']['price'])

        # else:
        #         print("Please enter a valid symbol")


        # for search_input in coins :
        #          print(search_input['cmc_rank'],search_input['symbol'],search_input['quote']['USD']['price'])

main()
# session = Session()
# session.headers.update(headers)

# response = session.get(url, params=parameters)

# print(json)
