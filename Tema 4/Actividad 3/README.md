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

## Instalación de Dependencias (Windows <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/ec844411-9bc4-403a-97b5-418b801ec434" />)

Para compilar y ejecutar este proyecto en Windows, se requiere configurar manualmente las herramientas de compilación o utilizar una terminal emulada. Siga uno de los siguientes métodos:

#### Método 1: Configuración Manual (Recomendado para tu entorno actual)

- **Flex:** Descargue e instale el paquete binario de Flex para Windows desde el proyecto GnuWin32 (instalado típicamente en `C:\Program Files (x86)\GnuWin32\bin\flex.exe`).
- **Compilador C++ (MinGW/GCC):** Asegúrese de contar con un entorno GCC para Windows, como el incluido en **Dev-C++** o **MinGW-w64** (ubicado típicamente en `C:\Dev-Cpp\MinGW64\bin\g++.exe`).
- **Variable de Entorno (Opcional):** Se recomienda añadir ambas rutas binarias al `PATH` del sistema para poder invocar directamente los comandos `flex` y `g++` sin necesidad de escribir sus rutas absolutas.

#### Método 2: Usando el Gestor de Paquetes Chocolatey (Alternativa Automatizada)
Si tiene instalado el gestor de paquetes Chocolatey en la PowerShell de Windows, puede instalar ambas herramientas ejecutando:

**```bash**

**choco install winflexbison mingw -y**
