import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.registro_comidas import (  # noqa: E402
    registrar_comida,
    obtener_comidas_por_momento,
    calcular_total_calorias,
    eliminar_ultima_comida,
    comida_mas_calorica
)


def setup_historial():
    """Crea un historial de prueba."""
    return [
        {"nombre": "Avena", "calorias": 300, "proteinas": 10,
         "carbohidratos": 54, "grasas": 5, "momento": "desayuno"},
        {"nombre": "Pollo con arroz", "calorias": 550, "proteinas": 40,
         "carbohidratos": 60, "grasas": 8, "momento": "almuerzo"},
        {"nombre": "Yogur", "calorias": 150, "proteinas": 8,
         "carbohidratos": 20, "grasas": 3, "momento": "merienda"}
    ]


# TEST 1: Registrar comida correctamente
def test_registrar_comida_correcta():
    historial = setup_historial()
    resultado = registrar_comida(historial, "Ensalada", 200, 5, 15, 10, "cena")
    assert resultado["nombre"] == "Ensalada"
    assert len(historial) == 4


# TEST 2: Nombre vacío lanza error
def test_registrar_nombre_vacio():
    historial = setup_historial()
    try:
        registrar_comida(historial, "", 200, 5, 15, 10, "cena")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 3: Momento inválido lanza error
def test_registrar_momento_invalido():
    historial = setup_historial()
    try:
        registrar_comida(historial, "Ensalada", 200, 5, 15, 10, "mañana")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 4: Calorías negativas lanza error
def test_registrar_calorias_negativas():
    historial = setup_historial()
    try:
        registrar_comida(historial, "Ensalada", -200, 5, 15, 10, "cena")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 5: Obtener comidas por momento
def test_obtener_comidas_por_momento():
    historial = setup_historial()
    resultado = obtener_comidas_por_momento(historial, "desayuno")
    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "Avena"


# TEST 6: Momento inválido en obtener lanza error
def test_obtener_momento_invalido():
    historial = setup_historial()
    try:
        obtener_comidas_por_momento(historial, "medianoche")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 7: Calcular total de calorías
def test_calcular_total_calorias():
    historial = setup_historial()
    resultado = calcular_total_calorias(historial)
    assert resultado == 1000


# TEST 8: Eliminar última comida
def test_eliminar_ultima_comida():
    historial = setup_historial()
    resultado = eliminar_ultima_comida(historial)
    assert resultado["nombre"] == "Yogur"
    assert len(historial) == 2


# TEST 9: Eliminar de historial vacío lanza error
def test_eliminar_historial_vacio():
    historial = []
    try:
        eliminar_ultima_comida(historial)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 10: Comida más calórica
def test_comida_mas_calorica():
    historial = setup_historial()
    resultado = comida_mas_calorica(historial)
    assert resultado["nombre"] == "Pollo con arroz"
