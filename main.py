import requests
from tkinter import *

def get_weather():
    print("fetching weather...")
    city = city_entry.get()
    api_key = "fa73b738c95a515c51c288acd16bd760"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    units = unit_var.get()
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        print("Fetching data from API...")
        response =requests.get(base_url, params=params)
        response.raise_for_status()
        print("Data fetched sucessfully!")

        data = response.json()

        if data["cod"] != 200:
            weather_result.set(f"Error: {data.get('message', 'Unknown error')}")
            return

        else:
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            if units == "metric":
                temp_unit = "°C"
            else:
                temp_unit = "°F"
                temperature = (temperature * 9/5) + 32



            weather_result.set(f"City: {city}\n"
                               f"Temperature: {temperature}°F"
                               f"Description: {weather_description.capitalize()}\n"
                               f"Humidity: {humidity}%\n"
                               f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        weather_result.set(f"Error fetching data: {str(e)}")
    except Exception as e:
        weather_result.set(f"Error: {str(e)}")

app = Tk()
app.title("Weather App")

Label(app, text="Enter City:").pack()
city_entry = Entry(app)
city_entry.pack()

unit_var = StringVar(value="metric")
unit_menu = OptionMenu(app, unit_var, "metric", "imperial")
unit_menu.pack()

Button(app, text="Get Weather", command=get_weather).pack()

weather_result = StringVar()
Label(app, textvariable=weather_result, wraplength=400).pack()

app.mainloop()
