import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_api_data(symbol, function):
    api_key = "2O7W9WY18QMH3DXR"
    if function == "TIME_SERIES_INTRADAY":
        interval = "5min"
        url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}"
    else:
        url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}"
    
    response = requests.get(url)
    data = response.json()
    return data

def get_time_series_function(choice):
    functions = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }
    return functions.get(choice, None)

def get_chart_type(choice):
    chart_types = {
        "1": "bar",
        "2": "line"
    }
    return chart_types.get(choice, None)