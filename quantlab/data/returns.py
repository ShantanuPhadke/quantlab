import pandas as pd
import numpy as np

def calculate_simple_returns(prices, column):
    return prices[column].pct_change()[1:]

def calculate_returns_stats(returns):
    returns_without_date = returns.drop(columns=["Date"])
    return pd.DataFrame({
        "Mean": returns_without_date.mean(),
        "Standard Deviation": returns_without_date.std(),
        "Skewness": returns_without_date.skew(),
        "Excess Kurtosis": returns_without_date.kurtosis() - 3,
        "Minimum": returns_without_date.min(),
        "Maximum": returns_without_date.max()
    })

def calculate_log_returns(simple_returns_pct):
    return 100 * np.log(1 + simple_returns_pct/100)
