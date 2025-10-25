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

def extract_time_series(data):
    for key in data.keys():
        if "Time Series" in key:
            return data[key]
    return None

def filter_data(time_series, start_date, end_date):
    filtered = {}
    for date_str, values in time_series.items():
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        if start_date <= date <= end_date:
            filtered[date] = float(values["4. close"])
    return dict(sorted(filtered.items()))

def plot_data (data, symbol, chart_type):
    dates = list (date.keys())
    prices = list (data.values())

    plt.figure(figsize=(10,5))
    if chart_type == "bar":
        plt.bar(dates, prices, color='skyblue')
    else:
        plt.plot(dates, prices, color='orange')

    plt.title(f"{symbol} Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.tight_layout()
    plt.show()

while True:
    print("Stock Data Visualizer\n--------------------------")