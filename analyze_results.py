import matplotlib.pyplot as plt
import numpy as np

# Simulated flow rates
flow = np.linspace(0.001, 0.005, 50)

# HydroPower equation: P = ρ*g*Q*H*η
hydro_power = 1000 * 9.81 * flow * 10 * 0.6

solar_power = 1000  # W constant
uv_load = 200       # W load
net_power = solar_power + hydro_power - uv_load

# Plot results
plt.plot(flow, net_power, label="Net Power (W)", color="blue")
plt.xlabel("Flow Rate (m³/s)")
plt.ylabel("Power (W)")
plt.title("Hybrid Greywater Solar–Hydro System Simulation")
plt.legend()
plt.grid(True)
plt.show()
