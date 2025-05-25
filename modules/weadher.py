import requests
import os
from config.settings import load_dotenv

def city_picker(command):
    """
    Extracts the city name from a string.
    
    Args:
        string (str): The input string containing the city name.
        
    Returns:
        str: The extracted city name or an empty string if not found.
    """
    command = command.lower()
    if " in " in command:
        city = command.split(" in ")[-1].strip()
        return city.title()
    return ""

def get_weather(sentance=""):
    city = city_picker(sentance)
    print(city)
    load_dotenv()
    api_key = os.getenv("WEADHER_API")
    if not city:
        return "Please specify a city."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    print(res)

    if res.get("main"):
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "Couldn't retrieve weather information."
