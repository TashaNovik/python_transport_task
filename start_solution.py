import numpy as np

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

# Начальное решение методом наименьшей стоимости
solution = np.zeros((n_warehouses, n_stores))

supply_copy = supply.copy()
demand_copy = demand.copy()

while np.sum(supply_copy) > 0 and np.sum(demand_copy) > 0:
    min_cost = np.inf
    min_index = None

    for i in range(n_warehouses):
        for j in range(n_stores):
            if costs[i, j] < min_cost and supply_copy[i] > 0 and demand_copy[j] > 0:
                min_cost = costs[i, j]
                min_index = (i, j)

    if min_index is None:
        break # Если не найдено допустимое решение, выходим из цикла

    i, j = min_index
    amount = min(supply_copy[i], demand_copy[j])
    solution[i, j] = amount
    supply_copy[i] -= amount
    demand_copy[j] -= amount


# Вычисление общей стоимости перевозок
total_cost = np.sum(solution * costs)

print("Матрица перевозок (xij):")
print(solution)
print("\nМинимальная стоимость перевозок:", total_cost)




# Проверка ограничений (для отладки):
print("\nПроверка:")
print("Сумма по строкам (запасы):", np.sum(solution, axis=1))
print("Сумма по столбцам (потребности):", np.sum(solution, axis=0))