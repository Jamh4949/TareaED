#Punto2.2B:
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parámetros físicos
g = 9.81
m = 1.0
gamma = 0.5
l = 1.0
n_values = [5, 6, 7]

# Ecuación no lineal, es decir la ec: (P)
def pendulum_nonlinear(t, y, gamma, l):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Solución analítica de (L)
def pendulum_linear_solution(t, theta0, omega0, gamma, l):
    omega_d = np.sqrt(abs(g / l - (gamma / (2 * m))**2))
    if (gamma / (2 * m))**2 < g / l:  # Subamortiguado
        return np.exp(-gamma * t / (2 * m)) * (theta0 * np.cos(omega_d * t))
    else:
        raise ValueError("Este código solo trata casos subamortiguados")

# Resolución y gráficos
for n in n_values:
    theta0 = np.pi / n
    omega0 = 0.0
    y0 = [theta0, omega0]

    # Resolviendo (P)
    t_eval = np.linspace(0, 10, 1000)
    sol_nonlinear = solve_ivp(pendulum_nonlinear, [0, 10], y0, args=(gamma, l), t_eval=t_eval)

    # Solución analítica de (L)
    sol_linear = pendulum_linear_solution(t_eval, theta0, omega0, gamma, l)

    # Calculando la diferencia
    difference = np.abs(sol_nonlinear.y[0] - sol_linear)

    # Gráfica de la diferencia
    plt.plot(t_eval, difference, label=f'n = {n}')

# Personalización del gráfico
plt.title("Diferencia entre soluciones de (P) y (L)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Diferencia |θ_P - θ_L|")
plt.legend()
plt.grid()
plt.show()