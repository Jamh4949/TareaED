#Punto2.2B
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parámetros físicos
g = 9.81  # m/s^2 (gravedad)
gamma = 0.0  # Sin fricción
l_values = [1.0, 2.0, 5.0]  # Diferentes longitudes

# Ecuación diferencial
def pendulum(t, y, gamma, l):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Condiciones iniciales
theta0 = np.pi / 5
omega0 = 0.0
y0 = [theta0, omega0]

# Resolviendo para γ=0 y variando l
plt.figure(figsize=(10, 6))
for l in l_values:
    sol = solve_ivp(pendulum, [0, 10], y0, args=(gamma, l), t_eval=np.linspace(0, 10, 1000))
    plt.plot(sol.t, sol.y[0], label=f"l={l}")

# Gráfica
plt.title("Soluciones para γ=0 variando l")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo θ (rad)")
plt.legend()
plt.grid()
plt.show()