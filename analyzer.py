# analyzer.py

def calculate_moving_average(df, window=20):
    df[f'{window}_SMA'] = df['close'].rolling(window=window).mean()
    return df

def calculate_daily_returns(df):
    df['daily_return'] = df['close'].pct_change()
    return df

if __name__ == "__main__":
    from data_fetcher import fetch_stock_data
    df = fetch_stock_data('AAPL')
    df = calculate_moving_average(df)
    df = calculate_daily_returns(df)
    print(df.head())
