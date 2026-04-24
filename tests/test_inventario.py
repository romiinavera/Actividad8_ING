# tests/test_inventario.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inventario import (  # noqa: E402
    agregar_ingrediente,
    eliminar_ingrediente,
    buscar_ingrediente,
    listar_por_categoria_calorica,
    actualizar_ingrediente
)


def setup_inventario():
    """Crea un inventario de prueba."""
    return [
        {"id": 1, "nombre": "Pollo", "calorias": 165,
         "proteinas": 31, "carbohidratos": 0, "grasas": 3},
        {"id": 2, "nombre": "Arroz", "calorias": 130,
         "proteinas": 2, "carbohidratos": 28, "grasas": 0},
        {"id": 3, "nombre": "Huevo", "calorias": 155,
         "proteinas": 13, "carbohidratos": 1, "grasas": 11}
    ]


# TEST 1: Agregar ingrediente nuevo
def test_agregar_ingrediente_nuevo():
    inv = setup_inventario()
    resultado = agregar_ingrediente(inv, "Atun", 116, 26, 0, 1)
    assert resultado["nombre"] == "Atun"
    assert len(inv) == 4


# TEST 2: Agregar ingrediente duplicado lanza error
def test_agregar_ingrediente_duplicado():
    inv = setup_inventario()
    try:
        agregar_ingrediente(inv, "Pollo", 165, 31, 0, 3)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 3: Agregar ingrediente con nombre vacío lanza error
def test_agregar_nombre_vacio():
    inv = setup_inventario()
    try:
        agregar_ingrediente(inv, "", 100, 10, 20, 5)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 4: Eliminar ingrediente existente
def test_eliminar_ingrediente_existente():
    inv = setup_inventario()
    resultado = eliminar_ingrediente(inv, "Arroz")
    assert resultado is True
    assert len(inv) == 2


# TEST 5: Eliminar ingrediente inexistente lanza error
def test_eliminar_ingrediente_inexistente():
    inv = setup_inventario()
    try:
        eliminar_ingrediente(inv, "Banana")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 6: Buscar ingrediente existente
def test_buscar_ingrediente_existente():
    inv = setup_inventario()
    resultado = buscar_ingrediente(inv, "Huevo")
    assert resultado is not None
    assert resultado["calorias"] == 155


# TEST 7: Buscar ingrediente inexistente devuelve None
def test_buscar_ingrediente_inexistente():
    inv = setup_inventario()
    resultado = buscar_ingrediente(inv, "Manzana")
    assert resultado is None


# TEST 8: Listar por categoría calórica
def test_listar_por_categoria_calorica():
    inv = setup_inventario()
    resultado = listar_por_categoria_calorica(inv, 140)
    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "Arroz"


# TEST 9: Límite calórico negativo lanza error
def test_limite_calorico_negativo():
    inv = setup_inventario()
    try:
        listar_por_categoria_calorica(inv, -10)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 10: Actualizar ingrediente existente
def test_actualizar_ingrediente():
    inv = setup_inventario()
    resultado = actualizar_ingrediente(inv, "Pollo", {"calorias": 180})
    assert resultado["calorias"] == 180
