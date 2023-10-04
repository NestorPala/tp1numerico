import time
from main import \
    solve_discrete_laplace_sor, \
    UPPER, LOWER, LEFT, RIGHT, \
    X_VALUE, X_ERROR_BOUND, RESIDUAL, ITERATIONS, best_w_value

r_tol = 0.001  # tolerancia
N = 32
w = best_w_value(N)

# Contorno de la placa
boundaries = [-1, -1, -1, -1]
boundaries[UPPER] = 80.0  # TN
boundaries[LOWER] = 20.0  # TS
boundaries[LEFT] = 40.0  # TW
boundaries[RIGHT] = 40.0  # TE

start_time = time.perf_counter()

# Si no se especifica "w", por defecto se calcula el mejor valor
# Si no se especifica "seed", por defecto se utiliza x0 = [0,0,...,0]
data = solve_discrete_laplace_sor(N, r_tol, boundaries, w=w)

end_time = time.perf_counter()
elapsed_time = end_time - start_time

T = data[X_VALUE]  # temperaturas en los nodos
DELTA_T = data[X_ERROR_BOUND]  # cotas de error
residual = data[RESIDUAL]  # residuo
iterations = data[ITERATIONS]  # cantidad de iteraciones

print(f"Los valores de temperatura de los nodos son: T =", T, "\n")
print(f"Las cotas de error para T son: ∆T =", DELTA_T, "\n")
print(f"El residuo final es: R =", residual, "\n")
print(f"La cantidad de iteraciones fue: K =", iterations, "\n")

print(20 * "-", "\nElapsed time:", round(elapsed_time, 2), "s")
