'Defina una función en python que acepte 3 valores y devuelva solo el maximo de los tres. (7pts)'

n1 = int(input("Introduzca el primer número: "))
n2 = int(input("Introduzca el segundo número: "))
n3 = int(input("Introduzca el tercer número: "))

def mayorNumero(n1,n2,n3):
    mayor = n1
    if (n1 > n2 and n1 > n2): 
        return n1
    elif (n2 > n1 and n2 > n1):
       return n2
    elif (n3 > n1 and n3 > n2):
       return n3
    else:
        return mayor

numeroMayor = mayorNumero(n1,n2,n3)

print("El número mayor es:", numeroMayor)