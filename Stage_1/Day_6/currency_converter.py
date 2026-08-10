# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================


# Import get from requests because we need
# to send HTTP requests to the currency API
from requests import get



# Import PrettyPrinter for formatting
# complex data structures while debugging
from pprint import PrettyPrinter





# ==============================
# API CONFIGURATION
# ==============================


# Base URL of the exchange rate API
#
# The API provides:
# - currency list
# - exchange rates
# - conversion information
BASE_URL = "https://open.er-api.com/v6/latest"



# Create a pretty printer object
# Useful when displaying dictionaries
# and API responses in readable format
printer = PrettyPrinter()





# ==============================
# GET AVAILABLE CURRENCIES
# ==============================


# Function responsible for retrieving
# all supported currencies from the API
#
# Returns:
# A list of available currency codes
def get_currencies():


    # Build API request URL
    #
    # Using USD as the base currency
    # because the API requires a starting currency
    url = f"{BASE_URL}/USD"



    # Send GET request to the API
    #
    # timeout prevents the program from
    # waiting forever if the server fails
    response = get(
        url,
        timeout=10
    )



    # Check whether the request succeeded
    #
    # HTTP status 200 means successful response
    if response.status_code != 200:

        print(
            "Could not fetch currencies"
        )

        return []



    # Convert JSON response into Python dictionary
    #
    # Example:
    #
    # {
    #    "rates": {
    #        "EUR": 0.92,
    #        "GBP": 0.79
    #    }
    # }
    data = response.json()



    # Extract only currency codes
    #
    # Example:
    #
    # ["EUR", "GBP", "RWF"]
    currencies = list(
        data["rates"].keys()
    )



    # Return currencies in a format
    # that can be displayed easily
    return [
        (currency, currency)
        for currency in currencies
    ]





# ==============================
# DISPLAY CURRENCIES
# ==============================


# Function responsible for showing
# available currency options
def print_currencies(currencies):


    # Loop through every currency
    for code, name in currencies:


        # Display currency code
        #
        # Example:
        # USD - USD
        print(
            f"{code} - {name}"
        )





# ==============================
# GET EXCHANGE RATE
# ==============================


# Function responsible for finding
# the conversion rate between two currencies
#
# Example:
#
# USD → EUR
#
# Returns:
# Exchange rate number
def exchange_rate(
    currency1,
    currency2
):


    # Build API URL using
    # the base currency
    #
    # Example:
    # /latest/USD
    url = f"{BASE_URL}/{currency1}"



    # Request exchange information
    response = get(
        url,
        timeout=10
    )



    # Check if API request succeeded
    if response.status_code != 200:

        print(
            "Invalid currency"
        )

        return None



    # Convert response into dictionary
    data = response.json()



    # Check whether API itself reported success
    if data.get("result") != "success":

        print(
            "Currency API error"
        )

        return None



    # Find the requested currency rate
    #
    # Example:
    #
    # rates["EUR"]
    rate = data["rates"].get(
        currency2
    )



    # Handle unknown currencies
    if rate is None:

        print(
            "Currency not found"
        )

        return None



    # Display exchange rate
    print(
        f"{currency1} -> {currency2} = {rate}"
    )



    # Return rate for later calculations
    return rate





# ==============================
# CURRENCY CONVERSION
# ==============================


# Function responsible for converting
# a specific amount of money
#
# Formula:
#
# converted amount =
# amount × exchange rate
def convert(
    currency1,
    currency2,
    amount
):


    # Get current exchange rate
    rate = exchange_rate(
        currency1,
        currency2
    )



    # Stop if rate retrieval failed
    if rate is None:

        return



    # Convert user input into decimal number
    #
    # Example:
    # "100" → 100.0
    try:

        amount = float(
            amount
        )



    # Handle invalid amounts
    except ValueError:

        print(
            "Invalid amount"
        )

        return



    # Perform mathematical conversion
    converted_amount = (
        amount * rate
    )



    # Display formatted result
    #
    # :.2f means:
    # show exactly 2 decimal places
    print(
        f"{amount} {currency1} = "
        f"{converted_amount:.2f} {currency2}"
    )



    # Return converted value
    return converted_amount





# ==============================
# APPLICATION CONTROLLER
# ==============================


# Main function controlling the entire application
def main():



    # Load supported currencies
    currencies = get_currencies()



    # Stop program if API fails
    if not currencies:

        print(
            "Unable to load currencies"
        )

        return





    # Display available commands
    print(
        "Welcome to the currency converter!"
    )

    print(
        "--------------------------------"
    )

    print(
        "list     - show available currencies"
    )

    print(
        "convert  - convert money"
    )

    print(
        "rate     - show exchange rate"
    )

    print(
        "q        - quit"
    )





    # Main command loop
    #
    # Keeps the application running
    # until user chooses to quit
    while True:


        # Ask user what operation they want
        command = input(
            "\nEnter a command: "
        ).lower()



        # Exit application
        if command == "q":

            break





        # Show supported currencies
        elif command == "list":

            print_currencies(
                currencies
            )





        # Show exchange rate only
        elif command == "rate":


            # Ask starting currency
            currency1 = input(
                "Enter base currency: "
            ).upper()



            # Ask destination currency
            currency2 = input(
                "Enter currency to convert to: "
            ).upper()



            # Display rate
            exchange_rate(
                currency1,
                currency2
            )





        # Convert actual amount
        elif command == "convert":


            currency1 = input(
                "Enter base currency: "
            ).upper()



            amount = input(
                "Enter amount: "
            )



            currency2 = input(
                "Enter currency to convert to: "
            ).upper()



            convert(
                currency1,
                currency2,
                amount
            )





        # Handle unknown commands
        else:

            print(
                "Unrecognized command!"
            )





# ==============================
# PROGRAM START
# ==============================


main()