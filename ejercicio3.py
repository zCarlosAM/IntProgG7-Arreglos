# Matriz de ventas por tienda (filas) y por mes (columnas)
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

# Mostrar la matriz original (solo los datos numéricos)
print("Matriz original:")
for fila in ventas:
    print(fila)

# Inicializar lista vacía para el arreglo linealizado por columnas
linealizado_columnas = []

# Obtener número de filas y columnas
num_filas = len(ventas)
num_columnas = len(ventas[0])

# Recorrer las columnas primero, luego las filas
for col in range(num_columnas):
    for fila in range(num_filas):
        # Agregar el elemento a la lista en orden por columnas
        linealizado_columnas.append(ventas[fila][col])

# Mostrar el arreglo linealizado
print("\nArreglo linealizado por columnas:")
print(linealizado_columnas)
