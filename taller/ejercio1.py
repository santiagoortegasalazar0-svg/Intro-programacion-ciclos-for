"""
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.
Fórmula o relación: El paso entre términos es 1 si A ≤ B y -1 si A > B.

"""
primer_num = int(input("escriba el primer numero entero entre el -100 y 100: "))

segundo_num= int(input("escriba el segundo numero entero entre -100 y 100: "))

if primer_num <= segundo_num:
    print(list(range(primer_num, segundo_num+1, 1)))
else:
    print(list(range(primer_num, segundo_num-1, -1)))
