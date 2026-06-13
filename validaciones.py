
def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError: print("Error: ingrese un numero valido")


def validar_texto(mensaje):
    while True:
        valor = input(mensaje)
        if valor == "":
            print("Error: el campo no puede estar vacío")
        else:
            return valor