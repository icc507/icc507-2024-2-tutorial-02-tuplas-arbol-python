#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)

def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return s

t = input().split()

t.reverse()
solved = tuple(t)
solved = list(map(convert_to_int, solved))
print(solved)
