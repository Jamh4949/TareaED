#Punto3B:
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parámetros modificados
m = 0.8  # masa (ajustada)
k = 2.0  # constante del resorte (ajustada)
kc = 1.5  # constante del resorte acoplado (ajustada)

omega1 = np.sqrt(k / m)
omegac = np.sqrt(kc / m)

# Sistema de ecuaciones diferenciales
def sistema(t, y):
    x1, v1, x2, v2 = y
    dx1 = v1
    dv1 = -omega1**2 * x1 - omegac**2 * (x1 - x2)
    dx2 = v2
    dv2 = -omega1**2 * x2 - omegac**2 * (x2 - x1)
    return [dx1, dv1, dx2, dv2]

# Nuevas condiciones iniciales
x10, v10 = 1.0, 0.3  # Bloque 1
x20, v20 = 0.5, -0.1  # Bloque 2
cond_iniciales = [x10, v10, x20, v20]

# Intervalo de tiempo
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Resolver el sistema
sol = solve_ivp(sistema, t_span, cond_iniciales, t_eval=t_eval)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label="x1 (Bloque 1)")
plt.plot(sol.t, sol.y[2], label="x2 (Bloque 2)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento (m)")
plt.title("Movimiento de los bloques acoplados (Parámetros ajustados)")
plt.legend()
plt.grid()
plt.show()