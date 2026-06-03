# Lenguaje L - DSL para la Automatización de Micro Redes Eléctricas Inteligentes (ECO-GRID)

Este apartado contiene la especificación formal, reglas gramaticales y scripts de prueba operativos del **Lenguaje L**, un Lenguaje de Dominio Específico (DSL) diseñado conceptualmente para el control automatizado, balance de carga autónomo y prevención de fallos críticos en el ecosistema de microredes eléctricas **ECO-GRID**.

## Descripción General

El **Lenguaje L** fue diseñado bajo restricciones formales rigurosas con el objetivo de ofrecer una abstracción de hardware simplificada y segura para ingenieros de sistemas energéticos. Al eliminar la complejidad de propósitos generales, permite un procesamiento directo, reduciendo la ambigüedad en entornos que demandan respuestas en tiempo real.

---

## Especificación Formal y Reglas Léxicas

### 1. Alfabeto y Sintaxis Base
* **Caracteres Válidos:** Letras del alfabeto latino (`a-z`, `A-Z`), dígitos numéricos (`0-9`), guión bajo (`_`) y símbolos delimitadores/operadores (`(`, `)`, `,`, `=`, `>`, `<`).
* **Operadores Lógicos:** Uso de la palabra clave reservada `Y`.
* **Identificadores:** Los nombres de variables o dispositivos deben comenzar estrictamente con una **letra minúscula**, seguida de caracteres alfanuméricos o guiones bajos (e.g., `temp_bateria1`, `estado_reles`).

### 2. Literales Soportados
* **Numéricos:** Enteros y de punto flotante para lecturas analógicas precisas (e.g., `10`, `10.5`).
* **Booleanos:** Representados de forma estricta por las palabras clave `VERDADERO` y `FALSO`.

### 3. Delimitación de Bloques
El analizador léxico procesa los espacios en blanco, tabulaciones y saltos de línea únicamente como separadores de tokens (sintaxis libre). La estructura del código no depende de la indentación; en su lugar, se emplean tokens unificados con guión bajo (`FIN_SI`, `FIN_MIENTRAS`) para el cierre formal de ámbitos de control.

---

## Palabras Clave y Primitivas Nativas

El DSL cuenta con un conjunto restringido de palabras reservadas e instrucciones nativas mapeadas directamente al hardware de la microred:

* **Control de Flujo:** `SI`, `ENTONCES`, `SINO`, `FIN_SI`, `MIENTRAS`, `EJECUTAR`, `FIN_MIENTRAS`, `Y`.
* **Primitivas del Sistema:**
  * `init_grid`: Inicializa los controladores de bajo nivel y canales de comunicación.
  * `leer_temperatura(id)`: Devuelve un valor flotante en grados Celsius ($^\circ\text{C}$) del sensor térmico especificado.
  * `estado_carga(id)`: Devuelve el porcentaje de almacenamiento del banco de baterías ($0$ a $100$).
  * `leer_flujo(id)`: Mide el flujo de entrada o salida analógica en kilovatios ($\text{kW}$) desde los inversores.
  * `conmutar_linea(id, estado)`: Envía una señal síncrona al relé de alta potencia para conectar (`VERDADERO`) o aislar (`FALSO`) un sector.
  * `alerta_emergencia(mensaje)`: Envía una interrupción prioritaria a la interfaz HMI del operador.

---

## Gramática Sintáctica Abstracta (BNF)

Para garantizar un parsing determinista y libre de ambigüedades, el árbol de análisis sintáctico (AST) se rige bajo la siguiente notación Backus-Naur Form (BNF) expandida:

```bnf
<Sentencia_Condicional> ::= "SI" <Condicion> "ENTONCES" <Sentencias> "FIN_SI" 
                          | "SI" <Condicion> "ENTONCES" <Sentencias> "SINO" <Sentencias> "FIN_SI"

<Sentencia_Iterativa>   ::= "MIENTRAS" <Condicion> "EJECUTAR" <Sentencias> "FIN_MIENTRAS"

<Asignación>            ::= <Identificador> "=" <Expresión>

<Llamada_Primitiva>     ::= <Nombre_Funcion> "(" <Argumentos> ")"

<Condicion>             ::= <Expresión> <Comparador> <Expresión> 
                          | <Condicion> "Y" <Condicion>

<Expresión>             ::= <Identificador> | <Literal_Numerico> | <Llamada_Primitiva>

<Comparador>            ::= ">" | "<" | "="

<Argumentos>            ::= <Identificador> | <Literal_Numerico> 
                          | <Identificador> "," <Argumentos>
