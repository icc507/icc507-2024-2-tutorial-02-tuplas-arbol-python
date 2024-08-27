#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
t = list(map(int, input().split() ) )

# numero, izquierda, centro, derecha
def arbolTernario(numero):
    return [numero, [], [] , [] ]

def insertar(numero, arbol):
    if arbol==[]:
        arbol += arbolTernario(numero)
    elif numero < arbol[0]:
        insertar(numero, arbol[1])
    elif numero == arbol[0]:
        insertar(numero, arbol[2])
    else:
        insertar(numero, arbol[3])

    return arbol

tree = []
for i in t:
    insertar(i, tree)
print(tree)
