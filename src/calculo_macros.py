def calcular_tdee(edad, sexo, peso, altura, actividad, objetivo):
    """Calcula el gasto calórico diario total (TDEE)."""
    if peso <= 0 or altura <= 0 or edad <= 0:
        raise ValueError("Peso, altura y edad deben ser valores positivos")

    if sexo == "M":
        bmr = 10 * peso + 6.25 * altura - 5 * edad + 5
    elif sexo == "F":
        bmr = 10 * peso + 6.25 * altura - 5 * edad - 161
    else:
        raise ValueError("Sexo debe ser 'M' o 'F'")

    factores = {
        "sedentario": 1.2,
        "ligero": 1.375,
        "moderado": 1.55,
        "activo": 1.725,
        "muy_activo": 1.9
    }

    if actividad not in factores:
        raise ValueError("Nivel de actividad no válido")

    tdee = bmr * factores[actividad]

    ajustes = {
        "bajar": -500,
        "mantener": 0,
        "subir": 300
    }

    if objetivo not in ajustes:
        raise ValueError("Objetivo no válido")

    return round(tdee + ajustes[objetivo])


def calcular_calorias_quemadas(tipo_ejercicio, minutos):
    """Calcula las calorías quemadas según el tipo de ejercicio."""
    if minutos <= 0:
        raise ValueError("Los minutos deben ser positivos")

    tasas = {
        "cardio": 7,
        "fuerza": 5,
        "hiit": 9,
        "yoga": 3,
        "natacion": 8,
        "deporte": 7,
        "otro": 5
    }

    if tipo_ejercicio not in tasas:
        return 0

    return round(tasas[tipo_ejercicio] * minutos)


def calcular_macros_objetivo(calorias_objetivo, objetivo):
    """Calcula la distribución de macros según el objetivo."""
    if calorias_objetivo <= 0:
        raise ValueError("Las calorías deben ser positivas")

    distribuciones = {
        "bajar": {"proteinas": 0.35, "carbohidratos": 0.40, "grasas": 0.25},
        "mantener": {"proteinas": 0.25, "carbohidratos": 0.50, "grasas": 0.25},
        "subir": {"proteinas": 0.30, "carbohidratos": 0.50, "grasas": 0.20}
    }

    if objetivo not in distribuciones:
        raise ValueError("Objetivo no válido")

    d = distribuciones[objetivo]
    return {
        "proteinas": round((calorias_objetivo * d["proteinas"]) / 4),
        "carbohidratos": round((calorias_objetivo * d["carbohidratos"]) / 4),
        "grasas": round((calorias_objetivo * d["grasas"]) / 9)
    }


def sumar_macros_del_dia(registros):
    """Suma los macros de todos los alimentos registrados en el día."""
    totales = {"calorias": 0, "proteinas": 0, "carbohidratos": 0, "grasas": 0}

    for item in registros:
        totales["calorias"] += item.get("calorias", 0)
        totales["proteinas"] += item.get("proteinas", 0)
        totales["carbohidratos"] += item.get("carbohidratos", 0)
        totales["grasas"] += item.get("grasas", 0)

    return totales


def validar_ingrediente(nombre, calorias, proteinas, carbohidratos, grasas):
    """Valida que un ingrediente tenga datos correctos antes de guardarlo."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    if any(v < 0 for v in [calorias, proteinas, carbohidratos, grasas]):
        raise ValueError("Los valores nutricionales no pueden ser negativos")
    return True
