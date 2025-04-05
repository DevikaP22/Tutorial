import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("weather.csv")

#Print first 10 rows of weather data
print("First 10 rows of weather data:")
print(df.head(10))

# Find the maximum and minimum temperature
max_temperature = df["temperature"].max()
min_temperature = df["temperature"].min()
print("\nMaximum temperature:", max_temperature)
print("Minimum temperature:", min_temperature)

#List the places with temperature less than 28°C
places_less_than_28 = df[df["temperature"] < 28][["place", "temperature"]]
print("\nPlaces with temperature less than 28°C:")
print(places_less_than_28)

# List the places with weather = “Cloudy”
cloudy_places = df[df["weather"] == "Cloudy"][["place", "weather"]]
print("\nPlaces with weather = 'Cloudy':")
print(cloudy_places)

# Sort and display each weather and its frequency
weather_frequency = df["weather"].value_counts().sort_index()
print("\nWeather frequency:")
print(weather_frequency)

#Create a bar plot to visualize temperature of each day
plt.figure(figsize=(10,6))
plt.bar(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature of each day")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

