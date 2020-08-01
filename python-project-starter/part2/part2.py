import json
import plotly.express as px
import pandas as pd

with open("data/forecast_5days_a.json") as json_file:
    forecast = json.load(json_file)

df = pd.read_json("data/forecast_5days_a.json")

# for item in json_file["DailyForecasts"]:
fig = px.line(df, x=(item["Temperature"]['Minimum']["Value"]), y=(item["Date"]), title="Minimum Temperature")
fig.write_html(min_temp.html)
