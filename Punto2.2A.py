# Punto 2.2A:
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definimos los parámetros físicos
g = 9.81  # m/s^2 (gravedad)
m = 1.0   # kg (masa)
gamma_values = [0.1, 0.5, 1.0]  # Valores de fricción (gamma)
l_fixed = 1.0  # Longitud fija del péndulo

# Ecuación diferencial
def pendulum(t, y, gamma, l):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Condiciones iniciales
theta0 = np.pi / 5  # Ángulo inicial (en radianes)
omega0 = 0.0        # Velocidad angular inicial
y0 = [theta0, omega0]

# Resolviendo y graficando para gamma variable, l fijo
plt.figure()
for gamma in gamma_values:
    # Resolver la ecuación diferencial para cada valor de gamma
    sol = solve_ivp(pendulum, [0, 10], y0, args=(gamma, l_fixed), t_eval=np.linspace(0, 10, 1000))
    plt.plot(sol.t, sol.y[0], label=f"γ={gamma}")

# Personalización del gráfico
plt.title(f"Soluciones para l={l_fixed} variando γ")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo θ (rad)")
plt.legend()
plt.grid()
plt.show()