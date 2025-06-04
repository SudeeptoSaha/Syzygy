class EconomicModel:
    def __init__(self, environment):
        self.env = environment

    def calibrate(self):
        pass

    def simulate(self):
        raise NotImplementedError

    def get_outputs(self):
        return {}
