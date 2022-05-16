'5.4 Desarrolle una función en python que acepte una variable string como primer parámetro y la cantidad de caracteres como segundo parámetro.'
'La función debe retornar un nuevo string que consista en el string original y el número correcto de caracteres necesarios para que el string se salga centrado.'
'No agregue caracteres al final del string. (10pts)'

mensaje = "Hola Mundo, Ing. Telemática"
longitud = 40

def variable(mensaje, longitud):
    numeroNecesario = len(mensaje.center(longitud)) + len(mensaje)
    textoNuevo = mensaje + " " + str(numeroNecesario)
    print("A continuación visualizaremos el texto centrado")
    print("|",mensaje.center(numeroNecesario),"|")
    return textoNuevo

respuesta = variable(mensaje, longitud)

print("Respuesta:", respuesta)