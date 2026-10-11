from pathlib import Path
import pandas as pd
from quantlab.data.experiments import test_return_skewness, test_return_kurtosis

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    test_return_skewness(BASE_DIR / "../../../data/combined_returns.csv", "AXP")
    test_return_kurtosis(BASE_DIR / "../../../data/combined_returns.csv", "AXP")
