from datos import cargar_paises, guardar_paises
from busquedas import busqueda_pais
from validaciones import validar_entero, validar_texto
from estadistica import pais_mayor_poblacion, pais_menor_poblacion, promedio_poblacion, promedio_superficie, cantidad_por_continente
from filtros import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
import os

paises = cargar_paises()

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("-"*25)
    print("----------Menu-----------")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar pais")
    print("5. Ordenar pais")
    print("6. Ver estadisticas")
    print("0. salir")
    print("-"*25)

    op = validar_entero("ingrese su opcion: ")
    return op

def menu_filtro():
    os.system("cls" if os.name == "nt" else "clear")
    print("-"*25)
    print("--------filtros---------")
    print("1. Continente.")
    print("2. Rango de poblacion.")
    print("3. Rango de superficie.")
    print("4. Volver.")
    print("-"*25)

    op = validar_entero("ingrese su opcion: ")
    return op

def menu_ordenar():
    os.system("cls" if os.name == "nt" else "clear")
    print("-"*25)
    print("--------ordenar---------")
    print("1. Nombre.")
    print("2. Poblacion.")
    print("3. Superficie.")
    print("4. Volver.")
    print("-"*25)

    op = validar_entero("ingrese su opcion: ")
    forma = validar_texto("ascendente o descendente: ")
    return op,forma

def filtro(opcion):
    os.system("cls" if os.name == "nt" else "clear")
    if opcion == 1:
        continente= validar_texto("ingrese el continente: ")
        resultado=filtrar_por_continente(paises, continente)
        for e in resultado:
            print(e)
    
    
    elif opcion ==2:
        print("cargar el rango a evaluar.")
        min_val=validar_entero("minimo:  ")
        max_val=validar_entero("maximo: ")
        resultado=filtrar_por_poblacion(paises, min_val, max_val)
        for e in resultado:
            print(e)

    elif opcion==3:
        print("cargar el rango a evaluar.")
        min_val=validar_entero("minimo:  ")
        max_val=validar_entero("maximo: ")
        resultado=filtrar_por_superficie(paises, min_val, max_val)
        for e in resultado:
            print(e)

    elif opcion == 4:
        menu()

    else:
        print("opcion invalida.")
    input("precione enter para continuar.")

def ordenar(op, ascendente):
    os.system("cls" if os.name == "nt" else "clear")
    if op == 1:
        por_nombre = ordenar_por_nombre(paises,ascendente)
        for e in por_nombre:
            print(e)
    elif op ==2:
        por_poblacion = ordenar_por_poblacion(paises,ascendente)
        for e in por_poblacion:
            print(e)
    elif op==3:
        por_superficie = ordenar_por_superficie(paises,ascendente)
        for e in por_superficie:
            print(e)
    elif op == 4:
        menu()

    else:
        print("opcion invalida.")    


def main():

    opcion = menu()
    while opcion != 0:

        if opcion == 1:
            nombre =validar_texto("ingrese el nombre del pais: ")
            poblacion =validar_entero("ingrese la cantidad de poblacion: ")
            superficie =validar_entero("ingrese la superficie del pais: ")
            print("Continentes disponibles: América, Europa, Asia, África, Oceanía")
            continente = validar_texto("ingrese el continente: ")
            agregar={
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            }
            paises.append(agregar)
            guardar_paises(paises)
            print("\npais guardado con exito \n")

        elif opcion == 2:
            nombre = validar_texto("ingrese el nombre del pais a actualizar: ")
            resultado =busqueda_pais(paises,nombre)
            if len(resultado) == 1:
                poblacion =validar_entero("ingrese la cantidad de poblacion: ")
                superficie =validar_entero("ingrese la superficie del pais: ")

                resultado[0]["poblacion"] = poblacion
                resultado[0]["superficie"] = superficie
                guardar_paises(paises)     
            elif len(resultado) == 0:
                print("país no encontrado")
            else:
                print("hay más de una coincidencia, sea más específico")
        elif opcion == 3:
            buscar = validar_texto("ingrese el pais: ")
            nom_pais = busqueda_pais(paises, buscar)
            for e in nom_pais:
                print(e)
            input("precione enter para continuar.")

        elif opcion == 4:
            op_filtro = menu_filtro()
            filtro(op_filtro)

        elif opcion == 5:
            op_orden, forma = menu_ordenar()
            ascendente = forma.lower() == "ascendente"
            ordenar(op_orden, ascendente)
            input("precione enter para continuar.")
            
        elif opcion == 6:
            print(f"el pais con mayor poblacion es: {pais_mayor_poblacion(paises)}")
            print(f"el pais con menor poblacion es: {pais_menor_poblacion(paises)}")
            print(f"El promedio de poblacion es: {round(promedio_poblacion(paises), 2)}")
            print(f"El promeedio de superficie es: {round(promedio_superficie(paises),2)}")
            conteo = cantidad_por_continente(paises)
            for continente, cantidad in conteo.items():
                print(f"{continente}: {cantidad}")
        input("precione enter para continuar. ")

        opcion = menu()
    print("que tenga buen dia. ")


main()