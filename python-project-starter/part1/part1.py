import json
from datetime import datetime

with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

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
        An integer (?? SHOULD THIS BE FLOAT) representing a temperature in degrees celcius.
    """
    temp = float((float(temp_in_farenheit) - 32) * 5/9)
    return temp


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

if __name__ == "__main__":
    process_weather("data/forecast_5days_a.json")


print()
for key,value in forecast.items():
    if key == "DailyForecasts":
        # number_of_days = count the number of days available in dailyforecasts
        number_of_days = (len(value))
        print(f"{number_of_days} Day Overview")
        # for all dates in forecast
        dates = []
        low_temps = []
        high_temps = []
        daytime = []
        day_rain = []
        nighttime = []
        night_rain = []
        # lowest_temp = identify the lowest temp of the forecast
        # lowest_temp_date = identify the date of the lowest temp
        # print(f"    The lowest temperature will be {lowest_temp}{DEGREE_SYBMOL}, and will occur on {lowest_temp_date}{convert_date(iso_string)}.")
        # # highest_temp = identify the highest temp of the forecast
        # # highest_temp_date = identify the date of the highest temp
        # print(f"    The highest temperature will be {highest_temp}{DEGREE_SYBMOL}, and will occur on {highest_temp_date}.")
        # # avg_low_temp = average of low temperatures  calculate_mean(total, num_items)
        # print(f"    The average low this week is {mean_temp}.")
        # # avg_high_temp = average of high temperatures  calculate_mean(total, num_items)
        # print(f"    The average low this week is {calculate_mean(total, num_items)}.")
        # print()
        
        for day in value:
            for key1,data1 in day.items():
                # for each day in dailyforecast
                if key1 == "Date":
                    # d.strftime("%A %d %B %Y") = identify the Day Date Month Year
                    iso_string = data1
                    dates.append(iso_string)
                    print(f"-------- {convert_date(iso_string)} --------")
                # low_temp = identify the day's lowest temp, convert to celcius using function and add symbol
                if key1 == "Temperature":
                    for key2,value2 in data1.items():
                        if key2 == "Minimum":
                            for key3,value3 in value2.items():
                                if key3 == "Value":
                                    temp_in_farenheit = value3
                                    temp = convert_f_to_c(temp_in_farenheit)
                                    low_temps.append(format_temperature(temp))
                                    print(f"Minimum Temperature: {format_temperature(temp)}")
                # high_temp = identify the day's highest temp, convert to celcius using function and add symbol
                    for key2,value2 in data1.items():
                        if key2 == "Maximum":
                            for key3,value3 in value2.items():
                                if key3 == "Value":
                                    temp_in_farenheit = value3
                                    # print(value3)
                                    temp = convert_f_to_c(temp_in_farenheit)
                                    print(f"Maximum Temperature: {format_temperature(temp)}")
                # day_weather = identify text description of the day's weather
                if key1 == "Day":
                    for key2,value2 in data1.items():
                        if key2 == "LongPhrase":
                            print(f"Daytime: {value2}")
                # day_rain = identify the chance of daytime rain
                    for key2,value2 in data1.items():
                        if key2 == "RainProbability":
                            print(f"    Chance of rain: {value2:>2}%")
                # night_weather = identify text description of the night's weather
                if key1 == "Night":
                    for key2,value2 in data1.items():
                        if key2 == "LongPhrase":
                            print(f"Nighttime: {value2}")
                # night_rain = identify the chance of nighttime rain
                    for key2,value2 in data1.items():
                            if key2 == "RainProbability":
                                print(f"    Chance of rain: {value2:>2}%")
                                print()


        print(low_temps)
        total = sum(low_temps)
        num_items = (len(low_temps))
        calculate_mean(total, num_items)
        format_temperature(temp)
        print(calculate_mean(total, num_items))

print()
print()

print(dates)
print(low_temps)
print(high_temps)
print(daytime)
print(day_rain)
print(nighttime)
print(night_rain)

## DETAILS BELOW ARE FORMAT FOR OUTPUT ##








