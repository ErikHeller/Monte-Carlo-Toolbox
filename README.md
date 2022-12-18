# Monte-Carlo-Toolbox
A collection of Monte Carlo Methods written in Python.

## Feature Roadmap

- [ ] Direct Simulation
- [ ] Helpers for repeating and tracing experiments
- [ ] Visualizations for experiments
  - [ ] Simulation results vs. number of repetitions
  - [ ] log-log-plot for showing rate of convergence
  - [ ] Trajectory plots
  - [ ] Histograms
- [ ] Confidence Intervals
  - [ ] via Chebyshev
  - [ ] via Hoeffding
  - [ ] via Central Limit Theorem (asymptotic)
- [ ] Acceptance-Rejection-Method
- [ ] Examples
  - [ ] Direct simulation of Genz test functions
  - [ ] Cramér-Lundberg-Process for the simulation of ruin problems
  - [ ] Black-Scholes-Model for option pricing
  - [ ] Spherical Process for solving the Dirichlet problem
  - [ ] Neutron transport through walls of finite thickness
- [ ] Variance Reduction methods
  - [ ] Antithetic Sampling
  - [ ] Control Variates
  - [ ] Stratified Sampling

## References

The implemented methods are based on the following reference book:

> Thomas Müller-Gronbach, Erich Novak, Klaus Ritter:
  Monte Carlo-Algorithmen. Springer-Lehrbuch, Springer 2012, ISBN 978-3-540-89140-6, doi: [10.1007/978-3-540-89141-3](https://doi.org/10.1007/978-3-540-89141-3)
