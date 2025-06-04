from syzygy import Environment, SimpleDSGE
import matplotlib.pyplot as plt

env = Environment(T=50)
model = SimpleDSGE(env)

model.calibrate()
model.simulate()
results = model.get_outputs()

plt.plot(results["Output"], label="Output")
plt.plot(results["Capital"], label="Capital")
plt.title("Simple DSGE Simulation")
plt.legend()
plt.show()
