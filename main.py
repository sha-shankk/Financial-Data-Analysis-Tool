# main.py

from data_fetcher import fetch_stock_data
from analyzer import calculate_moving_average, calculate_daily_returns
from visualizer import plot_stock_data, plot_daily_returns

def main():
    symbol = 'AAPL'
    df = fetch_stock_data(symbol)
    df = calculate_moving_average(df)
    df = calculate_daily_returns(df)
    plot_stock_data(df, symbol)
    plot_daily_returns(df, symbol)

if __name__ == "__main__":
    main()
