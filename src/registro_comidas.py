def registrar_comida(historial, nombre, calorias, proteinas, carbohidratos, grasas, momento):
    """Registra una comida en el historial del día."""
    momentos_validos = ["desayuno", "almuerzo", "merienda", "cena", "snack"]

    if not nombre or not nombre.strip():
        raise ValueError("El nombre de la comida no puede estar vacío")
    if calorias < 0:
        raise ValueError("Las calorías no pueden ser negativas")
    if momento not in momentos_validos:
        raise ValueError("Momento no válido")

    registro = {
        "nombre": nombre.strip(),
        "calorias": calorias,
        "proteinas": proteinas,
        "carbohidratos": carbohidratos,
        "grasas": grasas,
        "momento": momento
    }
    historial.append(registro)
    return registro


def obtener_comidas_por_momento(historial, momento):
    """Devuelve todas las comidas registradas en un momento del día."""
    momentos_validos = ["desayuno", "almuerzo", "merienda", "cena", "snack"]
    if momento not in momentos_validos:
        raise ValueError("Momento no válido")
    return [c for c in historial if c["momento"] == momento]


def calcular_total_calorias(historial):
    """Calcula el total de calorías del historial."""
    return sum(c["calorias"] for c in historial)


def eliminar_ultima_comida(historial):
    """Elimina el último registro del historial."""
    if not historial:
        raise ValueError("El historial está vacío")
    return historial.pop()


def comida_mas_calorica(historial):
    """Devuelve la comida con más calorías del historial."""
    if not historial:
        raise ValueError("El historial está vacío")
    return max(historial, key=lambda c: c["calorias"])
