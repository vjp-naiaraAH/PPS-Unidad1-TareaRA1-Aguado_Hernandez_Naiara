# Ejecución del programa mediante las opciones de Ejecución y Depuración de IDE

## Ejecución en terminal
### Configuración del Entorno

1. Comencé cerciorarme de saber si estaba Python instalado. para ello usé el comando 
~~~
python3 --version
~~~ 
![version phyton](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img8.png)

2. Seguidamente continué con la creación del entorno virtual con Python 
~~~bash
Python -m venv .venv
~~~

3. Lo activé con la ejecución de 
~~~bash
# Al activarlo ahora en la terminal saldrá delante (.venv) como se ve en la siguiente captura de pantalla
source .venv/bin/actívate
~~~

4. También instalé las dependencias de la siguiente manera
~~~bash
pip install -r requirements.txt && pip install -e .
~~~
![entorno virtual y dependencias](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img9.png)


### Primera ejecución del código
Para ejecutar el programa se hace poniendo lo siguiente 
~~~bash
PYTHONPATH=src python src/main_app.py
~~~
Esta primera ejecución no se completará puesto que el código cuenta con múltiples errores como se puede ver a continuación *líneas rojas y moradas*

![terminal ejecucion](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img10.png)

Por lo tanto como la finalidad es que funcione correctamente es lo que voy ha hacer a continuación.


### Errores hallados y posibles soluciones
#### Error 1: Falta de parámetro en llamada a función
```bash
File "home/PPSnaiara/Desktop/PPS-UNidad1-Tarea1-Aguado_Hernandez_Naiara/src/main_app.py", line 83 <module>
ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False)
TypeError: ejecutarSimulacion() missing 1 required positional argument 'encerado'
```
**Causa**
La llamada al ejemplo 4 en 'main_app.py' no tenía el parámetro obligatorio 'encerado' .

**Solución**
Añadí 'encerado=False' en la llamada del Ejemplo 4.
![fallo terminal](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img11.png)

Ahora si vuelvo a ejecutar el código lo hará correctamente. 
~~~bash
PYTHONPATH=src python src/main_app.py
~~~

Para finalizar la ejecución en ***terminal*** voy a salir y borrar el entorno virtual con el uso del siguiente comando
~~~bash
deactivate && rm -rf .venv
~~~
![desactivar entorno virtual](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img12.png)
---

## Depuración visual en el IDE (Visual Studio Code)
Utilicé el depurador de Visual Studio Code para analizar el flujo del programa paso a paso
** Uso de breakpoints** 
Los breakpoints permiten detener la ejecución en líneas específicas para inspeccionar el estado del programa.
- La llamada al Ejemplo 1 en `main_app.py` (para observar el inicio de la simulación completa).
- La línea `lavadero.hacerLavado(...)` (para ver cómo se configuran las opciones de lavado).
- La línea `lavadero.avanzarFase()` dentro del bucle (para controlar el cambio de fases línea por línea).

![ubicacion breakpoints](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img13.png)


### Ejecución del código con Run and Debug
1. Hacer clic sobre el icono de `play+insecto` 
![boton run and debug](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img14.png)
1. Luego clic sobre el botón de `Run and Debug`
![boton azul](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img15.png)
1. Ahora se abrirá otro menú hacia abajo, en el que selecciono la opción `Python File`
![file](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img17.png)
En esta captura se aprecian los breakpoints (bolitas rojas), la línea parada (amarilla) y los valores iniciales de las variables del lavadero.
![paron breakpoint](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img18.png)
Al depurar el Ejemplo 1, observé que con `secado_a_mano = True` y `encerado = True`, la transición desde fase 5 (rodillos) iba directamente a fase 6 (secado automático), omitiendo las fases 7 y 8.
En esta captura el depurador está parado en `avanzarFase()` con `fase = 5` y opciones de secado/encerado activadas. Al avanzar, pasa erróneamente a fase 6.
![captura](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img19.png)

- **Causa**: Lógica de transiciones invertida e incompleta en el método `avanzarFase` de `lavadero.py`.

- **Solución**: Corregido en el Apartado 3 en las pruebas unitarias.
