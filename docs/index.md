# Unidad 1 - Tarea RA1: Prueba de Aplicaciones

**Aplicación: Lavadero de coches**  
**Alumna**: Naiara Aguado Hernández  
**Fecha**: 19 de diciembre de 2025  

---

## Objetivos de la tarea

Esta actividad tiene los siguientes objetivos:

- Analizar y comprender la estructura interna del código (clases, métodos, flujos de control) y su modelo de ejecución (transiciones de estado y manejo de excepciones) para determinar los puntos críticos de prueba.

- Aplicar las herramientas del IDE (Integrated Development Environment) para la ejecución, depuración paso a paso y seguimiento del flujo de control, identificando y resolviendo posibles errores lógicos o de sintaxis.

- Diseñar, implementar y ejecutar pruebas unitarias que cubran la totalidad de los requisitos funcionales y no funcionales, validando la lógica individual de cada componente del código.

- Verificar que la aplicación maneja correctamente las reglas de negocio (precios, transiciones de fase y gestión de estados de error), tal como se define en la documentación.

- Ejecutar la aplicación en un entorno controlado para simular su comportamiento en un contexto real, validando la interacción entre sus componentes y el entorno de runtime.

---

## Índice de contenidos

- [1. Elementos de Python (Documentación del código)](#1-elementos-de-python-documentación-del-código)
- [2. Ejecución y Depuración](ejecucion_depuracion.md)
- [3. Pruebas unitarias](pruebas.md)
- [4. Ejecución en Sandbox](sandboxing.md)
- [5. Reflexión sobre seguridad de lenguajes](reflexion.md)

---

## 1. Elementos de Python (Documentación del código)

He documentado detalladamente el código fuente `lavadero.py` mediante un **Jupyter Notebook** donde explico línea por línea la estructura, constantes, métodos y flujo de control del programa.


### Resumen de elementos clave documentados

| Elemento                    | Descripción breve                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------|
| `class Lavadero`            | Clase principal que simula el túnel de lavado                                     |
| Constantes `FASE_*`         | Representan las 9 fases del proceso (0-8)                                          |
| `__init__`                  | Inicializa el lavadero cumpliendo requisito 1                                     |
| `@property`                 | Acceso de solo lectura a atributos privados                                       |
| `terminar()`                | Restablece el estado inicial                                                      |
| `hacerLavado(...)`          | Inicia lavado con validación de reglas (requisitos 2 y 3)                         |
| `_cobrar()`                 | Cálculo de ingresos según opciones (requisitos 4-8)                                |
| `avanzarFase()`             | Gestión del flujo de fases (requisitos 9-14)                                       |
| `imprimir_estado()`         | Visualización completa del estado actual                                          |

---

## 2. Ejecución y Depuración

He ejecutado la aplicación en el IDE VS Code, tanto en terminal como con depuración visual, identificando y corrigiendo errores de sintaxis y lógicos.

### Resumen de actividades realizadas

| Actividad                         | Descripción breve                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------|
| Ejecución en terminal             | Uso del comando `PYTHONPATH=src python3 src/main_app.py`                          |
| Corrección de errores             | TypeError por parámetro faltante y otros errores iniciales                        |
| Depuración visual                 | Breakpoints, panel de variables, avance paso a paso (F10)                         |
| Detección de errores lógicos      | Transiciones incorrectas en fases (detectado en fase 5)                           |

---

## 3. Pruebas unitarias

He diseñado e implementado 14 pruebas unitarias con `unittest` que cubren todos los requisitos funcionales (precios, excepciones, flujo de fases).

### Resumen de pruebas realizadas

| Tipo de prueba                    | Descripción breve                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------|
| Test 1                            | Estado inicial del lavadero                                                       |
| Tests 2-3                         | Excepciones ValueError (requisitos 2 y 3)                                         |
| Tests 4-8                         | Cálculo correcto de ingresos según opciones                                       |
| Tests 9-14                        | Secuencia exacta de fases para cada combinación de opciones                       |
| Ejecución final                   | Todos los tests pasan con `-v`                                                    |

---

## 4. Ejecución en Sandbox

He ejecutado la aplicación en un entorno aislado usando **Firejail** en Kali Linux, demostrando el aislamiento completo del programa.

### Resumen de actividades realizadas

| Actividad                         | Descripción breve                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------|
| Instalación                       | `sudo apt install firejail firetools`                                             |
| Ejecución                         | `firejail --private=. python3 main_app.py`                                        |
| Aislamiento                       | Sin acceso a red, archivos reales ni otros procesos                                |
| Resultado                         | Programa ejecutado correctamente dentro del sandbox                               |

---

## 5. Reflexión sobre seguridad de lenguajes

Reflexión personal comparando medidas de seguridad en lenguajes como Python, Java, Rust y C/C++, basada en contenidos teóricos y búsquedas.

### Temas tratados

| Tema                              | Descripción breve                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------|
| Manejo de memoria                 | Python (GC) vs Rust (ownership) vs C (manual)                                      |
| Excepciones y errores             | Try/except en Python vs checked exceptions en Java                                 |
| Vulnerabilidades comunes          | Inyecciones, overflows, race conditions                                           |
| Lenguajes más seguros             | Rust como referente actual                                                        |

---

## Herramientas utilizadas

- **IDE**: Visual Studio Code  
- **Documentación del código**: Jupyter Notebook (.ipynb)  
- **Depuración**: Run and Debug integrado  
- **Pruebas**: unittest  
- **Sandbox**: Firejail en Kali Linux  
- **Documentación final**: MkDocs con tema Material  
- **Repositorio**: GitHub + GitHub Pages  

---

Aguado Hernández Naiara 