#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input().split()
m = input().split()
def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return s

solved = tuple(m + t + m)
solved = list(map(convert_to_int, solved))
print(solved)
