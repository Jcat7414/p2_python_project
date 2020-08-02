import json
import plotly.express as px
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    temp = float(temp)
    return f"{temp:.1f}{DEGREE_SYBMOL}"

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
        An integer representing a temperature in degrees celcius.
    """
    temp = float((float(temp_in_farenheit) - 32) * 5/9)
    temp = round(temp,1)
    return temp


def calculate_mean(total, num_items):
    """Calculates the mean.

    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean_temp = float(float(total) / int(num_items))
    mean_temp = round(mean_temp,1)
    return mean_temp


# def process_weather(forecast_file):
#     """Converts raw weather data into meaningful text.

#     Args:
#         forecast_file: A string representing the file path to a file
#             containing raw weather data.
#     Returns:
#         A string containing the processed and formatted weather data.
#     """
with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

dates = []
min_temps = []
max_temps = []
min_real_feels = []
min_real_shades = []

for item in forecast["DailyForecasts"]:
    iso_string = (item["Date"])  
    print(convert_date(iso_string)) 
    dates.append(convert_date(iso_string))

    min_temp = (item["Temperature"]["Minimum"]["Value"])
    temp_in_farenheit = min_temp
    convert_f_to_c(temp_in_farenheit)
    print(convert_f_to_c(temp_in_farenheit))
    min_temps.append(convert_f_to_c(temp_in_farenheit))

    max_temp = (item["Temperature"]["Maximum"]["Value"])
    temp_in_farenheit = max_temp
    convert_f_to_c(temp_in_farenheit)
    print(convert_f_to_c(temp_in_farenheit))
    max_temps.append(convert_f_to_c(temp_in_farenheit))

    min_real_feel = (item["RealFeelTemperature"]["Minimum"]["Value"])
    temp_in_farenheit = min_real_feel
    convert_f_to_c(temp_in_farenheit)
    print(convert_f_to_c(temp_in_farenheit))
    min_real_feels.append(convert_f_to_c(temp_in_farenheit))

    min_real_shade = (item["RealFeelTemperatureShade"]["Minimum"]["Value"])
    temp_in_farenheit = min_real_shade
    convert_f_to_c(temp_in_farenheit)
    print(convert_f_to_c(temp_in_farenheit))
    min_real_shades.append(convert_f_to_c(temp_in_farenheit))

    # return temps

print(dates)
print(min_temps)
print(max_temps)
print(min_real_feels)
print(min_real_shades)

# if __name__ == "__main__":
#     print(process_weather("data/forecast_5days_a.json"))

df = {
    "Date": (dates),
    "Minimum": (min_temps),
    "Maximum": (max_temps)
}

fig = px.line(
    df, 
    x="Date",
    y=["Minimum", "Maximum"],
    title="Minimum and Maximum Temperature - Daily",
    labels ={"variable": "Temperature", "value": "Temperature in degrees celcius"}
)

fig.write_html("daily_min_max_temp.html")


df = {
    "Date": (dates),
    "Minimum": (min_temps),
    "Minimum Real Feel": (min_real_feels),
    "Minimum Real Feel Shade": (min_real_shades)
}

fig = px.bar(
    df, 
    x="Date",
    y=["Minimum", "Minimum Real Feel", "Minimum Real Feel Shade"],
    title="Minimum Temperature - Daily",
    labels ={"variable": "Temperature", "value": "Temperature in degrees celcius"},
    barmode="group"
)

fig.write_html("daily_min_temps.html")
    