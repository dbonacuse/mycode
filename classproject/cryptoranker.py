#!/usr/bin/env python3
""" Bitcoin Industries | Duncan Bonacuse
        Cryptocurrency data application """

# import statements
import sys
import time
import requests
from prettytable import PrettyTable
from colorama import Back, Style, init
from termcolor import cprint
from pyfiglet import figlet_format

# ASCII Art
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
cprint(figlet_format('coin    guru', font='starwars'),
       'white', 'on_blue', attrs=['bold'])

# Set variables to call later
LOCAL_CURRENCY = 'USD'
LOCAL_SYMBOL = '$'

# Dictionary of HTTP headers to send with request
headers = {
    'X-CMC_PRO_API_KEY': 'a4bfc9df-0ed7-4370-83a9-cc73eeb08dfc',
    'Accepts': 'application/json'
}

# Base URL of the CoinMarketCap API
BASE_URL = 'https://pro-api.coinmarketcap.com'

# Main function
def main():
    """
    Take user input to sort top cryptocurrencies
    using various metrics
    """
    while True:

        # Menu for CoinGuru
        # Different options to sort by descendning market cap,
        # percent price change and trading volume in the last day
        print()
        print("CoinGuru Explorer Menu\n")
        print("Please make a choice from the following menu on how you would " +
        "like to sort the top 100 cryptocurrencies\n")
        print("1 - Top 100 sorted by market cap")
        print("2 - Top 100 sorted by 24 hour price percentage change")
        print("3 - Top 100 sorted by 24 hour trading volume")
        print("4 - Top 100 sorted by circulating supply")
        print("5 - Top 100 sorted by maximum supply")
        print("0 - Exit\n")

        # collect user input for how they'd like to sort
        choice = input("What is your choice (1-5): ")

        sort = ""

        # sorting list based on user input
        if choice == '1':
            sort = 'market_cap'
        elif choice == '2':
            sort = 'percent_change_24h'
        elif choice == '3':
            sort = 'volume_24h'
        elif choice == '4':
            sort = 'circulating_supply'
        elif choice == '5':
            sort = 'max_supply'
        elif choice == '0':
            sys.exit(0)
        else:
            print("Please enter a valid number.\n")
            time.sleep(1)
            continue

        # concatenating Base URL with URL for listings/price quotes and sorting
        quote_url = BASE_URL + '/v1/cryptocurrency/listings/latest?convert=' + \
            LOCAL_CURRENCY + '&sort=' + sort

        # calling the requests library and getting data from API, passing in quote url
        # headers = headers dictionary
        # returning json data that has been requested
        request = requests.get(quote_url, headers=headers, timeout=10) # 10 second timeout
        results = request.json()

        # All my data is nested within the 'data' object in the API
        data = results['data']

        # Calling prettytable and setting the columns in the table
        table = PrettyTable(
            ['Market Cap Rank', 'Asset', 'Price', 'Market Cap', 'Volume',
             '1h', '24hr', '7d', 'Circulating Supply', 'Max Supply'])

        # For the currencies/assets in data, currency name is 'name',
        # symbol (or ticker) is 'symbol'
        # and rank is 'cmc_rank'
        print()
        for currency in data:
            name = currency['name']
            symbol = currency['symbol']
            rank = currency['cmc_rank']
            circ_supply = currency['circulating_supply']
            max_supply = currency['max_supply']

            # Declaring quote variable to simplify the logic tree
            quote = currency['quote'][LOCAL_CURRENCY]

            # Declaring the rest of the data in the table
            market_cap = quote['market_cap']
            hour_change = quote['percent_change_1h']
            day_change = quote['percent_change_24h']
            week_change = quote['percent_change_7d']
            price = quote['price']
            volume = quote['volume_24h']

            # Rounding hourly percentage change data and assigning the data a background color
            # based on positive or negative percentage change. Green for positive, red for negative
            if hour_change is not None:
                hour_change = round(hour_change, 2)
                if hour_change > 0:
                    hour_change = Back.GREEN + \
                        str(hour_change) + '%' + Style.RESET_ALL
                else:
                    hour_change = Back.RED + \
                        str(hour_change) + '%' + Style.RESET_ALL

            # Rounding daily percentage change data and assigning the data a background color
            # based on positive or negative percentage change
            if day_change is not None:
                day_change = round(day_change, 2)
                if day_change > 0:
                    day_change = Back.GREEN + \
                        str(day_change) + '%' + Style.RESET_ALL
                else:
                    day_change = Back.RED + \
                        str(day_change) + '%' + Style.RESET_ALL

            # Rounding weekly percentage change data and assigning the data a background color
            # based on positive or negative percentage change
            if week_change is not None:
                week_change = round(week_change, 2)
                if week_change > 0:
                    week_change = Back.GREEN + \
                        str(week_change) + '%' + Style.RESET_ALL
                else:
                    week_change = Back.RED + \
                        str(week_change) + '%' + Style.RESET_ALL

            # Assigning volume as a string and formatting it with commas every third digit,
            # and rounding to 2 decimal places
            if volume is not None:
                volume_str = '{:,}'.format(round(volume, 2))

            # Assigning market_cap as a string and formatting it with commas every third digit,
            # and rounding to 2 decimal places
            if market_cap is not None:
                market_cap_str = '{:,}'.format(round(market_cap, 2))

            # Formatting circulating supply
            if circ_supply is not None:
                circ_supply_str = '{:,}'.format(round(circ_supply, 2))

            # Formatting max supply
            if max_supply is not None:
                max_supply_str = '{:,}'.format(round(max_supply, 2))

            # Rounding and formatting price data as well
            price_str = '{:,}'.format(round(price, 2))

            # Adding rows to table based on various data points
            table.add_row([str(rank),
                           name + '(' + symbol + ')',
                           LOCAL_SYMBOL + price_str,
                           LOCAL_SYMBOL + market_cap_str,
                           LOCAL_SYMBOL + volume_str,
                           str(hour_change),
                           str(day_change),
                           str(week_change),
                           circ_supply_str,
                           max_supply_str])

        # printing table
        print()
        print(table)
        print()

        # provide user the option to run the program again
        choice2 = input("Would you like to run the CoinGuru application again? (y/n): ")
        if choice2 == "y":
            continue
        if choice2 == "n":
            print("Thank you for using CoinGuru.")
            break

main()
