ventas = []
for i in range(3):
    fila = []
    for j in range(4):
        fila.append(int(input(f"Vendedor {i}, Zona {j}: ")))
    ventas.append(fila)

zonas = [sum(ventas[i][j] for i in range(3)) for j in range(4)]
print(f"\nZona con más ventas: {zonas.index(max(zonas))}")

vend = [sum(ventas[i]) for i in range(3)]
print(f"Vendedor con menos ventas: {vend.index(min(vend))}")

print(f"Total vendido: {sum(vend)}")
