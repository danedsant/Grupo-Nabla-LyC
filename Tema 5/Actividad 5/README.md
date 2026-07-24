## 🤖 Actividad N°5: Elaborar Asistente de Programación Híbrido para UnegScript

### 📌 Descripción de la Actividad
En el marco del **Tema 5 (Análisis Sintáctico)**, se diseñó e implementó un **asistente de programación híbrido** 
para el lenguaje **UnegScript** (un subconjunto funcional de Python/Rust).

El objetivo principal de esta actividad es acoplar las técnicas deterministas de compilación tradicional 
(expresiones regulares, tablas de tokens y parsing recursivo descendente) con componentes probabilísticos de Inteligencia Artificial 
(distancia de Levenshtein y un módulo de Fallback a LLM). Esto permite al compilador tolerar, autorecuperar y sugerir 
correcciones ante errores tipográficos en el código fuente sin detener la construcción del Árbol de Sintaxis Abstracta (AST).

### 🛠️ Arquitectura e Implementación

El desarrollo se encuentra integrado en el script ejecutable `unegscript_assistant.py`, estructurado en las siguientes fases principales:

#### 1. Analizador Léxico Híbrido (Lexer + AI Fallback)

* **Análisis Base (Regex):** Procesa los tokens estándar del vocabulario (palabras clave, operadores, delimitadores, literales numéricos y cadenas)
partiendo de la especificación original de `lexer.l`.

* **Cálculo de Confianza (≥ 0.8):** Si se detecta un token desconocido o ambiguo, se utiliza `difflib.SequenceMatcher` para calcular
el ratio de similitud léxica con palabras reservadas y built-ins. * *Ejemplo:* `pront` o `prnt` producen ratios de $0.80$ y $0.89$ respectivamente
frente a `print`, ejecutando una corrección automática directa.

* **Mecanismo de Fallback a IA (< 0.8):** Cuando la confianza de similitud cae por debajo del umbral de 0.8, se activa la función `fallback_ia()`,
simulando la consulta contextual a un LLM para inferir la intención del programador y reclasificar el token.

#### 2. Analizador Sintáctico (Parser Recursivo Descendente)

* **Lookahead & AST:** Implementa un parser descendente con inspección de tokens para construir la representación jerárquica del programa
mediante clases de AST (`ProgramNode`, `AssignNode`, `IfNode`, `CallNode`, `BinOpNode`, etc.).

* **Recuperación de Errores Sintácticos:** Permite continuar el flujo de análisis ante tokens inesperados, registrando la discrepancia
en el reporte de la IA sin colapsar la compilación.

### 🧪 Pruebas de Ejecución

El analizador fue puesto a prueba sobre el código fuente de entrada con errores léxicos:

```python
pront x=5; if x>3 prnt(x) else prnt("no")
```

### 💻 Cómo Ejecutar el Proyecto

**Ejecutar el asistente híbrido autónomo**
```python
python unegscript_assistant.py
```
