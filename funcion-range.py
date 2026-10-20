"""
sitaxis de la funcion range

range([inicio], fin, [paso])

-EL INICIO ES 0 POR DEFECTO, SI NO SE INDICA

- EL PASO ES 1 POR DEFECTO, SI NO SE INDICA

- LA FUNCION RANGE() GENERA UNA SERI DE NUMERS ENTEROS ENTRE EL INICIO Y FIN -1, CON INCREMENTO DADO POR EL PASO.


"""
#CASO 1: range(fin)

print(list(range(10))) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#caso2: range(inicio, fin)
print(list(range(3, 10))) #3, 4, 5, 6, 7, 8, 9

#caso3: range(inicio, fin, paso)

print(list(range(3, 20, 2))) #3, 5, 7, 9, 11, 13, 15, 17, 19
print(list(range(21, 0, -2)))