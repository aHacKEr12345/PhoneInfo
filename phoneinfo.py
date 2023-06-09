import requests

def phone_number_info(phone_number, country_code=None):
    url = "http://apilayer.net/api/validate"
    params = {
        "access_key": "YOUR-API-KEY-HERE",
        "number": phone_number,
        "country_code": country_code
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "valid" in data and data["valid"]:
        print("The phone number is valid")
        print(f"Country code: {data['country_code']}")
        print(f"Country name: {data['country_name']}")
        print(f"City: {data['location']}")
        print(f"Carrier: {data['carrier']}")
    else:
        print("The phone number is invalid")

phone_number_info("YOUR-VICTIMS-NUMBER", "YOUR-CONTRY-CODE")
