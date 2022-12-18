import numpy as np
import scipy.stats


def hoeffding(repetitions: np.ndarray, delta: float) -> np.ndarray:
    """
    Create confidence intervals for a direct simulation using Hoeffding's inequality.
    #ToDo: Assumptions

    :param repetitions: Number of repetitions used during simulation
    :param delta: Confidence level, must be in interval (0,1). A confidence level of 0.05 corresponds to a probability
        of 95% that the confidence interval contains the value to be simulated.
    :return: L_n, the one-sided length of the confidence interval. To calculate the ends of the confidence interval for
        a given list of simulation values D_n, calculate [D_n - L_n, D_n + L_n]
    """
    assert (0 < delta < 1)
    return np.sqrt(np.divide(np.log(2 / delta), np.multiply(2, repetitions)))


def clt(repetitions: np.ndarray, variances: np.ndarray, delta: float) -> np.ndarray:
    """
    Create asymptotic confidence intervals for a direct simulation using the central limit theorem (CLT).

    :param repetitions: Number of repetitions used during simulation
    :param delta: Confidence level, must be in interval (0,1). A confidence level of 0.05 corresponds to a probability
        of 95% that the confidence interval contains the value to be simulated.
    :param variances: Empirical variances of the underlying basic experiment
    :return: L_n, the one-sided length of the confidence interval. To calculate the ends of the confidence interval for
        a given list of simulation values D_n, calculate [D_n - L_n, D_n + L_n]
    """
    assert (0 < delta < 1)
    # ToDo: confidence level
    return scipy.stats.norm.ppf(1 - (delta / 2)) * np.sqrt(np.divide(variances, repetitions))
