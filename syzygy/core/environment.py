import numpy as np

class Environment:
    def __init__(self, T=100, seed=42, params=None, shocks=None):
        """
        Environment for macroeconomic simulation.

        Parameters:
        - T (int): Number of time periods.
        - seed (int): Random seed for reproducibility.
        - params (dict): Custom model parameters.
        - shocks (dict): Custom shocks (e.g. productivity shocks).
        """
        np.random.seed(seed)
        self.T = T

        # Default parameters
        default_params = {
            "beta": 0.96,
            "alpha": 0.33,
            "delta": 0.08,
            "rho": 0.9,
            "sigma": 0.02,
        }

        # Use custom or default parameters
        self.params = default_params.copy()
        if params:
            self.params.update(params)

        # Use custom shocks or generate default
        if shocks:
            self.shocks = shocks
        else:
            self.shocks = self.generate_shocks()

    def generate_shocks(self):
        """
        Generate default shocks for the simulation.
        Currently includes only a productivity shock.
        """
        shocks = {
            "productivity": np.random.normal(0, self.params["sigma"], self.T)
        }
        return shocks
