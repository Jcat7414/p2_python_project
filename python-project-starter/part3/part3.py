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


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        forecast = json.load(json_file)

    output = ""
   
    print()
    for key,value in forecast.items():
        if key == "DailyForecasts":
            dates = []
            min_temps = []
            max_temps = []

            for day in value:
                for key1,data1 in day.items():
                    # for each day in dailyforecast
                    if key1 == "Date":
                        iso_string = data1
                        dates.append(convert_date(iso_string))

                    # min_temp = identify the day's minimum temp, convert to celcius using function and add symbol
                    if key1 == "Temperature":
                        for key2,value2 in data1.items():
                            if key2 == "Minimum":
                                for key3,value3 in value2.items():
                                    if key3 == "Value":
                                        temp_in_farenheit = value3
                                        temp = convert_f_to_c(temp_in_farenheit)
                                        temp = round(temp,1)
                                        min_temps.append(temp)

                    # max_temp = identify the day's maximum temp, convert to celcius using function and add symbol
                        for key2,value2 in data1.items():
                            if key2 == "Maximum":
                                for key3,value3 in value2.items():
                                    if key3 == "Value":
                                        temp_in_farenheit = value3
                                        temp = convert_f_to_c(temp_in_farenheit)
                                        temp = round(temp,1)
                                        max_temps.append(temp)

    with open("forecast_output.txt", "w") as txt_file:

        for key,value in forecast.items():
            if key == "DailyForecasts":
                # number_of_days = count the number of days available in dailyforecasts
                number_of_days = (len(value))
                output += f"{number_of_days} Day Overview\n"
                txt_file.write(f"{number_of_days} Day Overview" + "\n")

        # min_temp = identify the lowest temp of the forecast
        # temp = min(min_temps)
        temp = min(min_temps)
        minpos = min_temps.index(min(min_temps))
        # min_temp_date = identify the date of the lowest temp 
        min_temp_date = dates[minpos]
        format_temperature(temp)
        output += f"    The lowest temperature will be {format_temperature(temp)}, and will occur on {min_temp_date}.\n"
        txt_file.write(f"    The lowest temperature will be {format_temperature(temp)}, and will occur on {min_temp_date}." + "\n")

        # max_temp = identify the highest temp of the forecast
        # temp = max(max_temps)
        temp = max(max_temps)
        maxpos = max_temps.index(max(max_temps))
        # max_temp_date = identify the date of the highest temp *** THERE ARE 2 THE SAME, MINE IS RETURNING THE 'OTHER DATE'
        max_temp_date = dates[maxpos]
        format_temperature(temp)
        output += f"    The highest temperature will be {format_temperature(temp)}, and will occur on {max_temp_date}.\n"
        txt_file.write(f"    The highest temperature will be {format_temperature(temp)}, and will occur on {max_temp_date}." + "\n")

        # avg_low_temp = average of low temperatures  calculate_mean(total, num_items)
        total = sum(min_temps)
        num_items = (len(min_temps))
        temp = calculate_mean(total, num_items)
        format_temperature(temp)
        output += f"    The average low this week is {format_temperature(temp)}.\n"
        txt_file.write(f"    The average low this week is {format_temperature(temp)}." + "\n")

        # avg_high_temp = average of high temperatures  calculate_mean(total, num_items)
        total = sum(max_temps)
        num_items = (len(max_temps))
        temp = calculate_mean(total, num_items)
        format_temperature(temp)
        output += f"    The average high this week is {format_temperature(temp)}.\n"
        txt_file.write(f"    The average high this week is {format_temperature(temp)}." + "\n")

        output += "\n"
        txt_file.write("\n")

        for key,value in forecast.items():
            if key == "DailyForecasts":
                # for all dates in forecast
                dates = []
                min_temps = []
                max_temps = []
                
                for day in value:
                    for key1,data1 in day.items():
                        # for each day in dailyforecast
                        if key1 == "Date":
                            iso_string = data1
                            dates.append(convert_date(iso_string))
                            output += f"-------- {convert_date(iso_string)} --------\n"
                            txt_file.write(f"-------- {convert_date(iso_string)} --------" + "\n")

                        # min_temp = identify the day's minimum temp, convert to celcius using function and add symbol
                        if key1 == "Temperature":
                            for key2,value2 in data1.items():
                                if key2 == "Minimum":
                                    for key3,value3 in value2.items():
                                        if key3 == "Value":
                                            temp_in_farenheit = value3
                                            temp = convert_f_to_c(temp_in_farenheit)
                                            output += f"Minimum Temperature: {format_temperature(temp)}\n"
                                            txt_file.write(f"Minimum Temperature: {format_temperature(temp)}" + "\n")

                        # max_temp = identify the day's maximum temp, convert to celcius using function and add symbol
                            for key2,value2 in data1.items():
                                if key2 == "Maximum":
                                    for key3,value3 in value2.items():
                                        if key3 == "Value":
                                            temp_in_farenheit = value3
                                            temp = convert_f_to_c(temp_in_farenheit)
                                            output += f"Maximum Temperature: {format_temperature(temp)}\n"
                                            txt_file.write(f"Maximum Temperature: {format_temperature(temp)}" + "\n")

                        # day_weather = identify text description of the day's weather
                        if key1 == "Day":
                            for key2,value2 in data1.items():
                                if key2 == "LongPhrase":
                                    output += f"Daytime: {value2}\n"
                                    txt_file.write(f"Daytime: {value2}" + "\n")

                        # day_rain = identify the chance of daytime rain
                            for key2,value2 in data1.items():
                                if key2 == "RainProbability":
                                    output += f"    Chance of rain:  {value2:>1}%\n"
                                    txt_file.write(f"    Chance of rain:  {value2:>1}%" + "\n")

                        # night_weather = identify text description of the night's weather
                        if key1 == "Night":
                            for key2,value2 in data1.items():
                                if key2 == "LongPhrase":
                                    output += f"Nighttime: {value2}\n"
                                    txt_file.write(f"Nighttime: {value2}" + "\n")

                        # night_rain = identify the chance of nighttime rain
                            for key2,value2 in data1.items():
                                    if key2 == "RainProbability":
                                        output += f"    Chance of rain:  {value2:>1}%\n"
                                        txt_file.write(f"    Chance of rain:  {value2:>1}%" + "\n")
                                        output += "\n"
                                        txt_file.write("\n")

    return output

if __name__ == "__main__":
    print(process_weather("data/historical_24hours_a.json"))

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
    