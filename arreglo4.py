n = int(input("Filas (menor que 10): "))
m = int(input("Columnas (menor que 10): "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(int(input(f"[{i}][{j}]: ")))
    matriz.append(fila)

print("\nSuma por fila:")
for i in range(n):
    print(f"Fila {i}: {sum(matriz[i])}")

print("\nPromedio por columna:")
for j in range(m):
    col = [matriz[i][j] for i in range(n)]
    print(f"Columna {j}: {sum(col)/n:.1f}")

mayor = matriz[0][0]
f, c = 0, 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            f, c = i, j

print(f"\nMayor valor: {mayor} en [{f}][{c}]")
