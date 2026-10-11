from quantlab.data.providers import YFinanceProvider
from quantlab.data.returns import calculate_simple_returns, calculate_returns_stats, calculate_log_returns
from quantlab.data.combiner import combine_dataframes
from quantlab.data.writer import save_dataframe_to_csv
from quantlab.data.experiments import test_mean_return

import pandas as pd

yfinance_provider = YFinanceProvider()
ibm_data = yfinance_provider.get_stock_data("IBM", start="1985-12-31", end="2003-12-31", interval="1mo")
ibm_returns = calculate_simple_returns(ibm_data, column="Open")
ibm_returns['Date'] = ibm_data['Date']
ibm_returns['Date'] = pd.to_datetime(ibm_returns['Date'])

spx_data = yfinance_provider.get_stock_data("^SPX", start="1985-12-31", end="2003-12-31", interval="1mo")
spx_returns = calculate_simple_returns(spx_data, column="Open")
spx_returns['Date'] = spx_data['Date']
spx_returns['Date'] = pd.to_datetime(spx_returns['Date'])

combined_returns = combine_dataframes(ibm_returns, spx_returns, on_column="Date")
print(combined_returns.head())

combined_statistics = calculate_returns_stats(combined_returns)
print(combined_statistics)

daily_log_returns = calculate_log_returns(combined_returns.drop(columns=["Date"]))
daily_log_returns["Date"] = combined_returns["Date"]
print(daily_log_returns)

daily_log_returns_stats = calculate_returns_stats(daily_log_returns)
print(daily_log_returns_stats)

test_mean_return(combined_returns, "IBM", mode='dataframe')
test_mean_return(combined_returns, "^SPX", mode='dataframe')