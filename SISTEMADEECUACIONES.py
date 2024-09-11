import numpy as np

# Definir la matriz A y el vector b
A = np.array([[52, 30, 18], 
              [20, 50, 30], 
              [25, 20, 55]])

b = np.array([4800, 5810, 5690])

# Resolver el sistema de ecuaciones A * x = b
x = np.linalg.solve(A, b)

# Mostrar los resultados de manera más elegante
print("Solución del sistema x:")
print(f"Cantera 1 (x1): {x[0]:.2f} metros cúbicos")
print(f"Cantera 2 (x2): {x[1]:.2f} metros cúbicos")
print(f"Cantera 3 (x3): {x[2]:.2f} metros cúbicos")
