aguaMC = float(input('Introduce el valor en metros cubicos de agua consuimido: '))
tarifa = float(input('Introduce el valor de la tarifa por cada metros cubicos de agua consuimido: '))
pago = aguaMC * tarifa
print('El valor del pago por', round(aguaMC, 2),'metros cubicas es de $', int(pago), 'pesos.')