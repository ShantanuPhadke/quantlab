import yfinance as yf
import pandas as pd
from quantlab.data.combiner import combine_dataframes

class YFinanceProvider:
    def __init__(self):
        pass

    def get_stock_data(self, ticker, start=None, end=None, interval="1d"): 
        data = yf.download(ticker, start=start, end=end, interval=interval)
        data.reset_index(inplace=True)
        return data

    def get_stocks_data(self, tickers, start=None, end=None, interval="1d"):
        data_dict = {}
        for ticker in tickers:
            data_dict[ticker] = self.get_stock_data(ticker, start=start, end=end, interval=interval)
        combined_data = None
        for ticker, data in data_dict.items():
            if combined_data is None:
                combined_data = data
            else:
                combined_data = combine_dataframes(combined_data, data, on_column="Date")
        return combined_data

