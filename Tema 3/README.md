# 📚 Tema 3 - Lenguajes y Gramáticas Formales

## 📜 Descripción del repositorio

Este repositorio contiene el informe con la investigación teórica y el desarrollo práctico correspondiente al Tema de Lenguajes y Gramáticas Formales, el cual explora los fundamentos matemáticos y lógicos que rigen la creación, validación y procesamiento de lenguajes de programación, abarcando desde las reglas morfosintácticas generadoras hasta el diseño de autómatas para la fase léxica de un compilador.

## 📖 Resumen del contenido

### 1. Relación Entre Gramática y Lenguaje

Se define el Lenguaje Formal como el conjunto de cadenas válidas y la Gramática como su ente generador. Se explica detalladamente el proceso de derivación, demostrando cómo un compilador interactúa con símbolos No Terminales  y Terminales para construir código final válido.
___
### 2. Jerarquía de Chomsky

Estudio del nivel de complejidad de las gramáticas formales, clasificadas según su poder computacional y las restricciones teóricas de sus reglas:

- Tipo 3 (Regulares): Base de los analizadores léxicos y expresiones regulares.

- Tipo 2 (Libres de Contexto - GLC): Base de los analizadores sintácticos.

- Tipo 1 (Sensibles al Contexto): Reglas con dependencias estrictas del entorno.

- Tipo 0 (Irrestrictas): Lenguajes reconocibles por una Máquina de Turing.
___

### 3. Derivación y Modelado - Caso Práctico: Herramientas de Dibujo

Implementación de una Gramática Libre de Contexto (Tipo 2) para procesar instrucciones gráficas. Utilizando el alfabeto terminal $\Sigma = \{a, c, g, t\}$ y memoria de estado en pila (Push/Pop), se modelan y derivan rigurosamente figuras como:

- Un cuadrado bidimensional.

- Un árbol fractal con ramificaciones y hojas.

- La proyección de un cubo tridimensional sobre un plano 2D.

- Escaleras y rectángulos simétricos.
___
### 4. Higiene y Optimización de Gramáticas

Aplicación de ingeniería sobre gramáticas teóricas para evitar patologías críticas en analizadores predictivos. Se resuelven casos prácticos y algebraicos de:

Gramática Ambigua: Corrección de jerarquías para evitar conflictos de decisión y múltiples árboles de derivación.

Recursividad por la Izquierda: Transformación algorítmica para prevenir bucles infinitos en la ejecución del parser.

Factorización por la Izquierda: Optimización para desempatar producciones que comparten prefijos comunes.
___
### 5. De la Expresión al Autómata - Caso Práctico: Ajedrez PGN

Abstracción de la fase léxica aplicada al estándar Portable Game Notation (PGN). Se diseña una Expresión Regular (Regex) estricta para validar un subconjunto de movimientos tácticos básicos de peones y piezas mayores, modelando su correspondiente Autómata Finito Determinístico (AFD) para garantizar un procesamiento de reconocimiento en tiempo lineal.

