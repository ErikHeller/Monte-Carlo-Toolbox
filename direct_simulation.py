from typing import Callable

import numpy as np
from tqdm import tqdm

from confidence_intervals import clt


# https://numpy.org/doc/stable/user/basics.subclassing.html
# https://numpy.org/doc/stable/user/basics.interoperability.html#basics-interoperability

class RandomVectors(np.ndarray):
    def __new__(cls, values: np.ndarray = None, n: int = None, d: int = None, seed: int = None, **kwargs):
        if values:
            return values

        if not (n and d):
            raise ValueError("Either provide existing values as a numpy array or specify the number and dimensions of "
                             "the random vectors to be generated.")

        rng = np.random.default_rng(seed)
        return rng.uniform(low=0.0, high=1.0, size=(n, d))


class BasicExperiment(np.ndarray):
    def __new__(cls, function: Callable[[RandomVectors], np.ndarray], x: RandomVectors):
        # ToDo: Use exception
        assert (x.shape[0] > 1)
        basic_experiment = function(x).view(BasicExperiment)
        basic_experiment.x = x
        basic_experiment.function = function
        return basic_experiment


class ExperimentResults:
    def __init__(self, values: np.ndarray, repetitions: np.ndarray, variances: np.ndarray = None,
                 confidence_intervals: tuple[np.ndarray, np.ndarray] = None, confidence_level: float = None):
        self.values = values,
        self.repetitions = repetitions,
        self.variances = variances
        self.confidence_intervals = confidence_intervals
        self.confidence_level = confidence_level


# Methods ==========

def direct_simulation(basic_experiment: BasicExperiment, n: int):
    # ToDo: Use exceptions
    assert (1 < n <= basic_experiment.shape[0])
    y = basic_experiment[:n]
    result = 1 / n * np.sum(y, axis=0)
    return result


def empirical_variance(data: np.ndarray, average: np.ndarray):
    n = data.shape[0]
    v = 1 / (n - 1) * np.sum(np.power(data, 2), axis=0) - n / (n - 1) * np.power(average, 2)
    non_zero = (v > 0).astype(int)
    return np.power(v, non_zero)  # Assure strictly positive variances


def experiment_helper(basic_experiment: BasicExperiment, repetitions: list[int],
                      calculate_variances=True, confidence_level=0.05) -> ExperimentResults:
    variances = np.zeros(len(repetitions))
    values = np.zeros(len(repetitions))
    confidence_intervals = [np.zeros(len(repetitions)), np.zeros(len(repetitions))]

    i = 0
    for n in tqdm(repetitions):
        values[i] = direct_simulation(basic_experiment, n)
        if calculate_variances:
            variances[i] = empirical_variance(basic_experiment[:n], values[i])
        i = i + 1

    repetitions = np.array(repetitions)

    interval_lengths = clt(repetitions, variances, confidence_level)
    confidence_intervals[0] = values - interval_lengths
    confidence_intervals[1] = values + interval_lengths

    if not calculate_variances:
        variances = None
        confidence_intervals = None
        confidence_level = None

    return ExperimentResults(values, np.array(repetitions, dtype=int), variances,
                             tuple(confidence_intervals), confidence_level)
