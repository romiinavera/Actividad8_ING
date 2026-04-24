# src/inventario.py
# NutriStock - Módulo de gestión de inventario


def agregar_ingrediente(inventario, nombre, calorias, proteinas, carbohidratos, grasas):
    """Agrega un nuevo ingrediente al inventario."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    if any(v < 0 for v in [calorias, proteinas, carbohidratos, grasas]):
        raise ValueError("Los valores nutricionales no pueden ser negativos")

    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            raise ValueError("El ingrediente ya existe en el inventario")

    ingrediente = {
        "id": len(inventario) + 1,
        "nombre": nombre.strip(),
        "calorias": calorias,
        "proteinas": proteinas,
        "carbohidratos": carbohidratos,
        "grasas": grasas
    }
    inventario.append(ingrediente)
    return ingrediente


def eliminar_ingrediente(inventario, nombre):
    """Elimina un ingrediente del inventario por nombre."""
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            inventario.remove(item)
            return True
    raise ValueError("El ingrediente no existe en el inventario")


def buscar_ingrediente(inventario, nombre):
    """Busca un ingrediente por nombre."""
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            return item
    return None


def listar_por_categoria_calorica(inventario, limite_calorias):
    """Lista ingredientes que están por debajo del límite calórico."""
    if limite_calorias < 0:
        raise ValueError("El límite de calorías no puede ser negativo")
    return [i for i in inventario if i["calorias"] <= limite_calorias]


def actualizar_ingrediente(inventario, nombre, nuevos_datos):
    """Actualiza los datos de un ingrediente existente."""
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            item.update(nuevos_datos)
            return item
    raise ValueError("El ingrediente no existe en el inventario")
