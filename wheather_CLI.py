import requests
import os
from dotenv import load_dotenv
load_dotenv()
key=os.getenv('H-key')
if key is None:
    print("API key not found!")
    exit()
try:
    lat=float(input("Enter the latitude: "))
    lon=float(input("Enter the longitude: ")) 
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&units=metric"
        )    
    status=response.status_code
    if status==200:
        print(f"Status : {status}")
        w_data=response.json()
        print("=======Weather Data=======")
        print(f"City : {w_data['city']['name']}")
        print(f"Country : {w_data['city']['country']}")
        print(f"Weather : {w_data['list'][0]['weather'][0]['description']}")
        print(f"Temperature : {w_data['list'][0]['main']['temp']} °C")
        print(f"Pressure : {w_data['list'][0]['main']['pressure']} hPa")
        print(f"Humidity : {w_data['list'][0]['main']['humidity']} %")
        print(f"Wind Speed : {w_data['list'][0]['wind']['speed']} m/s")
    else:
        print(f"Status Code: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException as e:
    print("Failed to load the data")
