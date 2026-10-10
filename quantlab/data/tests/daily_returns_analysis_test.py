# Read from the sample simple returns data in ../../data/combined_returns.csv
import pandas as pd
from pathlib import Path
from quantlab.data.returns import calculate_returns_stats

BASE_DIR = Path(__file__).resolve().parent

combined_returns = pd.read_csv(BASE_DIR / "../../../data/combined_returns.csv")

combined_statistics = calculate_returns_stats(combined_returns)
print(combined_statistics)