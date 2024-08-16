A = int(input("Ingrese el valor de A:"))
B = int(input("Ingrese el valor de B:"))
C = int(input("Ingrese el valor de C:"))

area_triangulo = (B*(C-A))/2
area_rectangulo = B*C
area_total = area_triangulo + area_rectangulo

print("El área del del terreno es:", area_total)