# NutriStock – Actividad N°8: Integración Continua

## 1. Descripción del proyecto
El presente repositorio corresponde al desarrollo de un módulo funcional de la aplicación **NutriStock**, orientada a asistir a los usuarios en la gestión de su alimentación mediante el uso de información nutricional y automatización de procesos.

En el marco de la Actividad N°8, se implementan prácticas de Gestión de la Configuración** e **Integración Continua (CI), con el objetivo de automatizar la validación del código y garantizar su calidad antes de ser integrado a la rama principal.

---

## 2. Organización del equipo y ramas de trabajo

El desarrollo se estructuró mediante el uso de ramas de características (feature branches), asignadas a cada integrante del equipo.

Romina trabajó en la rama `feature/romina-registro-comidas`, donde desarrolló la base del módulo.

Sofía trabajó en la rama `feature/sofia-calculo-macros`, encargándose de la simulación de errores en las pruebas automatizadas.

Facundo trabajó en la rama `feature/facundo-inventario`, enfocándose en la gestión del inventario.

Cada integrante desarrolló sus tareas de manera independiente sobre su respectiva rama, integrando posteriormente los cambios mediante Pull Requests hacia la rama principal. 

---

## 3. Tecnologías utilizadas

- Lenguaje: Python  
- Control de versiones: Git  
- Plataforma de repositorio: GitHub  
- Integración continua: GitHub Actions  
- Framework de testing: Pytest  
- Herramienta de análisis estático: Flake8  

---

## 4. Instrucciones para clonar y ejecutar el proyecto

### 4.1 Clonar el repositorio

```bash
git clone https://github.com/romiinavera/Actividad8_ING.git
cd Actividad8_ING
```

### 4.2 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4.3 Ejecutar pruebas unitarias

```bash
pytest
```

### 4.4 Ejecutar el análisis de estilo

```bash
flake8 .
```

---

## 5. Integración Continua

Se implementó un pipeline de Integración Continua utilizando GitHub Actions, configurado para ejecutarse automáticamente ante los siguientes eventos:

- Push a cualquier rama del repositorio
- Creación de Pull Requests hacia la rama principal (`main`)

### 5.1 Archivo de configuración

El pipeline se encuentra definido en el siguiente archivo:

```
.github/workflows/ci.yml
```

---
### 5.2 Funcionamiento de la Integración Continua en el proyecto

La Integración Continua en este proyecto se basa en la ejecución automática de un pipeline configurado en GitHub Actions. Cada vez que se realiza un push o se crea un Pull Request, el sistema ejecuta una serie de validaciones sobre el código.

Estas validaciones incluyen la instalación de dependencias, la verificación de estándares de estilo mediante Flake8 y la ejecución de pruebas unitarias con Pytest. En caso de que alguna de estas etapas falle, el pipeline se detiene e informa el error, impidiendo la integración del código a la rama principal.

De esta manera, se asegura que únicamente se integren cambios que cumplan con los criterios de calidad definidos por el equipo.

---

## 6. Funcionamiento del pipeline

El proceso automatizado ejecuta las siguientes etapas:

1. Clonado del repositorio
2. Configuración del entorno de ejecución
3. Instalación de dependencias
4. Ejecución de pruebas unitarias
5. Verificación de estándares de estilo mediante Flake8
6. Generación del estado del pipeline (éxito o fallo)

Este mecanismo permite detectar errores de manera temprana antes de la integración del código.

---

## 7. Pruebas automatizadas

Se implementaron pruebas unitarias utilizando Pytest, cubriendo las funcionalidades principales del módulo. Estas pruebas permiten validar el comportamiento esperado del sistema ante distintos escenarios.

---

## 8. Simulación de errores

Con el fin de validar el funcionamiento del pipeline de Integración Continua, se simularon errores controlados.

### 8.1 Error de prueba fallida

En la rama `feature/sofia-calculo-macros` se introdujo una modificación intencional en la función de cálculo:

```python
return round(tasas[tipo_ejercicio] + minutos)
```

Esta modificación generó un resultado incorrecto, provocando el fallo de las pruebas automatizadas y, en consecuencia, del pipeline.

### 8.2 Resolución

El error fue corregido restableciendo la operación original:

```python
return round(tasas[tipo_ejercicio] * minutos)
```

Tras la corrección, las pruebas fueron superadas y el pipeline finalizó exitosamente.

---

### 8.3 Error de estilo

Se introdujeron errores de formato en el código (por ejemplo, inconsistencias en espacios o indentación), los cuales fueron detectados por la herramienta Flake8.

### 8.4 Resolución

Se realizaron los ajustes necesarios para cumplir con las normas de estilo establecidas, logrando nuevamente un pipeline exitoso.

---

## 9. Flujo de trabajo adoptado

El equipo implementó el siguiente flujo de trabajo:

1. Desarrollo en ramas individuales (`feature/*`)
2. Realización de commits y envío de cambios al repositorio remoto
3. Ejecución automática del pipeline de CI
4. Creación de Pull Requests hacia la rama principal
5. Integración de cambios únicamente si el pipeline finaliza correctamente

Este enfoque permite mantener la estabilidad del código y minimizar errores en la rama principal.

---

## 10. Resultados

El uso de Integración Continua permitió:

- Detectar errores de manera temprana
- Automatizar procesos de validación
- Mejorar la calidad del código
- Facilitar el trabajo colaborativo

---

## 11. Enlace al repositorio

https://github.com/romiinavera/Actividad8_ING

---

## 12. Conclusión

La implementación de Integración Continua en el proyecto permitió automatizar la validación del código, garantizando estándares de calidad y facilitando la integración segura de cambios. Esta práctica resulta fundamental para el desarrollo colaborativo y escalable de software. 
