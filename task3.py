import requests
from datetime import datetime, time

def fetch_weather(location):
    api_key = "a8fb122dba6beef5e3d4deff7178ef0a"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        # Extracting relevant weather information
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        visibility = weather_data["visibility"]
        windspeed = weather_data["wind"]["speed"]
        sunrise = datetime.fromtimestamp(weather_data["sys"]["sunrise"]).time()
        sunset = datetime.fromtimestamp(weather_data["sys"]["sunset"]).time()
        description = weather_data["weather"][0]["description"]

        # Display weather information
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
        print(f"Visibility: {visibility}")
        print(f"Wind Speed: {windspeed}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunrise: {sunset}")
    else:
        print("Error: City not found")

def main():
    print("Welcome to the Weather App!")
    location = input("Enter city name or ZIP code: ")
    weather_data = fetch_weather(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()