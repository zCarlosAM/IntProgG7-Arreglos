# Datos de ventas: cada fila representa una tienda y cada columna un mes
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

nombres_tiendas = ["ABSA 1", "ABSA 2", "ABSA 3", "ABSA 4"]

# a. Venta total por todas las tiendas
total_general = sum(sum(tienda) for tienda in ventas)
print(f"Venta total por todas las tiendas: ${total_general:,.0f}")

# b. Venta total por tienda
ventas_por_tienda = [sum(tienda) for tienda in ventas]
print("\nVenta total por tienda:")
for i, total in enumerate(ventas_por_tienda):
    print(f"{nombres_tiendas[i]}: ${total:,.0f}")

# c. Tienda que más vendió en los 6 meses
indice_max = ventas_por_tienda.index(max(ventas_por_tienda))
print(f"\nTienda que más vendió en los 6 meses: {nombres_tiendas[indice_max]} con ${ventas_por_tienda[indice_max]:,.0f}")

# d. Tienda que menos vendió
indice_min = ventas_por_tienda.index(min(ventas_por_tienda))
print(f"Tienda que menos vendió en los 6 meses: {nombres_tiendas[indice_min]} con ${ventas_por_tienda[indice_min]:,.0f}")
