from providers import YFinanceProvider
from returns import calculate_simple_returns
from combiner import combine_dataframes
from writer import save_dataframe_to_csv

import pandas as pd

yfinance_provider = YFinanceProvider()
axp_data = yfinance_provider.get_stock_data("AXP", start="1993-12-31", end="2003-12-31")
#print(axp_data.head())
axp_returns = calculate_simple_returns(axp_data, column="Open")
axp_returns['Date'] = axp_data['Date']
axp_returns['Date'] = pd.to_datetime(axp_returns['Date'])

cat_data = yfinance_provider.get_stock_data("CAT", start="1993-12-31", end="2003-12-31")
cat_returns = calculate_simple_returns(cat_data, column="Open")
cat_returns['Date'] = cat_data['Date']
cat_returns['Date'] = pd.to_datetime(cat_returns['Date'])

starbucks_data = yfinance_provider.get_stock_data("SBUX", start="1993-12-31", end="2003-12-31")
starbucks_returns = calculate_simple_returns(starbucks_data, column="Open")
starbucks_returns['Date'] = starbucks_data['Date']
starbucks_returns['Date'] = pd.to_datetime(starbucks_returns['Date'])

combined_returns = combine_dataframes(axp_returns, cat_returns, on_column="Date")
combined_returns = combine_dataframes(combined_returns, starbucks_returns, on_column="Date")

save_dataframe_to_csv(combined_returns, "../../data/combined_returns.csv")