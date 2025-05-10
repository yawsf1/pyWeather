import tkinter as tk
from tkinter import messagebox
import requests
import datetime

def get_weather(city):
    api_key = "33f8b9a358b9572037ec0b2ee0ae2a8f" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('cod') != 200:
                messagebox.showerror("Error", f"Error: {data.get('message', 'Unknown error')}")
                return
            
            main_data = data['main']
            weather_data = data['weather'][0]
            
            temperature = main_data['temp']
            humidity = main_data['humidity']
            description = weather_data['description']
            
            result_text = (
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Description: {description.capitalize()}"
            )
            
            result_label.config(text=result_text)
            
            log_weather_search(city, temperature, humidity, description)
        else:
            messagebox.showerror("Error", "Failed to fetch data from the API")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request failed: {e}")

def log_weather_search(city, temp, humidity, desc):
    with open("weather_history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(
            f"[{timestamp}] {city.title()} - Temp: {temp}°C, Humidity: {humidity}%, Description: {desc.capitalize()}\n"
        )

def on_get_weather_click():
    city = city_entry.get()
    if city:
        get_weather(city.strip())
    else:
        messagebox.showwarning("Input Error", "Please enter a city name!")

window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")

title_label = tk.Label(window, text="Weather App", font=("Arial", 24))
title_label.pack(pady=20)

city_label = tk.Label(window, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(window, font=("Arial", 14))
city_entry.pack(pady=5)

get_weather_button = tk.Button(window, text="Get Weather", font=("Arial", 14), command=on_get_weather_click)
get_weather_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

window.mainloop()
