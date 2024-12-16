import numpy as np
from scipy.optimize import linprog

# Стоимости перевозок (Cij)
costs = np.array([[4, 3, 5, 6],
                 [8, 2, 4, 7]])

# Запасы на складах
supply = np.array([100, 200])

# Потребности магазинов
demand = np.array([50, 100, 75, 75])

# Размерность задачи
n_warehouses = len(supply)
n_stores = len(demand)

# Преобразование задачи в стандартную форму для linprog
c = costs.flatten()
A_eq = []
b_eq = []

for i in range(n_warehouses):
    row = np.zeros((n_warehouses, n_stores)).flatten()
    row[i * n_stores : (i + 1) * n_stores] = 1
    A_eq.append(row)
    b_eq.append(supply[i])

for j in range(n_stores):
    row = np.zeros((n_warehouses, n_stores)).flatten()
    for i in range(n_warehouses):
        row[i*n_stores + j] = 1
    A_eq.append(row)
    b_eq.append(demand[j])


A_eq = np.array(A_eq)
b_eq = np.array(b_eq)


# Решение с помощью linprog
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None))

# Преобразование результата обратно в матрицу
optimal_solution = result.x.reshape((n_warehouses, n_stores))
optimal_cost = result.fun

print("\nОптимальное решение (с помощью linprog):")
print(optimal_solution)
print("\nМинимальная стоимость (оптимальная):", optimal_cost)