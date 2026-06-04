# 📚 Tema 2: Los Lenguajes de Programación

Este apartado contiene los recursos, investigaciones y códigos desarrollados por el **Grupo Nabla** correspondientes al Tema 2 de la asignatura Lenguajes y Compiladores. El enfoque principal es el análisis de la infraestructura lingüística y computacional de las herramientas de desarrollo modernas.

### Enlace a defensa 
- https://www.youtube.com/watch?v=c_5YSLEfxQU
<a href="https://www.youtube.com/watch?v=c_5YSLEfxQU" target="_blank">
  <img src="https://img.youtube.com/vi/c_5YSLEfxQU/maxresdefault.jpg" alt="Miniatura del video" width="300" />
</a>

## 📝 Descripción de las Actividades

El desarrollo de este tema se estructuró en tres actividades principales:

* **Actividad I: Fundamentación Teórica e Investigación**

    Elaboración de un informe académico y su respectiva defensa (diapositivas) sobre la *"Arquitectura de Lenguajes y Compiladores"*. En esta etapa se establecieron las bases de los paradigmas de programación (Imperativo, Orientado a Objetos, Funcional, etc.) y se analizó el lenguaje como un producto de software sujeto a restricciones formales rigurosas.
---
* **Actividad II: Benchmarking Estructural (Conjetura de Collatz)**

    Prueba empírica de procesamiento intensivo utilizando la Conjetura de Collatz para medir y comparar el rendimiento de ejecución. Se implementaron algoritmos en **Python, JavaScript, Rust y Zig** para evidenciar cómo el diseño léxico (como el tipado dinámico vs. estático) impacta directamente en la velocidad de la máquina y el consumo de recursos de hardware.
---
* **Actividad III: Diseño de un Lenguaje de Dominio Específico (DSL) para Sistemas logico - físicos 
Críticos***

    Diseño conceptual y especificación formal del **"Lenguaje L"**, un Lenguaje de Dominio Específico (DSL) orientado a la automatización, balance de carga y prevención de fallos de micro redes eléctricas inteligentes (ECO-GRID). Se definieron sus reglas léxicas, primitivas nativas de hardware y gramática sintáctica abstracta (BNF).

---

## 🗂️ Estructura del Repositorio (Tema 2)

```text
Tema 2/
├── Actividad II/
│   ├── Javascript/
│   │   ├── collatz.js
│   │   └── README.md
│   ├── Python/
│   │   ├── collatz.py
│   │   └── README.md
│   ├── Rust/
│   │   ├── src/
│   │   │   └── main.rs
│   │   ├── Cargo.toml
│   │   └── README.md
│   ├── Zig/
│   │   ├── collatz.zig
│   │   └── README.md
│   └── README.md
├── Actividad III/
│   ├── EscenarioA.txt
│   ├── EscenarioB.txt
│   └── README.md
├── Grupo NABLA - Exposición Tema 2 (Diapositivas).pdf
├── Grupo NABLA - Tema 2 - Informe.pdf
└── README.md