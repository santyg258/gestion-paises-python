def pais_mayor_poblacion(paises):
    return max(paises, key=lambda e: e["poblacion"])

def pais_menor_poblacion(paises):
    return min(paises, key=lambda e: e["poblacion"])

def promedio_poblacion(paises):
    return sum(e['poblacion'] for e in paises) / len(paises)

def promedio_superficie(paises):
    return sum(e['superficie'] for e in paises) / len(paises)

def cantidad_por_continente(paises):
    conteo = {}

    for e in paises:
        if e["continente"] in conteo:
            conteo[e["continente"]] = conteo[e["continente"]] + 1
        else:
            conteo[e['continente']] = 1
    return conteo
