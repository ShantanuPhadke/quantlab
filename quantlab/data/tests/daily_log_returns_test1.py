import pandas as pd
import numpy as np
from pathlib import Path
from quantlab.data.returns import calculate_log_returns, calculate_returns_stats

BASE_DIR = Path(__file__).resolve().parent
combined_returns = pd.read_csv(BASE_DIR / "../../../data/combined_returns.csv")

# Transform simple returns to daily log returns

# Calculate daily log returns
daily_log_returns = calculate_log_returns(combined_returns.drop(columns=["Date"]))
daily_log_returns["Date"] = combined_returns["Date"]
print(daily_log_returns)

# log returns statistics
daily_log_returns_stats = calculate_returns_stats(daily_log_returns)
print(daily_log_returns_stats)
