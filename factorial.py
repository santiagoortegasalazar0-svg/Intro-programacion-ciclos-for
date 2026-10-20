"""
calcular el factorial de un numero

fact(n): 1 x 2 x 3 x 4... x n; 0! = 1

ejemplo: 5! = 1 x 2 x 3 x 4 x 5 = 120
"""
n= int(input("ingrese el valor de n:"))
if n == 0:
    print(1)
elif n > 0:
    fact = 1
    for valor in range(1, n+1):
        fact = fact * valor
    print(n, "!=", fact)
else:
    print("error. n debe ser mayor o igual que 0")