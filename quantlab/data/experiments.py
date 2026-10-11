from enum import Enum
import scipy.stats as s
import pandas as pd

class Experiment:
    def __init__(self, name):
        self.name = name
        self.null_hypothesis = None
        self.alternative_hypothesis = None
        self.result = None
        self.significance_level = 0.05

    def set_null_hypothesis(self, hypothesis):
        self.null_hypothesis = hypothesis

    def set_alternative_hypothesis(self, hypothesis):
        self.alternative_hypothesis = hypothesis

    def set_result(self, result):
        self.result = result

    def set_significance_level(self, level):
        self.significance_level = level

    def set_data_value_computation(self, f):
        self.data_value_computation = f

    def calculate_t_stat(self, data):
        # Placeholder for t-statistic calculation
        # Right now the data.mean() is hardcoded to compare against the null hypothesis expected value,
        # it needs to be generalized
        mean_diff = self.data_value_computation(data) - self.null_hypothesis.expected_value
        std_err = data.std(ddof=1) / (data.shape[0] ** 0.5)
        t_stat = mean_diff / std_err
        return t_stat

    def calculate_p_value(self, data):
        df = data.shape[0]
        t_stat = self.calculate_t_stat(data)
        p_value = 2 * (1 - s.t.cdf(abs(t_stat), df))
        return p_value

    def run(self, data):
        p_value = self.calculate_p_value(data)
        if p_value < self.significance_level:
            self.set_result(ExperimentResult.REJECT_NULL)
        else:
            self.set_result(ExperimentResult.ACCEPT_NULL)

class ComparisonOperator(Enum):
    EQUAL = "=="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN_OR_EQUAL = "<="

class ExperimentResult(Enum):
    ACCEPT_NULL = "accept_null"
    REJECT_NULL = "reject_null"

class Hypothesis:
    def __init__(self, description):
        self.description = description
        self.attribute_name = None
        self.expected_value = None
        self.operator = None

def test_mean_return(dataorpath, company_symbol, mode='file'):
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
    if mode == 'file':
        combined_returns = pd.read_csv(dataorpath)
    elif mode == 'dataframe':
        combined_returns = dataorpath
    else:
        raise ValueError("Invalid mode. Use 'file' or 'dataframe'.")

    # Run the experiment with the loaded data
    experiment.run(combined_returns[company_symbol])
    print(f"Experiment Result: {experiment.result.value}")

def test_return_skewness(dataorpath, company_symbol, mode='file'):
    # Set up a new experiment to see if the return skewness is 0
    experiment = Experiment(f"Return Skewness = 0 Test - {company_symbol}")
    experiment.set_null_hypothesis(Hypothesis("Return skewness is 0"))
    experiment.null_hypothesis.attribute_name = "skewness"
    experiment.null_hypothesis.expected_value = 0
    experiment.null_hypothesis.operator = ComparisonOperator.EQUAL
    experiment.set_data_value_computation(lambda data: data.skew())

    # Optionally, set the significance level for the experiment
    experiment.set_significance_level(0.05)
    # The experiment is now fully set up and ready to be run with data
    if mode == 'file':
        combined_returns = pd.read_csv(dataorpath)
    elif mode == 'dataframe':
        combined_returns = dataorpath
    else:
        raise ValueError("Invalid mode. Use 'file' or 'dataframe'.")

    # Run the experiment with the loaded data
    experiment.run(combined_returns[company_symbol])
    print(f"Experiment Result: {experiment.result.value}")

def test_return_kurtosis(dataorpath, company_symbol, mode='file'):
    # Set up a new experiment to see if the return kurtosis is 0
    experiment = Experiment(f"Return Kurtosis = 0 Test - {company_symbol}")
    experiment.set_null_hypothesis(Hypothesis("Return kurtosis is 3"))
    experiment.null_hypothesis.attribute_name = "kurtosis"
    experiment.null_hypothesis.expected_value = 3
    experiment.null_hypothesis.operator = ComparisonOperator.EQUAL
    experiment.set_data_value_computation(lambda data: data.kurt())

    # Optionally, set the significance level for the experiment
    experiment.set_significance_level(0.05)
    # The experiment is now fully set up and ready to be run with data
    if mode == 'file':
        combined_returns = pd.read_csv(dataorpath)
    elif mode == 'dataframe':
        combined_returns = dataorpath
    else:
        raise ValueError("Invalid mode. Use 'file' or 'dataframe'.")

    # Run the experiment with the loaded data
    experiment.run(combined_returns[company_symbol])
    print(f"Experiment Result: {experiment.result.value}")
