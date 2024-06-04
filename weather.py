import requests

def get_weather(city):
    api_key = "w.json"
     
    base_url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&current_weather=true" # type: ignore
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data['cod'] == 200:
        city = weather_data['name']
        country = weather_data['sys']['country']
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        print(f"Weather in {city}, {country}:")
        print(f"Condition: {main_weather} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error fetching weather data: {weather_data['message']}")

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
