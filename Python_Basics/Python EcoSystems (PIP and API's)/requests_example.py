# # allows your Python program to talk to the internet. It can visit websites and download data,
# # just like a web browser. This is how we interact with API's

# Example: When you check the weather on your phone, your phone doesn't have a thermometer sticking out of it.
# Your phone sends a Request (via API) to the Weather.com server: "Hey, what's the temperature in Mumbai?"
# Weather.com receives the message, looks up the data, and sends a Response: "It is 28°C."
# Your phone shows you the number.

# Uber uses the Google Maps API to show you the map. (Uber didn't build their own satellites!).

# A travel site uses the Airline APIs to check ticket prices from Delta, British Airways, and Emirates all at once.

import requests

# 1. We send a "GET" request to a website URL
response = requests.get('https://api.github.com')

# 2. We check if it worked (Status Code 200 means OK)
if response.status_code == 200:
    print('Success')

    # 3. Convet the data to a JSON (Dictionary)
    data = response.json()
    print(data)
else:
    print("Something went wrong!")
