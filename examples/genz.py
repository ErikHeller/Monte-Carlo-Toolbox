# https://www.sfu.ca/~ssurjano/integration.html

import numpy as np

from direct_simulation import experiment_helper, RandomVectors, BasicExperiment
from visualizations import repeated_simulation


# https://www.sfu.ca/~ssurjano/cont.html
def genz_continuous_integrand(x, u, a):
    return np.exp(-np.sum(a * abs(x-u), axis=-1))


u = [0.5, 0.5]
a = [50, 50]

x = RandomVectors(n=50000, d=1)
basic_experiment = BasicExperiment(lambda x_i: genz_continuous_integrand(x_i, u, a), x)
exp_results = experiment_helper(basic_experiment, list(range(10, 50000, 10)), confidence_level=0.01)
repeated_simulation(exp_results, "genz_cont.html")
