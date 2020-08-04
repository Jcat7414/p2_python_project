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


def convert_time(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Hours Minutes
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%H:%M%p")


# with open("data/historical_24hours_a.json") as json_file:
#     summary = json.load(json_file)

    


# for key,value in summary.items():
#         if key == "DailyForecasts":
#             dates = []
#             min_temps = []
#             max_temps = []

#             for day in value:
#                 for key1,data1 in day.items():
#                     # for each day in dailyforecast
#                     if key1 == "Date":
#                         iso_string = data1
#                         dates.append(convert_date(iso_string))

#                     # min_temp = identify the day's minimum temp, convert to celcius using function and add symbol
#                     if key1 == "Temperature":
#                         for key2,value2 in data1.items():
#                             if key2 == "Minimum":
#                                 for key3,value3 in value2.items():
#                                     if key3 == "Value":
#                                         temp_in_farenheit = value3
#                                         temp = convert_f_to_c(temp_in_farenheit)
#                                         temp = round(temp,1)
#                                         min_temps.append(temp)

#                     # max_temp = identify the day's maximum temp, convert to celcius using function and add symbol
#                         for key2,value2 in data1.items():
#                             if key2 == "Maximum":
#                                 for key3,value3 in value2.items():
#                                     if key3 == "Value":
#                                         temp_in_farenheit = value3
#                                         temp = convert_f_to_c(temp_in_farenheit)
#                                         temp = round(temp,1)
#                                         max_temps.append(temp)


#         for key,value in forecast.items():
#             if key == "DailyForecasts":
#                 # number_of_days = count the number of days available in dailyforecasts
#                 number_of_days = (len(value))
#                 output += f"{number_of_days} Day Overview\n"
#                 txt_file.write(f"{number_of_days} Day Overview" + "\n")

#         # min_temp = identify the lowest temp of the forecast
#         # temp = min(min_temps)
#         temp = min(min_temps)
#         minpos = min_temps.index(min(min_temps))
#         # min_temp_date = identify the date of the lowest temp 
#         min_temp_date = dates[minpos]
#         format_temperature(temp)
#         output += f"    The lowest temperature will be {format_temperature(temp)}, and will occur on {min_temp_date}.\n"
#         txt_file.write(f"    The lowest temperature will be {format_temperature(temp)}, and will occur on {min_temp_date}." + "\n")

#         # max_temp = identify the highest temp of the forecast
#         # temp = max(max_temps)
#         temp = max(max_temps)
#         maxpos = max_temps.index(max(max_temps))
#         # max_temp_date = identify the date of the highest temp *** THERE ARE 2 THE SAME, MINE IS RETURNING THE 'OTHER DATE'
#         max_temp_date = dates[maxpos]
#         format_temperature(temp)
#         output += f"    The highest temperature will be {format_temperature(temp)}, and will occur on {max_temp_date}.\n"
#         txt_file.write(f"    The highest temperature will be {format_temperature(temp)}, and will occur on {max_temp_date}." + "\n")

#         # avg_low_temp = average of low temperatures  calculate_mean(total, num_items)
#         total = sum(min_temps)
#         num_items = (len(min_temps))
#         temp = calculate_mean(total, num_items)
#         format_temperature(temp)
#         output += f"    The average low this week is {format_temperature(temp)}.\n"
#         txt_file.write(f"    The average low this week is {format_temperature(temp)}." + "\n")

#         # avg_high_temp = average of high temperatures  calculate_mean(total, num_items)
#         total = sum(max_temps)
#         num_items = (len(max_temps))
#         temp = calculate_mean(total, num_items)
#         format_temperature(temp)
#         output += f"    The average high this week is {format_temperature(temp)}.\n"
#         txt_file.write(f"    The average high this week is {format_temperature(temp)}." + "\n")

#         output += "\n"
#         txt_file.write("\n")

#         for key,value in forecast.items():
#             if key == "DailyForecasts":
#                 # for all dates in forecast
#                 dates = []
#                 min_temps = []
#                 max_temps = []
                
#                 for day in value:
#                     for key1,data1 in day.items():
#                         # for each day in dailyforecast
#                         if key1 == "Date":
#                             iso_string = data1
#                             dates.append(convert_date(iso_string))
#                             output += f"-------- {convert_date(iso_string)} --------\n"
#                             txt_file.write(f"-------- {convert_date(iso_string)} --------" + "\n")

#                         # min_temp = identify the day's minimum temp, convert to celcius using function and add symbol
#                         if key1 == "Temperature":
#                             for key2,value2 in data1.items():
#                                 if key2 == "Minimum":
#                                     for key3,value3 in value2.items():
#                                         if key3 == "Value":
#                                             temp_in_farenheit = value3
#                                             temp = convert_f_to_c(temp_in_farenheit)
#                                             output += f"Minimum Temperature: {format_temperature(temp)}\n"
#                                             txt_file.write(f"Minimum Temperature: {format_temperature(temp)}" + "\n")

#                         # max_temp = identify the day's maximum temp, convert to celcius using function and add symbol
#                             for key2,value2 in data1.items():
#                                 if key2 == "Maximum":
#                                     for key3,value3 in value2.items():
#                                         if key3 == "Value":
#                                             temp_in_farenheit = value3
#                                             temp = convert_f_to_c(temp_in_farenheit)
#                                             output += f"Maximum Temperature: {format_temperature(temp)}\n"
#                                             txt_file.write(f"Maximum Temperature: {format_temperature(temp)}" + "\n")

#                         # day_weather = identify text description of the day's weather
#                         if key1 == "Day":
#                             for key2,value2 in data1.items():
#                                 if key2 == "LongPhrase":
#                                     output += f"Daytime: {value2}\n"
#                                     txt_file.write(f"Daytime: {value2}" + "\n")

#                         # day_rain = identify the chance of daytime rain
#                             for key2,value2 in data1.items():
#                                 if key2 == "RainProbability":
#                                     output += f"    Chance of rain:  {value2:>1}%\n"
#                                     txt_file.write(f"    Chance of rain:  {value2:>1}%" + "\n")

#                         # night_weather = identify text description of the night's weather
#                         if key1 == "Night":
#                             for key2,value2 in data1.items():
#                                 if key2 == "LongPhrase":
#                                     output += f"Nighttime: {value2}\n"
#                                     txt_file.write(f"Nighttime: {value2}" + "\n")

#                         # night_rain = identify the chance of nighttime rain
#                             for key2,value2 in data1.items():
#                                     if key2 == "RainProbability":
#                                         output += f"    Chance of rain:  {value2:>1}%\n"
#                                         txt_file.write(f"    Chance of rain:  {value2:>1}%" + "\n")
#                                         output += "\n"
#                                         txt_file.write("\n")

    # return txt_file
#     pass
# if __name__ == "__main__":
#     print(process_weather("data/historical_6hours.json"))

# GRAPH DATA BELOW HERE - FUNCTIONING CORRECTLY - DO NOT AMEND

with open("data/historical_24hours_a.json") as json_file:
    summary = json.load(json_file)

with open("day_summary.txt", "w") as txt_file:

    print(f"==========  A Summary of Weather Activity  ==========\n")
    txt_file.write(f"==========  A Summary of Weather Activity  ==========\n")


    date = []
    times = []
    temps = []
    real_feels = []
    weather_text = []


    for item in summary:
        iso_string = (item["LocalObservationDateTime"])  
        print(convert_date(iso_string))
        date.append(convert_date(iso_string))
        print(convert_time(iso_string)) 
        times.append(convert_time(iso_string))

        temp = (item["Temperature"]["Metric"]["Value"])
        print(temp)
        temps.append(temp)

        real_feel = (item["RealFeelTemperature"]["Metric"]["Value"])
        print(real_feel)
        real_feels.append(real_feel)

        weathertext = (item["WeatherText"])
        print(weathertext)
        weather_text.append(weathertext)

    print(date)
    print(times)
    print(temps)
    print(real_feels)
    print(weather_text)

    txt_file.write("\n")

    # when the minimum and maximum temperatures occured
    # min_temp = identify the lowest temp of the forecast
    min_temp = min(temps)
    # print(min_temp)
    minpos = temps.index(min(temps))
    # min_temp_time = identify the times of the minimum temp *** CURRENTLY ONLY RETURNING EARLIEST TIME, NOT ALL TIMES
    min_temp_time = times[minpos]
    # format_temperature(temp)
    print(f"The minimum temperature was {min_temp:.1f}{DEGREE_SYBMOL} and last occured at {min_temp_time}.\n")
    txt_file.write(f"The minimum temperature was {min_temp:.1f}{DEGREE_SYBMOL} and last occured at {min_temp_time}." + "\n")

    # max_temp = identify the maximum temp of the forecast
    max_temp = max(temps)
    maxpos = temps.index(max(temps))
    # max_temp_time = identify the times of the maximum temp *** CURRENTLY ONLY RETURNING EARLIEST TIME, NOT ALL TIMES
    max_temp_time = times[maxpos]
    # format_temperature(temp)
    print(f"The maximum temperature was {max_temp:.1f}{DEGREE_SYBMOL} and last occured at {max_temp_time}.\n")
    txt_file.write(f"The maximum temperature was {max_temp:.1f}{DEGREE_SYBMOL} and last occured at {max_temp_time}." + "\n")

    txt_file.write("\n")

    # the amount of precipitation that fell in the 24 hours
    # identify PrecipitationSummary-Past24Hours-Metric-Value of the latest LocalObservationDateTime
    most_recent_dict = summary[0]
    precipitation_24hrs = most_recent_dict["PrecipitationSummary"]["Past24Hours"]["Metric"]["Value"]
    unit = most_recent_dict["PrecipitationSummary"]["Past24Hours"]["Metric"]["Unit"]
    print(f"The amount of precipitation that fell in the last 24 hours was {precipitation_24hrs}{unit}.")
    txt_file.write(f"The amount of precipitation that fell in the last 24 hours was {precipitation_24hrs}{unit}.\n")

# the number of hours that precipitation was recorded for
#  count HasPrecipitation = true
    for item in summary:
        count_precip = []
        precip = item["HasPrecipitation"]
        count_precip.append(precip)
        print(count_precip)
        precip_count = sum(1 for item in count_precip if item == True)
        print(precip_count)
        hours_precip = sum(precip_count)
        print(hours_precip)
        # print(f"Precipitation has been recorded in {count_precip} of the past {precip} hours.")

# the number of daylight hours in the past 24 hours
#  count of IsDayTime = true

#  the maximum UV index, and what hour(s) this occured
# identify max UVIndex and corresponding LocalObservationDateTime (s)

#  txt_file.write(f"    The lowest temperature will be {format_temperature(temp)}, and will occur on {min_temp_date}." + "\n")


    

# df = {
#     "Date": (date),
#     "Times": (times),
#     "Temperature": (temps),
#     "Real Feel Temperature": (real_feels)
# }

# fig = px.box(
#     df, 
#     y=["Temperature", "Real Feel Temperature"],
#     # y="Times",
#     title="Temperature and Real Feel Temperature",
#     points="all",
#     labels ={"variable": "Type of Temperature", "value": "Degrees Celcius"}
# )

# fig.write_html("temp_real_feel_temp.html")


# df = {
#     "Weather Category": (weather_text),
    
# }

# fig = px.bar(
#     df, 
#     # x="Date",
#     y=["Weather Category"],
#     title="Weather By Category",
#     labels ={"variable": "Weather", "value": "Categories", "count": "Number of occurences"},
#     barmode="group"
# )

# fig.write_html("weather_text.html")
    