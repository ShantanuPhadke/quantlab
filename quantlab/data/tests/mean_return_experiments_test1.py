from pathlib import Path
import pandas as pd
from quantlab.data.experiments import Experiment, Hypothesis, ExperimentResult, ComparisonOperator

def test_mean_return(company_symbol):
    # Set up a new experiment to see if the mean oercentage return is 0
    experiment = Experiment(f"Mean Percentage Return = 0 Test - {company_symbol}")
    experiment.set_null_hypothesis(Hypothesis("Mean percentage return is 0"))
    experiment.null_hypothesis.attribute_name = "mean_return"
    experiment.null_hypothesis.expected_value = 0
    experiment.null_hypothesis.operator = ComparisonOperator.EQUAL
    experiment.set_data_value_computation(lambda data: data.mean())

    # Optionally, set the significance level for the experiment
    experiment.set_significance_level(0.05)
    # The experiment is now fully set up and ready to be run with data
    BASE_DIR = Path(__file__).resolve().parent
    combined_returns = pd.read_csv(BASE_DIR / "../../../data/combined_returns.csv")

    # Run the experiment with the loaded data
    experiment.run(combined_returns[company_symbol])
    print(f"Experiment Result: {experiment.result.value}")


if __name__ == "__main__":
    test_mean_return("AXP")
    test_mean_return("CAT")
    test_mean_return("SBUX")
