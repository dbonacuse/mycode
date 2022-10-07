#!/usr/bin/env python3
""" Bitcoin Industries | Duncan Bonacuse
        Cryptocurrency data application """

# import statements
import requests
import json
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
import sys

# ASCII Art
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('cryptonalysis', font='starwars'),
       'white', 'on_blue', attrs=['bold'])

# Set variables to call later
local_currency = 'USD'
local_symbol = '$'

# Dictionary of HTTP headers to send with request
headers = {
        'X-CMC_PRO_API_KEY' : 'a4bfc9df-0ed7-4370-83a9-cc73eeb08dfc' ,
        'Accepts' : 'application/json'
        }

# Base URL of the CoinMarketCap API
base_url = 'https://pro-api.coinmarketcap.com'

# Main function
def main():

    while True:
        
        # Menu for Coinalysis
        # Different options to sort by descendning market cap, percent price change and trading volume in the last day
        print()
        print("CoinMarketCap Explorer Menu")
        print()
        print("1 - Top 100 sorted by market cap")
        print("2 - Top 100 sorted by 24 hour percent change")
        print("3 - Top 100 sorted by 24 hour trading volume")
        print("0 - Exit")

        # collect user input for how they'd like to sort
        choice = input("What is your choice (1-3): ")

        sort = ""

        # sorting list based on user input
        if choice == '1':
            sort = 'market_cap'
        if choice == '2':
            sort = 'percent_change_24h'
        if choice == '3':
            sort = 'volume_24h'
        if choice == '0':
            exit(0)
        else:
            print("Please enter a number (0-3)")

        # concatenating Base URL with URL for listings/price quotes and sorting
        quote_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency + '&sort=' + sort

        # calling the requests library and getting data from API, passing in quote url
        # headers = headers dictionary
        # returning json data that has been requested
        request = requests.get(quote_url, headers=headers)
        results = request.json()

        # All my data is nested within the 'data' object in the API
        data = results['data']

        # Calling prettytable and setting the columns in the table
        table = PrettyTable(['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24hr', '7d'])

        # For the currencies/assets in data, currency name is 'name', symbol (or ticker) is 'local_symbol
        # and rank is 'cmc_rank'
        print()
        for currency in data:
            name = currency['name']
            symbol = currency['symbol']
            rank = currency['cmc_rank']

            # Declaring quote variable to simplify the logic tree
            quote = currency['quote'][local_currency]

            # Declaring the rest of the data in the table
            market_cap = quote['market_cap']
            hour_change = quote['percent_change_1h']
            day_change = quote['percent_change_24h']
            week_change = quote['percent_change_7d']
            price = quote['price']
            volume = quote['volume_24h']

            # Rounding hourly percentage change data and assigning the data a background color
            # based on positive or negative percentage change. Green for positive, red for negative
            if hour_change != None:
                hour_change = round(hour_change, 2)
                if hour_change > 0:
                    hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
                else:    
                    hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

            # Rounding daily percentage change data and assigning the data a background color
            # based on positive or negative percentage change
            if day_change != None:
                day_change = round(day_change, 2)
                if day_change > 0:
                    day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
                else:    
                    day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL
            
            # Rounding weekly percentage change data and assigning the data a background color
            # based on positive or negative percentage change
            if week_change != None:
                week_change = round(week_change, 2)
                if week_change > 0:
                    week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
                else:    
                    week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL
            
            # Assigning volume as a string and formatting it with commas every third digit,
            # and rounding to 2 decimal places
            if volume != None:
                volume_str = '{:,}'.format(round(volume,2))
            
            # Assigning market_cap as a string and formatting it with commas every third digit,
            # and rounding to 2 decimal places
            if market_cap != None:
                market_cap_str = '{:,}'.format(round(market_cap,2))

            # Rounding and formatting price data as well
            price_str = '{:,}'.format(round(price,2))

            # Adding rows to table based on various data points
            table.add_row([str(rank),
                        name + '(' + symbol + ')',
                        local_symbol + price_str,
                        local_symbol + market_cap_str,
                        local_symbol + volume_str,
                        str(hour_change),
                        str(day_change),
                        str(week_change)])

        # printing table
        print()
        print(table)
        print()

main()

