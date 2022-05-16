'Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista. (7pts)'

vListaEntero = [10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58 ,61, 64, 67, 70]

def sumaImpares(lista):
    respuesta = 0
    for vIndice in lista:
        if(vIndice % 2 != 0):
            respuesta += vIndice
    return respuesta

respuesta = sumaImpares(vListaEntero)
print("La suma de los valores impares es:", respuesta)
