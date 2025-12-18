# Sandbox
Un ***sandbox*** es un **entorno controlado**, aislado y seguro que se utiliza para ejecutar programas, procesar archivos o probar código sin que estos tengan la capacidad de afectar al sistema operativo principal ni a otros recursos críticos. La idea es crear un “espacio cerrado”, como una caja de arena donde los niños juegan sin peligro, pero aplicado a la informática.


### ¿Para que sirve?
+ Probar programas o código sin riesgo de daña el sistema
+ Analizar archivos sospechosos (como por ejemplo malware) sin infectar el equipo.
+ Ejecutar aplicaciones con permisos muy limitados
+ Simular entornos para desarrollo o experimentación


### ¿Como funciona?
Un **sandbox** funciona creando un entorno aislado donde un programa puede ejecutarse sin afectar al sistema real. Para lograrlo, limita los permisos del software: controla qué archivos puede tocar, qué procesos puede ver, cuánta memoria puede usar o si puede acceder a internet. Cada acción que intenta realizar pasa por un **filtro de seguridad**, y el sandbox decide si permitirla o bloquearla.

Además, utiliza un **sistema de archivos temporal** donde todo lo que el programa hace queda encerrado. De este modo, aunque intente modificar el sistema o comportarse de forma peligrosa, los cambios quedan atrapados en ese espacio aislado y se eliminan al cerrar el sandbox. Esto permite *probar código, analizar archivos* o *ejecutar software desconocido* sin riesgos.


### Ejemplos de Sandbox
- Máquinas virtuales (VirtualBox, VMware)
- Espacios de pruebas en navegadores (Chrome Sandbox)
- Herramientas coo Firejail, Sandboxie o Docker

---

## Prueba de aplicacion en un entorno controlado (Sandboxing)
En esta actividad voy a documentar como he podido realizar la prueba de la aplicación lavadero en un entorno controlado. 
Los objetivos de la actividad han sido:
- Conocer como se puede ejecutar programas, malware, etc en entornos controlados y aislados para su análisis
- Ser capaz de hacer Sandboxing de un programa


### Instalacion de Firejail y Firetools
Ejecuto en el terminal de Kali 
~~~
sudo apt install firejail
~~~ 
para instalar el software firejail por si acaso no está instalado en Kali aún.

![instalar firejail](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img26.png)
---

Ejecuto en la terminal sudo apt install firejail firetools puesto que es necesario ambos paquetes para poder usar correctamente el *Sandbox*.

![github](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img27.png)


### Ejecucion del Sandbox
Ahora sí ejecuto el programa dentro del Sandbox (entorno seguro) usando el comando 
~~~
firejail --private=. python3 main_app.py
~~~
Que sería el sandbox más básico de firejail
El resultado completo del firejail es el siguiente
~~~
Reading profile /etc/firejail/default.profile
Reading profile /etc/firejail/disable-common.inc
Reading profile /etc/firejail/disable-programs.inc
Reading profile /etc/firejail/landlock-common.inc
Warning: networking feature is disabled in Firejail configuration file

** Note: you can use --noprofile to disable default.profile **

firejail version 0.9.76

Parent pid 26642, child pid 26643
Warning: not remounting /var/lib/docker/overlay2/496d8f236f4874b190794e236f2699f12cbfc8a8a534fed6a4b1642cb1115c89/merged
Warning: not remounting /var/lib/docker/overlay2/c2b0fd92f4725f7bea99b07c335d646ec916132594f479316b3a19e5bd2a08de/merged
Warning: not remounting /var/lib/docker/overlay2/d2b2ff36569c4cc0893906ad61458840c88f3f70ef3c41384022d9558e4c4ee7/merged
Warning: not remounting /var/lib/docker/overlay2/7391c3341c935e0a627994b4db7fa67612122c6bb9501220ec77d122f4d01a14/merged
Warning: not remounting /var/lib/docker/overlay2/80f06f3463329cda539086cb9cbd8a7b4509bb0dbcdad15d549a62d957ed4e2c/merged
Warning: not remounting /var/lib/docker/overlay2/496d8f236f4874b190794e236f2699f12cbfc8a8a534fed6a4b1642cb1115c89/merged
Warning: not remounting /var/lib/docker/overlay2/c2b0fd92f4725f7bea99b07c335d646ec916132594f479316b3a19e5bd2a08de/merged
Warning: not remounting /var/lib/docker/overlay2/d2b2ff36569c4cc0893906ad61458840c88f3f70ef3c41384022d9558e4c4ee7/merged
Warning: not remounting /var/lib/docker/overlay2/7391c3341c935e0a627994b4db7fa67612122c6bb9501220ec77d122f4d01a14/merged
Warning: not remounting /var/lib/docker/overlay2/80f06f3463329cda539086cb9cbd8a7b4509bb0dbcdad15d549a62d957ed4e2c/merged
Warning: cannot find /var/run/utmp
Base filesystem installed in 34.50 ms
Child process initialized in 84.63 ms

