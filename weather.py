import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather():
    print('\n**** Get Current Weather Conditions  in New Delhi ***\n')

    city = input('\nPlease enter your city:\n')

    request_url =f'https://api.openweathermap.org/data/2.5/weather?&appid=f5461504430b76a5b6347ab29aab9e50&q={city}&units=metric'

    print(request_url)
    weather_data = requests.get(request_url).json()

    
    # name = weather_data["name"]
    # temp = weather_data["main"].temp
    # description= weather_data["weather"][0].description
    
    print(f"\n Current Weather For {weather_data["name"]}")
    print(f"\n The Temp is {weather_data["main"]["temp"]} degree Celsius")


get_current_weather()