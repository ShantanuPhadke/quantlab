from pathlib import Path
import pandas as pd
from quantlab.data.experiments import test_mean_return

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    test_mean_return(BASE_DIR / "../../../data/combined_returns.csv", "AXP")
    test_mean_return(BASE_DIR / "../../../data/combined_returns.csv", "CAT")
    test_mean_return(BASE_DIR / "../../../data/combined_returns.csv", "SBUX")
