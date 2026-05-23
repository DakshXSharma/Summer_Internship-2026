# import requests

# def weather_info(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=474eabca416757db2c6f7299d1ea9106&units=metric"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         print("Temperature:", data['main']['temp'])
#         print("Feels like:", data['main']['feels_like'])
#         print("Pressure:", data['main']['pressure'])
#         print("Humidity:", data['main']['humidity'])
#         print("Sea level:", data['main']['sea_level'])
#         print("Ground level:", data['main']['grnd_level'])
#         print("Visibility:", data['visibility'])
#     except requests.exceptions.RequestException as e:
#         print(e)

# city = input("Enter your city: ")
# weather_info(city)

import pywhatkit
pywhatkit.sendwhatmsg("+910123456789", "Hi", 10, 55)