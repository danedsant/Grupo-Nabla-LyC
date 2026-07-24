# Actividad 1 



## Descripción de actividad
Este directorio contiene la implementación práctica correspondiente a la **Pregunta 1** del Tema 5. El objetivo principal es la comprensión, definición, caracterización y modelado de **Árboles de Sintaxis Abstracta (AST)**.

Se han desarrollado dos ejemplos prácticos aplicando Programación Orientada a Objetos para representar la jerarquía computacional pura del código fuente, omitiendo elementos puramente sintácticos que no aportan significado semántico a las operaciones.

## Estructura de Archivos
* `ast_aritmetico.py`: Implementación del Ejemplo A (Expresión aritmética `a + b * c`). Demuestra la precedencia de operadores matemáticos mediante el anidamiento profundo de nodos `OperacionBinaria`.

* `ast_condicional.py`: Implementación del Ejemplo B (Estructura de control `if (x > 3) print(x)`). Modela constructos de control de flujo, nodos lógicos relacionales, literales e identificadores, abstrayendo elementos léxicos como los paréntesis.

## Entorno de Desarrollo y Pruebas
Los scripts fueron programados y validados bajo el siguiente entorno:
* **Lenguaje:** Python 3.x
* **Plataforma:** Lenovo ThinkPad T480 - Windows 11

## Instrucciones de Ejecución
No se requieren dependencias externas ni compiladores adicionales. Para visualizar la construcción por consola y el recorrido de los árboles sintácticos, ejecute:

`python ast_aritmetico.py`
`python ast_condicional.py`