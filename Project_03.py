#Project 3

import requests
import pygal
import webbrowser
from datetime import datetime

API_KEY = "demo"#Find API Alpha Vantage Key

def main():
    def get_data(symbol): 
        #fetch data from Alpha Vantage API
        url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={API_KEY}&outputsize=full"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def parse_data(data, start_date, end_date):
        #parse data from API response
        time_series = [k for k in data.keys() if "Time Series" in k][0]
        all_data = data[time_series_key]
        filtered_data = {
            data: values for data, values in all_data.items()
            if start_date <= date <= end_date
        }
        sortred_dates = sorted(filtered_data.keys())
        return sorted_datas, filtered_data

    def create_chart(dates, stock_data, chart_type, symbol):
        #Create line chart using Pygal
        chart = pygal.Line(x_label_rotation=45) if chart_type == 2 else pygal.Bar(x_label_rotation=45)
        chart.title = f"Stock Data for {symbol}"
        chart.x_labels = dates

        opens, highs, lows, closes = [], [], [], []
        for d in dates:
            opens.append(stock_data[date]["1. open"])
            highs.append(stock_data[date]["2. high"])
            lows.append(stock_data[date]["3. low"])
            closes.append(stock_data[date]["4. close"])

        chart.add("Open", opens)
        chart.add("High", highs)
        chart.add("Low", lows)
        chart.add("Close", closes)

        filename = "stock_chart.html"
        chart.render_to_file(filename)
        webbrowser.open_new_tab(filename)
        
    def main():
        while True:
            print("\nStock Data Analyzer")
            print("--------------------")
            symbol = input("Enter the stock symbol you are looking for: ").upper()

            print("\nChart Types\n1. Bar\n2. Line\n")#3. Exit")
            chart_type = int(input("Enter the chart type you want: (1, 2)"))

            print("\nSelect the Time Series of the chart you want to Generate")
            print("1. Intraday (within market hours)\n2. Daily\n3. Weekly\n4. Monthly\n")
            time_option = int(input("Enter the time series you want: (1, 2, 3, 4): "))

            functions = {
                1: "TIME_SERIES_INTRADAY&interval=60min",
                2: "TIME_SERIES_DAILY",
                3: "TIME_SERIES_WEEKLY",
                4: "TIME_SERIES_MONTHLY"
            }
            function = functions[time_option]

            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")

            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                if end_object < start_object:
                    print("The end date can't be before the start date.")
                    continue
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                continue

            print("\nGenerating chart, please wait...\n")
            try:
                data = get_data(symbol, function)
                dates, stock_data = parse_data(data, start_date, end_date)
                if not dates:
                    print("No data found for the specified date range.")
                    continue
                create_chart(dates, stock_data, chart_type, symbol)
                print("Chart generated successfully and opened in browser!")
            except Exception as e:
                print("f Error:", e)
                
            again = input("\nDo you want to generate another chart? (yes/no): ").lower()
            if again.lower() != "yes":
                break