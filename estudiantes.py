import os

nombres = ["", "", "", "", ""]
calificaciones = [  [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
promedios = [0, 0, 0, 0, 0]

os.system("cls || clear")
for i in range(len(nombres)):
    nombres[i] = input(f"Ingrese el nombre del estudiante {i+1}: ")

    print("-"*64)

    for j in range(len(calificaciones[i])):
        calificaciones[i][j] = int(input(f"Ingrese la calificación número {j+1}: "))
    print()

os.system("cls || clear")

for i in range(len(nombres)):
    for j in calificaciones[i]:
        promedios[i] += j

    promedios[i] /= len(calificaciones[i])


print("Promedios finales")
print("-"*64)
for i in range(len(nombres)):
    print(f"{nombres[i]}: {round(promedios[i])}")
