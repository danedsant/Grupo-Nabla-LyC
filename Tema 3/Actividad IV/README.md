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

### Ejemplos de Herramienta de dibujo

1. **Ejemplo:** El Cubo (Proyección Tridimensional sobre Plano 2D)

- **Objetivo:** Representar un hexaedro regular aplicando desplazamiento lineal simétrico para superponer dos caras cuadradas interconectadas por aristas oblicuas o de profundidad.

- **Cadena resultante esperada:** acacacacgcacaaacatcacagcacacaacatcaca

**Proceso de Derivación Formal:**

S → acacacacC1 (Aplicando Regla 1) 
→ acacacac(gcacaaacatC2) (Aplicando Regla 4: C1 → gcacaaacatC2) 
→ acacacacgcacaaacat(cacagcacacaacatC3) (Aplicando Regla 5:  C2 → cacagcacacaacatC3)  
→ acacacacgcacaaacatcacagcacacaacat(caca) (Aplicando Regla 6:  C3 → caca) 
→ acacacacgcacaaacatcacagcacacaacatcaca (Cadena terminal validada)

### 3. Expresión Regular (Regex)

<img width="535" height="251" alt="image" src="https://github.com/user-attachments/assets/0a357527-ca99-4734-8c4e-88a1f4695e5b" />

**Mecanismo de Ejecución Gráfica:** Ejecuta la secuencia inicial acacacac para constituir por completo el cuadrado bidimensional frontal. En vértices clave específicos, el terminal g congela la coordenada bidimensional y efectúa un desfase geométrico para trazar las líneas de profundidad y estructurar el cuadrado posterior. Con la terminal t se recupera el nodo original eliminando la necesidad de trazar líneas repetidas sobre los mismos ejes. 

