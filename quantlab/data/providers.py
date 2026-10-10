import yfinance as yf

class YFinanceProvider:
    def __init__(self):
        pass

    def get_stock_data(self, ticker, start=None, end=None):
        data = yf.download(ticker, start=start, end=end)
        # Move the Date index into a regular column
        data.reset_index(inplace=True)
        return data

