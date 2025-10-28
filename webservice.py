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

def plot_data(data, symbol, chart_type):
    dates = list(data.keys())
    prices = list(data.values())

    plt.figure(figsize=(10,5))
    if chart_type == "bar":
        plt.bar(dates, prices, color='skyblue')
    else:
        plt.plot(dates, prices, color='orange')

    plt.title(f"{symbol} Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("---Stock Data Analyzer---")
    
    symbol = input("Enter the stock symbol you are looking for (IBM, AAPL, TSLA, etc...): ").upper()
    
    print("\nChoose Time Series Function:")
    print("1. Intraday (within market hours)")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")
    function_choice = input("Enter your choice (1-4): ")
    
    function = get_time_series_function(function_choice)
    if function is None:
        print("Invalid choice. Exiting...")
        exit()
        
        print("\nChoose Chart Type:")
        print("1. Bar Chart")
        print("2. Line Chart")
        chart_choice = input("Enter your choice (1-2): ")
        
        chart_type = get_chart_type(chart_choice)
        if chart_type is None:
            print("Invalid choice. Exiting...")
            exit()
            
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
            
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
                print("Invalid date format. Exiting...")
                exit()
                
        if end_date < start_date:
            print("End date can't be before the start date. Exiting...")
            exit()
            
        data = get_api_data(symbol, function)
        time_series = extract_time_series(data)
        if time_series is None:
            print("No No data returned. Check your stock symbol. Exiting...")
            exit()
            
        filtered_data = filter_data(time_series, start_date, end_date)
        plot_data(filtered_data, symbol, chart_type)