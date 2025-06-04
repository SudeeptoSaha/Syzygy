import numpy as np
from syzygy.core.model_interface import EconomicModel

class SimpleDSGE(EconomicModel):
    def __init__(self, environment):
        super().__init__(environment)
        self.K = []
        self.Y = []

    def calibrate(self):
        self.alpha = self.env.params["alpha"]
        self.beta = self.env.params["beta"]
        self.delta = self.env.params["delta"]
        self.shocks = self.env.shocks["productivity"]

    def simulate(self):
        T = self.env.T
        K = np.zeros(T)
        Y = np.zeros(T)

        K[0] = 1.0  # initial capital

        for t in range(1, T):
            A = np.exp(self.shocks[t])
            Y[t] = A * K[t-1]**self.alpha
            K[t] = self.beta * (1 - self.delta) * K[t-1] + Y[t] * self.alpha

        self.K = K
        self.Y = Y

    def get_outputs(self):
        return {
            "Capital": self.K,
            "Output": self.Y
        }
