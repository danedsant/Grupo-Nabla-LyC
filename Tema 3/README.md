# Analizador Léxico PGN Simplificado - Sección 2.4

Este módulo corresponde al **Rol 4: Diseñador de Autómatas** dentro del Tema 3 (Lenguajes y Gramáticas Formales) para la cátedra de Lenguajes y Compiladores de la **Universidad Nacional Experimental de Guayana (UNEG)**.

La aplicación consiste en un compilador/analizador a nivel léxico que valida si un movimiento de ajedrez pertenece al lenguaje formal propuesto, implementando tanto una expresión regular como la simulación exacta de un Autómata Finito Determinístico (AFD).

---

## 📋 Requerimientos del Rol

* **Contexto:** Analizar la notación estándar PGN (*Portable Game Notation*) de Ajedrez y definir un subconjunto simplificado para los movimientos básicos de posicionamiento.
* **Entregables:** 1. Diseño formal y algebraico de la Expresión Regular (Regex).
  2. Modelado de la estructura matemática del Autómata Finito Determinístico (AFD) equivalente.
  3. Código fuente funcional basado en la simulación del autómata carácter por carácter.

---

## 📐 Especificación Teórica del Lenguaje

### 1. El Subconjunto PGN Simplificado
Para garantizar un procesamiento lineal óptimo de Tipo 3 (Jerarquía de Chomsky), se redujo el formato a dos estructuras atómicas sin ambigüedad:
* **Movimientos de Peón:** Únicamente la casilla de destino (Ej: `e4`, `d5`).
* **Movimientos de Piezas:** La inicial de la pieza en mayúscula (`R`, `N`, `B`, `Q`, `K`) seguida de la casilla de destino (Ej: `Nf3`, `Qd8`).

### 2. Alfabeto Formal ($\Sigma$)
$$\Sigma = \{a, b, c, d, e, f, g, h, 1, 2, 3, 4, 5, 6, 7, 8, R, N, B, Q, K\}$$

### 3. Expresión Regular (Regex)
```regex
^([RNBQK]?[a-h][1-8])$
