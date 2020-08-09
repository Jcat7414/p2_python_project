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

with open("data/historical_24hours_a.json") as json_file:
    summary = json.load(json_file)

with open("day_summary.txt", "w") as txt_file:

    txt_file.write(f"==========  A Summary of Weather Activity  ==========\n")


    date = []
    times = []
    temps = []
    real_feels = []
    weather_text = []

    # data required for graphs
    for item in summary:
        iso_string = (item["LocalObservationDateTime"])  
        date.append(convert_date(iso_string))
        times.append(convert_time(iso_string))

        temp = (item["Temperature"]["Metric"]["Value"])
        temps.append(temp)

        real_feel = (item["RealFeelTemperature"]["Metric"]["Value"])
        real_feels.append(real_feel)

        weathertext = (item["WeatherText"])
        weather_text.append(weathertext)

    txt_file.write("\n")

    # data required for text output
    # when the minimum and maximum temperatures occured

    # min_temp = identify the minimum temp of the day
    min_temp = min(temps)
    # min_temp_time = identify the times of the minimum temp 
    min_temp_time = [i for i in range(len(temps)) if temps[i] == min_temp]
    min_temp_times = [times[i] for i in min_temp_time]
    txt_file.write(f"The minimum temperature was {min_temp:.1f}{DEGREE_SYBMOL}.\n")
    txt_file.write("The minimum temperature was recorded at {} and {}.\n" .format(", " .join(map(str,min_temp_times[0:-1])), min_temp_times[-1]))

    txt_file.write("\n")

    # max_temp = identify the maximum temp of the day
    max_temp = max(temps)
    # max_temp_time = identify the times of the maximum temp 
    max_temp_time = [i for i in range(len(temps)) if temps[i] == max_temp]
    max_temp_times = [times[i] for i in max_temp_time]
    txt_file.write(f"The maximum temperature was {max_temp:.1f}{DEGREE_SYBMOL}.\n")
    txt_file.write("The maximum temperature was recorded at {} and {}.\n" .format((', '.join(map(str,max_temp_times[0:-1]))), max_temp_times[-1]))

    txt_file.write("\n")

    # the amount of precipitation that fell in the 24 hours
    # identify PrecipitationSummary-Past24Hours-Metric-Value of the latest LocalObservationDateTime
    most_recent_dict = summary[0]
    precipitation_24hrs = most_recent_dict["PrecipitationSummary"]["Past24Hours"]["Metric"]["Value"]
    unit = most_recent_dict["PrecipitationSummary"]["Past24Hours"]["Metric"]["Unit"]
    txt_file.write(f"The amount of precipitation that fell in the last 24 hours was {precipitation_24hrs}{unit}.\n")

    # the number of hours that precipitation was recorded for
    #  count HasPrecipitation = true
    rained = []
    for item in summary:
        precip = (item["HasPrecipitation"])
        rained.append(precip)
        count_rain = 0
        for rain in rained:
            if rain == True:
                count_rain += 1
        num_hours = (len(rained))
    txt_file.write(f"Precipitation has been recorded in {count_rain} of the past {num_hours} hours.\n")

    txt_file.write("\n")

    # the number of daylight hours in the past 24 hours
    #  count of IsDayTime = true
    daylight = []
    for item in summary:
        daytime = (item["IsDayTime"])
        daylight.append(daytime)
        count_daytime = 0
        for daytime in daylight:
            if daytime == True:
                count_daytime += 1
        num_hours = (len(daylight))
    txt_file.write(f"There were {count_daytime} hours of daylight in the past {num_hours} hours.\n")

    #  the maximum UV index, and what hour(s) this occured
    # identify max UVIndex and corresponding LocalObservationDateTime (times)
    uv = []
    max_uv = []
    for item in summary:
        uv_index = (item["UVIndex"])
        uv.append(uv_index)
    max_uv_index = max(uv)
    uv_time = [i for i in range(len(uv)) if uv[i] == max_uv_index]
    max_uv_times = [times[i] for i in uv_time]
    txt_file.write("The maximum UV Index recorded was {}. This recording was received at {} and {}.".format(max_uv_index, (', '.join(map(str,max_uv_times[0:-1]))), max_uv_times[-1]))

    txt_file.write("\n")



df = {
    "Date": (date),
    "Times": (times),
    "Temperature": (temps),
    "Real Feel Temperature": (real_feels)
}

fig = px.box(
    df, 
    y=["Temperature", "Real Feel Temperature"],
    # y="Times",
    title="Temperature and Real Feel Temperature",
    points="all",
    labels ={"variable": "Type of Temperature", "value": "Degrees Celcius"}
)

fig.write_html("temp_real_feel_temp.html")


df = {
    "Weather Category": (weather_text),
    
}

fig = px.bar(
    df, 
    # x="Date",
    y=["Weather Category"],
    title="Weather By Category",
    labels ={"variable": "Weather", "value": "Categories", "count": "Number of occurences"},
    barmode="group"
)

fig.write_html("weather_text.html")
    