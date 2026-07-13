# Analizador Léxico para $L_{Rust}$ mediante Flex (<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/b70a6d38-d47d-4fc1-8131-fd96126c59d3" />)

Este módulo contiene la especificación léxica e implementación automatizada de un lexer para 
el subconjunto de lenguaje $L_{Rust}$, desarrollado en C++ utilizando la herramienta de metacompilación Flex.

## Prerrequisitos del Sistema

Para compilar y ejecutar este software de manera local, 
es mandatorio contar con las siguientes herramientas instaladas en su entorno de ejecución (Linux / WSL recomendado):

- **Flex:** Generador de analizadores léxicos.
- **GCC / G++:** Compilador nativo de <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/b70a6d38-d47d-4fc1-8131-fd96126c59d3" />.

## Instalación de Dependencias (Ubuntu <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/0a7d0ab6-04be-4492-8b86-441c6de7b13b" />)

**```bash**

**sudo apt update**

**sudo apt install flex build-essential -y**

