import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculo_macros import (
    calcular_tdee,
    calcular_calorias_quemadas,
    calcular_macros_objetivo,
    sumar_macros_del_dia,
    validar_ingrediente
)


# TEST 1: TDEE correcto para hombre
def test_tdee_hombre_moderado():
    resultado = calcular_tdee(25, "M", 70, 175, "moderado", "mantener")
    assert resultado > 0


# TEST 2: TDEE correcto para mujer
def test_tdee_mujer_ligero():
    resultado = calcular_tdee(30, "F", 60, 165, "ligero", "bajar")
    assert resultado > 0


# TEST 3: Sexo inválido lanza error
def test_tdee_sexo_invalido():
    try:
        calcular_tdee(25, "X", 70, 175, "moderado", "mantener")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 4: Peso negativo lanza error
def test_tdee_peso_negativo():
    try:
        calcular_tdee(25, "M", -70, 175, "moderado", "mantener")
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass


# TEST 5: Calorías quemadas cardio 30 minutos
def test_calorias_quemadas_cardio():
    resultado = calcular_calorias_quemadas("cardio", 30)
    assert resultado == 210


# TEST 6: Calorías quemadas HIIT 45 minutos
def test_calorias_quemadas_hiit():
    resultado = calcular_calorias_quemadas("hiit", 45)
    assert resultado == 405


# TEST 7: Ejercicio desconocido devuelve 0
def test_calorias_ejercicio_desconocido():
    resultado = calcular_calorias_quemadas("baile", 30)
    assert resultado == 0


# TEST 8: Suma de macros del día
def test_sumar_macros_del_dia():
    registros = [
        {"calorias": 300, "proteinas": 20, "carbohidratos": 40, "grasas": 8},
        {"calorias": 500, "proteinas": 35, "carbohidratos": 60, "grasas": 12},
    ]
    resultado = sumar_macros_del_dia(registros)
    assert resultado["calorias"] == 800
    assert resultado["proteinas"] == 55


# TEST 9: Validar ingrediente correcto
def test_validar_ingrediente_correcto():
    resultado = validar_ingrediente("Pollo", 165, 31, 0, 3.6)
    assert resultado is True


# TEST 10: Ingrediente con nombre vacío lanza error
def test_validar_ingrediente_nombre_vacio():
    try:
        validar_ingrediente("", 165, 31, 0, 3.6)
        assert False, "Debería haber lanzado ValueError"
    except ValueError:
        pass
