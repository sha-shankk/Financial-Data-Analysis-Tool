# data_fetcher.py

import requests
import pandas as pd

ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

def fetch_stock_data(symbol, interval='1min', outputsize='compact'):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': ALPHA_VANTAGE_API_KEY,
        'outputsize': outputsize,
        'datatype': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if "Time Series" not in data:
        raise ValueError("Error fetching data from Alpha Vantage API")
    time_series = data[f'Time Series ({interval})']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    return df

if __name__ == "__main__":
    df = fetch_stock_data('AAPL')
    print(df.head())
