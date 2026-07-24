# Actividad 2: Comparación e Implementación de Analizadores Sintácticos LL y LR

# Responsable: Andrés Gómez

---

## 1. Definición y Comparación Teórica

El análisis sintáctico constituye la fase del compilador encargada de verificar que la secuencia de tokens generada por el analizador léxico cumpla con la estructura formal de una Gramática Libre de Contexto (GLC), construyendo un Árbol de Sintaxis Abstracta (AST).

* **Analizadores LL (Left-to-right, Leftmost derivation):**
  * **Estrategia:** Descendente (*Top-Down*). Construyen el árbol sintáctico desde la raíz (símbolo inicial) hacia las hojas.
  * **Mecanismo:** Leen la entrada de izquierda a derecha aplicando derivaciones por la izquierda.
  * **Restricciones:** Requieren gramáticas no ambiguas y sin recursión a la izquierda.

* **Analizadores LR (Left-to-right, Rightmost derivation in reverse):**
  * **Estrategia:** Ascendente (*Bottom-Up*). Construyen el árbol desde las hojas (tokens) hacia la raíz mediante la técnica de desplazamiento y reducción (*Shift-Reduce*).
  * **Mecanismo:** Leen la entrada de izquierda a derecha y construyen la derivación más a la derecha en orden inverso.
  * **Flexibilidad:** Admiten gramáticas más complejas y recursivas sin necesidad de transformaciones previas.

### Cuadro Comparativo

| Criterio | Análisis LL (ej. LL(1)) | Análisis LR (ej. SLR, LALR, LR(1)) |
| :--- | :--- | :--- |
| **Dirección del Análisis** | Descendente (*Top-Down*) | Ascendente (*Bottom-Up*) |
| **Construcción del AST** | Desde la raíz hacia las hojas | Desde las hojas hacia la raíz |
| **Derivación** | Derivación más a la izquierda (*Leftmost*) | Derivación más a la derecha en orden inverso |
| **Complejidad de Implementación** | Baja. Implementable mediante Funciones Recursivas Descendentes. | Alta. Requiere tablas de transición (*Action / Goto*). |
| **Gramáticas Soportadas** | Restrictivas (sin recursión izquierda). | Amplias y generales. |

---

## 2. Evidencia de Uso Actual en la Industria

* **Parsers LL:**
  * **ANTLR:** Herramienta moderna que utiliza algoritmos LL(*) adaptativos para motores de búsqueda de datos (Apache Hive, Presto) e IDEs.
  * **Compiladores de Producción:** Compiladores como `clang` (C/C++) y `Rust` utilizan parsers descendentes escritos a mano para ofrecer mensajes de error altamente detallados.

* **Parsers LR / LALR:**
  * **GNU Bison / Yacc:** Utilizados para generar parsers LALR(1) en gestores de bases de datos como **PostgreSQL** y lenguajes como **PHP**.
  * **Procesadores de DSL:** Aplicados cuando la gramática es naturalmente recursiva a la izquierda o densamente anidada.

---

## 3. Gramática del Lenguaje $L$

Para evaluar la cadena de prueba `3 + 5 * 2`, se definieron dos versiones de la gramática del lenguaje $L$:

### Gramática para LR (Ascendente - Original)
1. $E \to E + T$
2. $E \to T$
3. $T \to T * F$
4. $T \to F$
5. $F \to \mathbf{num}$

### Gramática para LL(1) (Descendente - Refactorizada sin recursión izquierda)
1. $E \to T \; E'$
2. $E' \to + \; T \; E' \;\mid\; \varepsilon$
3. $T \to F \; T'$
4. $T' \to * \; F \; T' \;\mid\; \varepsilon$
5. $F \to \mathbf{num}$
