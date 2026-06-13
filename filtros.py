import unicodedata

def normalizar(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8").lower()

def filtrar_por_continente(paises, continente):
    pais_continente = []

    for e in paises:

        if normalizar(continente) in normalizar(e["continente"]):
            pais_continente.append(e)

    if not pais_continente:
        print("no se encontro continente")

    return pais_continente



def filtrar_por_poblacion(paises, min_pob, max_pob):
    pais_poblacion = []

    for e in paises:

        if min_pob <= e['poblacion'] <= max_pob:
            pais_poblacion.append(e)

    if not pais_poblacion:
        print("no se econtro pais con ese rango de poblacion")

    return pais_poblacion



def filtrar_por_superficie(paises, min_sup, max_sup):
    pais_superficie= []

    for e in paises:

        if min_sup <= e['superficie'] <= max_sup:
            pais_superficie.append(e)

    if not pais_superficie:
        print("no se econtro pais con ese rango de superficie")

    return pais_superficie
