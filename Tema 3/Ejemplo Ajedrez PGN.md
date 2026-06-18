# Analizador Léxico PGN Simplificado

Analizar la notación estándar PGN (*Portable Game Notation*) de Ajedrez y definir un subconjunto simplificado para los movimientos básicos de posicionamiento.


## 📐 Especificación del Lenguaje

### 1. El Subconjunto PGN Simplificado
Para garantizar un procesamiento lineal óptimo de Tipo 3 (Jerarquía de Chomsky), se redujo el formato a dos estructuras atómicas sin ambigüedad:
* **Movimientos de Peón:** Únicamente la casilla de destino (Ej: `e4`, `d5`).
* **Movimientos de Piezas:** La inicial de la pieza en mayúscula (`R`, `N`, `B`, `Q`, `K`) seguida de la casilla de destino (Ej: `Nf3`, `Qd8`).

### 2. Alfabeto Formal ($\Sigma$)
$$\Sigma = \{a, b, c, d, e, f, g, h, 1, 2, 3, 4, 5, 6, 7, 8, R, N, B, Q, K\}$$

### 3. Expresión Regular (Regex)
```regex
^([RNBQK]?[a-h][1-8])$
```

### Demostracion interactiva
- https://ana-lex-grupo-nabla.vercel.app/
