import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data from the OpenWeatherMap API
def get_weather(city):
    api_key = "33f8b9a358b9572037ec0b2ee0ae2a8f"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Constructing the URL
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    # Making the request
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Checking if the response was successful
        if response.status_code == 200:
            data = response.json()
            
            # Check if the city data is returned correctly
            if data.get('cod') != 200:
                messagebox.showerror("Error", f"Error: {data.get('message', 'Unknown error')}")
                return
            
            # Extracting the necessary information from the JSON response
            main_data = data['main']
            weather_data = data['weather'][0]
            
            temperature = main_data['temp']
            humidity = main_data['humidity']
            description = weather_data['description']
            
            # Updating the UI with the fetched data
            result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description.capitalize()}")
        else:
            messagebox.showerror("Error", "Failed to fetch data from the API")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request failed: {e}")

# Function to trigger when the "Get Weather" button is clicked
def on_get_weather_click():
    city = city_entry.get()
    
    if city:
        get_weather(city)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name!")

# Setting up the Tkinter window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")

# Title Label
title_label = tk.Label(window, text="Weather App", font=("Arial", 24))
title_label.pack(pady=20)

# City input field
city_label = tk.Label(window, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(window, font=("Arial", 14))
city_entry.pack(pady=5)

# Get Weather button
get_weather_button = tk.Button(window, text="Get Weather", font=("Arial", 14), command=on_get_weather_click)
get_weather_button.pack(pady=20)

# Label to display weather results
result_label = tk.Label(window, text="", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
