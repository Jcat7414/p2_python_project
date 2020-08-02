import json
import plotly.express as px

with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

temps = ""

for item in forecast["DailyForecasts"]:
    min_temp = (item["Temperature"]["Minimum"]["Value"])
    max_temp = (item["Temperature"]["Maximum"]["Value"])
    min_real_feel = (item["RealFeelTemperature"]["Minimum"]["Value"])
    min_real_shade = (item["RealFeelTemperatureShade"]["Minimum"]["Value"])
    temps += f"Minimum: {min_temp}, Maximum: {max_temp}, Minimum Real Feel: {min_real_feel}, Minimum Real Feel Shade: {min_real_shade}\n"

print(temps)

# df = pd.read_json("data/forecast_5days_a.json")

# for item in json_file["DailyForecasts"]:
# fig = px.line(df, x={min_temp}, y={max_temp}, title="Minimum Temperature")
# fig.write_html(min_temp.html)
