# Realización de los test unitarios de la app
Lo primero que he hecho ha sido crear una carpeta llamada test, y dentro de la misma he creado un archivo llamado `test_lavadero_unittest.py`

![creacion de archivos y carpetas](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img20.png)

Dentro de este archivo he añadido las 14 pruebas `Testlavadero` utilizando *Unittest*, con 14 métodos de test correspondientes a cada requisito de la tarea.

---

## Pruebas realizadas
- Test 1-3: Estado inicial y excepciones (ValueError)
- Test 4-8: Cálculo correcto de ingresos según opciones
- Test 9-14: Secuencia exacta de fases para cada combinación de opciones (usando una función auxiliar `ejecutar_y_obtener_fases`)
---

## Ejecución de los test unitarios
En este paso como bien dice el título del mismo voy a ejecutar los test. Lo haré con el uso del siguiente comando:
~~~bash
Python -m unittest ./tests/test_lavadero_unittest.py -v
~~~
el cual me ha dado el siguiente resultado:
![resultado unnittest](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img21.png)

---

## Corrección de fallos
- ERROR en test 3: Lanza RuntimeError en vez de ValueError cuando el lavadero está ocupado
- FAIL en test 5 & 7: precios de secado incorrectos (6.20 y 7.70 en vez de 6.00 y 7.50).
- FAIL en test 9 a 14: flujo de fases mal (siempre va a la fase 6 o 7 cuando no debe y nunca llega a la fase 8)


### Error 1: excepción lavadero ocupado
**Causa**
Falla porque lanzaba RuntimeError en vez de ValueError
**Solución**
Cambié RuntimeError por ValueError
![Error 1 unittest](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img22.png)


### Error 2: precios
**Causa**
Los precios del encerado y del secado a mano daban erróneos puesto que estaban invertidos a cómo están definidos en las premisas
**Solución**
Poner los precios que ponen en las premisas.
![error 2 unittest](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img23.png)


### Error 3: flujo de fases
**Causa**
Si hay secado o encerado va a fase 6 (secado automático) en vez de 7. Además nunca llega a fase 8. 
**Solución**
Poner tal cual lo que hay en la imagen a continuación
![error 3 unittest](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img24.png)

---

## Ejecución después de corrección
Después de corregir los fallos mencionados anteriormente volví a ejecutar los test unitarios usando el comando mencionado anteriormente:
~~~bash
Python -m unittest ./tests/test_lavadero_unittest.py -v
~~~
Y ahora ya todos los test dan ok.
![todo ok](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img23.png)
