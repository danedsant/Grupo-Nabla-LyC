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

### Ejemplos de Herramientas de Dibujo

1. Ejemplo: El Cubo (Proyección Tridimensional sobre Plano 2D)Objetivo: Representar un hexaedro regular aplicando desplazamiento lineal simétrico para superponer dos caras cuadradas interconectadas por aristas oblícuas o de profundidad.Cadena resultante esperada:

$acacacacgcacaaacatcacagcacacaacatcaca$

Proceso de Derivación Formal:$$\begin{aligned}
S &\Rightarrow acacacacC_1 & \text{(Aplicando Regla 1)} \\
&\Rightarrow acacacac(gcacaaacatC_2) & \text{(Aplicando Regla 4: } C_1 \rightarrow gcacaaacatC_2) \\
&\Rightarrow acacacacgcacaaacat(cacagcacacaacatC_3) & \text{(Aplicando Regla 5: } C_2 \rightarrow cacagcacacaacatC_3) \\
&\Rightarrow acacacacgcacaaacatcacagcacacaacat(caca) & \text{(Aplicando Regla 6: } C_3 \rightarrow caca) \\
&\Rightarrow acacacacgcacaaacatcacagcacacaacatcaca & \text{(Cadena terminal validada)}
\end{aligned}$$

<img width="535" height="251" alt="imagen3" src="https://github.com/user-attachments/assets/ceb5c173-3ebe-43e1-9f69-41c7eb77b31b" />

### Mecanismo de Ejecución Gráfica
Ejecuta la secuencia inicial $acacacac$ para constituir por completo el cuadrado bidimensional frontal. En vértices clave específicos, el terminal $g$ congela la coordenada bidimensional y efectúa un desfase geométrico para trazar las líneas de profundidad y estructurar el cuadrado posterior. Con el terminal $t$ se recupera el nodo original eliminando la necesidad de trazar líneas repetidas sobre los mismos ejes.
