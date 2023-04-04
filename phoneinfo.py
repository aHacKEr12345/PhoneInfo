# Import the requests library
import requests

# Define a function that takes a phone number and an optional country code
def phone_number_info(number, country_code=None):
    # Set the API URL
    url = "http://apilayer.net/api/validate"

    # Set the API parameters
    params = {
        "access_key": "oA6417lDKB4gWwA04ph1Id9rqdE6QISN",
        "number": number,
        "country_code": country_code
    }

    # Make the API call and get the response
    response = requests.get(url, params=params)

    # Get the JSON data from the response
    data = response.json()

    # Check if the number is valid
    if data["valid"]:
        # Print information about the phone number
        print("The number is valid.")
        print(f"Country code: {data['country_code']}")
        print(f"Country name: {data['country_name']}")
        print(f"Location: {data['location']}")
        print(f"Carrier: {data['carrier']}")
    else:
        # Print an error message if the number is invalid
        print("The number is invalid.")

# Call the function with a phone number and a country code
phone_number_info("698889903", "355")
