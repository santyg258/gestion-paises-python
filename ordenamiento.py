def ordenar_por_nombre(paises, ascendente):

    return sorted(paises, key=lambda e: e["nombre"], reverse= not ascendente)

def ordenar_por_poblacion(paises, ascendente):

    return sorted(paises, key=lambda e: e["poblacion"], reverse= not ascendente)

def ordenar_por_superficie(paises, ascendente):
    
    return sorted(paises, key=lambda e: e["superficie"], reverse= not ascendente)