# visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_data(df, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close Price')
    if '20_SMA' in df.columns:
        plt.plot(df.index, df['20_SMA'], label='20-day SMA')
    plt.title(f'{symbol} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_daily_returns(df, symbol):
    plt.figure(figsize=(14, 7))
    sns.histplot(df['daily_return'].dropna(), bins=50, kde=True)
    plt.title(f'{symbol} Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    from data_fetcher import fetch_stock_data
    from analyzer import calculate_moving_average, calculate_daily_returns

    symbol = 'AAPL'
    df = fetch_stock_data(symbol)
    df = calculate_moving_average(df)
    df = calculate_daily_returns(df)
    plot_stock_data(df, symbol)
    plot_daily_returns(df, symbol)
