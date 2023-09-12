import requests

def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["cod"] == "404":
        return f"Unable to retrieve weather forecast for {city} 😞"
    
    weather_description = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    
    forecast = f"Current weather in {city}: {weather_description} 🌤️\n"
    forecast += f"Temperature: {temperature:.1f}°C 🌡️\n"
    forecast += f"Humidity: {humidity}% 💧"
    
    return forecast


# API key from OpenWeatherMap
api_key = "36175c520160b199e511dff91b0f8168"

# City for weather forecast
city = "Nellore"

# Get the weather forecast
weather_forecast = get_weather_forecast(api_key, city)
print(weather_forecast)