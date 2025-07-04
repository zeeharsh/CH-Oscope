import gaspype as gp
import numpy as np
import matplotlib.pyplot as plt

# Define allowed gases
system = gp.fluid_system("CH4, CO, CO2, H2, O2")

# Define CH₂O as the fuel (1C, 2H, 1O)
fuel = gp.elements({'C': 1, 'H': 2, 'O': 1}, system)

# Temperature range in Kelvin
temps = np.linspace(1000, 2500, 10)

# Run the equilibrium calculation
results = [gp.equilibrium(fuel, t=T) for T in temps]

# Extract mole fractions for each gas
fractions = {gas: [r[gas] for r in results] for gas in system.species}

# Create a smaller graph
plt.figure(figsize=(7, 4))  # 📏 Smaller size

# Plot gas amounts
for gas, values in fractions.items():
    plt.plot(temps, values, label=gas, linewidth=1.8)

# Labels
plt.title("Gas Breakdown from Heating CH₂O", fontsize=11)
plt.xlabel("Temperature (K)", fontsize=10)
plt.ylabel("Mole Fraction", fontsize=10)
plt.legend(fontsize=8)
plt.grid(True, linestyle="--", alpha=0.5)

#-Add compact summary box
summary = (
    "Summary:\n"
    "CH₂O breaks down as it heats up.\n"
    "H₂ and CO rise, CH₄ fades.\n"
    "Used in engines, combustion, rockets."
)

plt.gcf().text(0.6, 0.25, summary,
               fontsize=8,
               bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

plt.tight_layout()
plt.show()
