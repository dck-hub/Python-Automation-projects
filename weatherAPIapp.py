# Allow to get the weather of any city in the world well as the tempreture and other information
import requests

API_KEY = '3dd5f356f91c54578f514590ed6dabfd'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "clesius")
else:
    print("An error occurred.")