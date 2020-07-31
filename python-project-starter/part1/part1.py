import json
from datetime import datetime

with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

# print(forecast)

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius
    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer (?? SHOULD THIS BE FLOAT) representing a temperature in degrees celcius.
    """
    temp_in_celsius = int((float(temp_in_farenheit) - 32) * 5/9)
    return temp_in_celcius


def calculate_mean(total, num_items):
    """Calculates the mean.

    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean_temp = float(int(total) / int(num_items))
    return mean_temp


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass

headline = forecast[0]
dailyforecasts = forecast[1:]

weather_forecast_data = []

print()
for key,value in forecast.items():
    print()
    if key == "DailyForecasts":
        print(key)
        for day,data in key.items():
            print(day)
            # for key1,data1 in day.items():
            #     if key1 == "Date":
            #         print(data1)

print()
print()

## DETAILS BELOW ARE FORMAT FOR OUTPUT ##
# # number_of_days = count the number of days data available
# print(f"{number_of_days} Day Overview")

# # for all dates in forecast
# # lowest_temp = identify the lowest temp of the forecast
# # lowest_temp_date = identify the date of the lowest temp
# print(f"    The lowest temperature will be {lowest_temp}{DEGREE_SYBMOL}, and will occur on {lowest_temp_date}.")
# # highest_temp = identify the highest temp of the forecast
# # highest_temp_date = identify the date of the highest temp
# print(f"    The highest temperature will be {highest_temp}{DEGREE_SYBMOL}, and will occur on {highest_temp_date}.")
# # avg_low_temp = average of low temperatures
# print(f"    The average low this week is {avg_low_temp}{DEGREE_SYBMOL}.")
# # avg_high_temp = average of high temperatures
# print(f"    The average low this week is {avg_high_temp}{DEGREE_SYBMOL}.")
# print()


# for each day in dailyforecast
# d.strftime("%A %d %B %Y") = identify the Day Date Month Year
# print(f"-------- {d.strftime} --------")
# # low_temp = identify the day's lowest temp, convert to celcius using function
# print(f"Minimum Temperature: {low_temp:>22}{DEGREE_SYBMOL}")
# # high_temp = identify the day's highest temp, convert to celcius using function
# print(f"Maximum Temperature: {high_temp:>22}{DEGREE_SYBMOL}")
# # day_weather = identify text description of the day's weather
# print(f"Daytime: {day_weather}")
# # day_rain = identify the chance of daytime rain
# print(f"    Chance of rain: {day_rain:>22}")
# # night_weather = identify text description of the night's weather
# print(f"Nighttime: {night_weather}")
# # night_rain = identify the chance of nighttime rain
# print(f"    Chance of rain: {night_rain:>22}")
# print()




