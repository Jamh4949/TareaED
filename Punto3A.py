#Punto3A:
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0  # masa
k = 1.0  # constante del resorte
kc = 0.5  # constante del resorte acoplado

omega1 = np.sqrt(k / m)
omegac = np.sqrt(kc / m)

# Definir el sistema de ecuaciones diferenciales
def sistema(t, y):
    x1, v1, x2, v2 = y
    dx1 = v1
    dv1 = -omega1**2 * x1 - omegac**2 * (x1 - x2)
    dx2 = v2
    dv2 = -omega1**2 * x2 - omegac**2 * (x2 - x1)
    return [dx1, dv1, dx2, dv2]

# Condiciones iniciales
x10, v10 = 1.0, 0.0  # Bloque 1
x20, v20 = -1.0, 0.0  # Bloque 2
condiciones_iniciales = [x10, v10, x20, v20]

# Intervalo de tiempo para la simulación
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Resolver el sistema
sol = solve_ivp(sistema, t_span, condiciones_iniciales, t_eval=t_eval)

# Graficar las soluciones
plt.plot(sol.t, sol.y[0], label="x1 (Bloque 1)")
plt.plot(sol.t, sol.y[2], label="x2 (Bloque 2)")
plt.xlabel("Tiempo")
plt.ylabel("Desplazamiento")
plt.legend()
plt.title("Movimiento de los bloques acoplados")
plt.grid()
plt.show()