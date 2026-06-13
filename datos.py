import csv

def cargar_paises():
    try:
        with open("paises.csv", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            lista=[]

            for e in  lector:
                e["poblacion"] = int(e["poblacion"])
                e["superficie"] = int(e["superficie"])
                lista.append(e)
            return lista
    except FileNotFoundError:
        print("Error: no se encontró el archivo paises.csv")
        return []
    except ValueError:
        print("Error: el archivo tiene datos con formato incorrecto")
        return []
    
def guardar_paises(lista):

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
        lector = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])

        lector.writeheader()
        for pais in lista:

            lector.writerow(pais)

