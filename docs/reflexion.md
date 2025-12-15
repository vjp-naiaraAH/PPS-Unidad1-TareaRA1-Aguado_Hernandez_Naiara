# Reflexión sobre las medidas de seguridad de los principales lenguajes de programación
A continuación voy ha hacer una ***opinión personal*** a cerca de las **medidas de seguridad** que incorporan los diferentes *lenguajes de programación* habiendo leído el powerpoint proporcionado por el profesor y ampliando la información con búsquedas en internet.

---

> **“El lenguaje de programación que elijas influirá tanto en la seguridad de tu software como la cerradura que pones en tu puerta.”**  
> — Bruce Schneier (experto en criptografía y ciberseguridad)

---

La cita de Bruce Schneier que abre tanto la teoria de esta unidad como ahora esta reflexión resume perfectamente lo que he aprendido: **el lenguaje de programación que elegimos es la primera y más importante medida de seguridad que aplicamos a nuestro software**.

Los **lenguajes de bajo nivel** (C, C++, ensamblador) nos dan control absoluto, pero también responsabilidad absoluta. La gestión manual de memoria y los punteros hacen que errores como *buffer overflow*, *use-after-free* o desreferenciación de punteros nulos sean fáciles de cometer y extremadamente peligrosos. En 2025 siguen siendo la **causa principal de vulnerabilidades críticas en sistemas operativos**, navegadores y firmware.

Los **lenguajes de alto nivel** incorporan por diseño mecanismos que eliminan familias enteras de bugs:

- La **recolección automática de basura** (presente en Java, C#, Go, Python, PHP 8.x, JavaScript, etc.) evita fugas de memoria y muchos errores de liberación.  
- La verificación de límites en arrays y la ausencia de aritmética de punteros directos reducen drásticamente los desbordamientos.  
- Los sistemas de tipos estáticos fuertes y las comprobaciones en tiempo de compilación (especialmente avanzadas en lenguajes modernos como Rust) detectan errores de concurrencia y de acceso a memoria antes de la ejecución.  
- Los entornos de ejecución controlados (JVM, CLR, sandbox del navegador) añaden capas adicionales de aislamiento.

### Comparativa de medidas de seguridad estructural

| **Lenguaje**         | **Gestión de memoria**           | **Seguridad de memoria inherente** | **Prevención de errores comunes (overflow, inyecciones…)** | **Concurrencia segura** | **Protección estructural** |
|------------------|------------------------------|--------------------------------|--------------------------------------------------------|---------------------|------------------------|
| ***C / C++***      | Manual                       | Muy baja                       | Depende totalmente del programador                     | Manual y propensa   | ★☆☆☆☆                 |
| *Java*         | GC + verificación bytecode   | Muy alta                       | Alta (sandbox, prepared statements)                    | Buena               | ★★★★☆                 |
| ***C#***           | GC + CLR                     | Muy alta                       | Alta                                                   | Buena               | ★★★★☆                 |
| ***Python***       | GC automático                | Alta                           | Buena con frameworks y buenas prácticas                | Media (GIL)         | ★★★☆☆                 |
| ***Go***           | GC + canales                 | Muy alta                       | Alta                                                   | Excelente           | ★★★★☆                 |
| ***Rust***         | Ownership / borrow checker   | **Máxima** (garantías en tiempo de compilación) | Muy alta                                     | Excelente           | ★★★★★                 |
| ***PHP 8.x***      | GC automático                | Alta                           | Media-alta (según versión y código)                   | Básica              | ★★★☆☆                 |
| ***JavaScript***   | GC automático                | Alta                           | Buena en entornos modernos                             | Excelente (async)   | ★★★☆☆                 |

---

### Conclusión final
En conclusión, aunque ningún lenguaje garantiza por sí solo la seguridad absoluta *las buenas prácticas, revisiones de código y actualizaciones siguen siendo imprescindibles*, los lenguajes modernos ofrecen **niveles de protección estructural muy superiores** a los disponibles hace dos décadas.

Por ello, la selección del lenguaje debe considerarse una **decisión estratégica de seguridad** desde la fase inicial del proyecto, ya que condiciona directamente qué vulnerabilidades quedarán prácticamente eliminadas por diseño y cuáles requerirán controles adicionales durante todo el ciclo de vida del software.