=======================================================
EJEMPLO 1: Prelavado (S), Secado a mano (S), Encerado (S)
--- INICIO: Prueba de Lavado con Opciones Personalizadas ---
Opciones solicitadas: [Prelavado: True, Secado a mano: True, Encerado: True]

Coche entra. Estado inicial:
----------------------------------------
Ingresos Acumulados: 0.00 €
Ocupado: True
Prelavado a mano: True
Secado a mano: True
Encerado: True
Fase: 0 - Inactivo
----------------------------------------

AVANZANDO FASE POR FASE:
 (COBRADO: 8.70 €) -> Fase actual: 1 - Cobrando
-> Fase actual: 2 - Haciendo prelavado a mano
-> Fase actual: 3 - Echándole agua
-> Fase actual: 4 - Enjabonando
-> Fase actual: 5 - Pasando rodillos
-> Fase actual: 6 - Haciendo secado automático
-> Fase actual: 0 - Inactivo

----------------------------------------
Lavado completo. Estado final:
----------------------------------------
Ingresos Acumulados: 8.70 €
Ocupado: False
Prelavado a mano: False
Secado a mano: False
Encerado: False
Fase: 0 - Inactivo
----------------------------------------
Ingresos acumulados: 8.70 €
----------------------------------------

=======================================================
EJEMPLO 2: Sin extras (Prelavado: N, Secado a mano: N, Encerado: N)
--- INICIO: Prueba de Lavado con Opciones Personalizadas ---
Opciones solicitadas: [Prelavado: False, Secado a mano: False, Encerado: False]

Coche entra. Estado inicial:
----------------------------------------
Ingresos Acumulados: 8.70 €
Ocupado: True
Prelavado a mano: False
Secado a mano: False
Encerado: False
Fase: 0 - Inactivo
----------------------------------------

AVANZANDO FASE POR FASE:
 (COBRADO: 5.00 €) -> Fase actual: 1 - Cobrando
-> Fase actual: 3 - Echándole agua
-> Fase actual: 4 - Enjabonando
-> Fase actual: 5 - Pasando rodillos
-> Fase actual: 7 - Haciendo secado a mano
-> Fase actual: 0 - Inactivo

----------------------------------------
Lavado completo. Estado final:
----------------------------------------
Ingresos Acumulados: 13.70 €
Ocupado: False
Prelavado a mano: False
Secado a mano: False
Encerado: False
Fase: 0 - Inactivo
----------------------------------------
Ingresos acumulados: 13.70 €
----------------------------------------

=======================================================
EJEMPLO 3: ERROR (Encerado S, Secado a mano N)
--- INICIO: Prueba de Lavado con Opciones Personalizadas ---
Opciones solicitadas: [Prelavado: False, Secado a mano: False, Encerado: True]
ERROR DE ARGUMENTO: No se puede encerar el coche sin secado a mano

=======================================================
EJEMPLO 4: Prelavado (S), Secado a mano (N), Encerado (N)
Traceback (most recent call last):
  File "/home/PPSnaiara/main_app.py", line 83, in <module>
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: ejecutarSimulacion() missing 1 required positional argument: 'encerado'

Parent is shutting down, bye...
~~~

![github](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img28.png)
---

Como se ve en la próxima imágen, el programa se ejecuta dentro de un sandbox completamente aislado del resto del sistema. Esto confirma que la aplicación queda protegida aunque sea maliciosa o tenga vulnerabilidades. La opción `--debug` muestra en pantalla todo lo que Firejail está haciendo.

![github](https://github.com/vjp-naiaraAH/PPS-Unidad1-TareaRA1-Aguado_Hernandez_Naiara/blob/main/docs/images/img29.png)

---

## Conclusiones y reflexion
Gracias al uso de Firejail con la opción `--private`, la aplicación Python se ejecutó en un entorno completamente aislado:

- No tiene acceso al sistema de archivos real del host
- No puede acceder a la red
- No puede ver ni interactuar con otros procesos
- Cualquier cambio realizado desaparece al cerrar el sandbox

Esto demuestra que incluso si el script hubiera sido malicioso, no podría haber afectado al sistema real de Kali Linux.

Firejail es una herramienta extremadamente ligera y eficaz para sandboxing rápido de aplicaciones en Linux, ideal tanto para análisis de malware como para ejecutar software de procedencia desconocida con seguridad.