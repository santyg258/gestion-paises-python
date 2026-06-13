
def busqueda_pais(paises, nom_pais):

    coincidencia = []

    for e in paises:
        if  nom_pais.lower() in e['nombre'].lower():
            coincidencia.append(e)
    if not coincidencia:
        print("no se encontraron coincidencias.")
    return coincidencia