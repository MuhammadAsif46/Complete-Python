import requests

API_KEY = 'b20f0da2987e0dca77ea7da278c9ff18'
city_name = input("Enter city name: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'


response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     # print(data)
#     weather_disc = data['weather'][0]
#     print(weather_disc)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather_disc = data['weather'][0]['description']
    temp = data['main']['temp'] - 273.15
    
    # Display weather info
    print(f'Weather in {city_name}: {round(temp, 1)} °C with {weather_disc}')
else:
    print(f"City name {city_name} is not found or incorrect")
    