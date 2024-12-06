#Punto 1:
import numpy as np
import matplotlib.pyplot as plt

# Constante de carga 
q = -1

# Coordenadas de las cargas
charges = [(0, 0), (1, 0), (0.5, np.sqrt(3)/2)]

# Definimos el potencial total
def potential(x, y):
    P = 0
    for a, b in charges:
        P += q * np.log((x - a)**2 + (y - b)**2)
    return P

# Gradiente del potencial (derivadas parciales)
def grad_potential(x, y):
    px, py = 0, 0
    for a, b in charges:
        factor = 2 * q / ((x - a)**2 + (y - b)**2)
        px += factor * (x - a)
        py += factor * (y - b)
    return -px, -py  # Campo eléctrico: -gradiente del potencial

# Crear una malla para graficar
x = np.linspace(-1, 2, 400)
y = np.linspace(-1, 2, 400)
X, Y = np.meshgrid(x, y)

# Calcular el potencial y su gradiente
Z = potential(X, Y)
Ex, Ey = grad_potential(X, Y)  # Componentes del campo eléctrico

# Graficar curvas equipotenciales
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour, label="Potencial")
plt.title("Curvas equipotenciales y líneas de corriente")
plt.xlabel("x")
plt.ylabel("y")

# Graficar líneas de corriente
plt.streamplot(X, Y, Ex, Ey, color='red', linewidth=0.8, density=1.2, arrowsize=1)

# Opcional: Graficar las posiciones de las cargas
for a, b in charges:
    plt.plot(a, b, 'ro', markersize=10, label='Carga')

plt.legend(['Cargas'])
plt.grid()
plt.show()