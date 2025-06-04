import numpy as np
from syzygy import Environment, SimpleDSGE

def test_simple_dsge_simulation_runs():
    env = Environment(T=10)
    model = SimpleDSGE(env)
    model.calibrate()
    model.simulate()
    results = model.get_outputs()

    assert len(results["Output"]) == 10
    assert len(results["Capital"]) == 10
    assert np.all(np.isfinite(results["Output"]))
    assert np.all(np.isfinite(results["Capital"]))

def test_custom_parameters():
    custom_params = {
        "beta": 0.99,
        "alpha": 0.25,
        "delta": 0.1,
        "sigma": 0.01,
    }

    env = Environment(T=5, params=custom_params)
    assert env.params["beta"] == 0.99
    assert env.params["alpha"] == 0.25

def test_custom_shocks():
    T = 5
    custom_shocks = {
        "productivity": np.linspace(0, 0.01, T)
    }

    env = Environment(T=T, shocks=custom_shocks)
    model = SimpleDSGE(env)
    model.calibrate()
    model.simulate()
    results = model.get_outputs()

    assert np.allclose(env.shocks["productivity"], custom_shocks["productivity"])
    assert len(results["Output"]) == T
