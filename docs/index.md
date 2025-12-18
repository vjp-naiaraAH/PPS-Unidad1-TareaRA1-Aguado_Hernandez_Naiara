# Unidad 1 - Tarea RA1: Prueba de Aplicaciones

**Aplicación: Lavadero de coches**  
**Alumno/a**: Naiara Aguado Hernández  
**Fecha**: 18 de diciembre de 2025  

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

- [Unidad 1 - Tarea RA1: Prueba de Aplicaciones](#unidad-1---tarea-ra1-prueba-de-aplicaciones)
  - [Objetivos de la tarea](#objetivos-de-la-tarea)
  - [Índice de contenidos](#índice-de-contenidos)
  - [1. Elementos de Python (Documentación del código)](#1-elementos-de-python-documentación-del-código)
    - [Resumen de elementos clave documentados](#resumen-de-elementos-clave-documentados)
  - [Apartados detallados](#apartados-detallados)
    - [→ ejecucion\_depuracion.md](#-ejecucion_depuracionmd)
    - [→ pruebas.md](#-pruebasmd)
    - [→ sandboxing.md](#-sandboxingmd)
    - [→ reflexion.md](#-reflexionmd)
  - [Herramientas utilizadas](#herramientas-utilizadas)

---

## 1. Elementos de Python (Documentación del código)

He documentado detalladamente el código fuente de la aplicación `lavadero.py` mediante un **Jupyter Notebook** donde explico línea por línea:

- La estructura de la clase `Lavadero`
- El significado de cada constante y atributo
- El funcionamiento de cada método
- El flujo de control y las reglas de negocio

> **Archivo Jupyter Notebook con todo el código comentado**:  
> [Ver Actividad-ElementosPrograma-Python.ipynb](../src/Actividad-ElementosPrograma-Python.ipynb)  
> *(Haz clic para abrirlo en VS Code o Jupyter Lab. Recomendado visualizar en modo presentación para mejor lectura)*

### Resumen de elementos clave documentados

| Elemento                    | Descripción breve                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------|
| `class Lavadero`            | Clase principal que simula el túnel de lavado                                     |
| Constantes `FASE_INACTIVO` a `FASE_ENCERADO` | Representan las 9 fases posibles del proceso (0-8)                                |
| `__init__`                  | Inicializa el lavadero en estado inactivo (requisito 1)                           |
| Propiedades `@property`     | Acceso seguro de solo lectura a atributos privados                                |
| `terminar()`                | Restablece el lavadero al estado inicial                                          |
| `hacerLavado(...)`          | Inicia lavado validando reglas (requisitos 2 y 3)                                 |
| `_cobrar()`                 | Calcula ingresos según opciones (requisitos 4-8)                                   |
| `avanzarFase()`             | Gestiona el flujo secuencial de fases (requisitos 9-14)                           |
| `imprimir_estado()`         | Muestra información completa del estado actual                                    |

![Captura del Jupyter Notebook con comentarios detallados](images/notebook_elementos_python.png)

*(Si no tienes captura aún, abre el notebook, haz una pantalla completa y guárdala con ese nombre en `docs/images/`)*

---

## Apartados detallados

### [→ ejecucion_depuracion.md](ejecucion_depuracion.md)  
Ejecución en terminal, corrección de errores iniciales, depuración visual en VS Code con breakpoints, panel de variables y detección de errores lógicos en el flujo de fases.

### [→ pruebas.md](pruebas.md)  
Diseño y ejecución de 14 pruebas unitarias con unittest, análisis de fallos, correcciones aplicadas y resultado final con todos los tests pasando.

### [→ sandboxing.md](sandboxing.md)  
Ejecución de la aplicación en un entorno aislado (sandbox), descripción del método utilizado y capturas del proceso.

### [→ reflexion.md](reflexion.md)  
Reflexión personal sobre las medidas de seguridad incorporadas en diferentes lenguajes de programación.

---

## Herramientas utilizadas

- **IDE**: Visual Studio Code  
- **Formato de documentación**: Jupyter Notebook (.ipynb)  
- **Depuración**: Run and Debug integrado  
- **Pruebas**: unittest  
- **Documentación final**: MkDocs con tema Material + búsqueda en internet
- **Repositorio**: GitHub + GitHub Pages