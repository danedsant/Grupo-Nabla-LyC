# Analizador Léxico para $L_{Rust}$ mediante Flex (<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/b70a6d38-d47d-4fc1-8131-fd96126c59d3" />)

Este módulo contiene la especificación léxica e implementación automatizada de un lexer para 
el subconjunto de lenguaje $L_{Rust}$, desarrollado en C++ utilizando la herramienta de metacompilación Flex.

## Prerrequisitos del Sistema

Para compilar y ejecutar este software de manera local, 
es mandatorio contar con las siguientes herramientas instaladas en su entorno de ejecución (Linux / WSL recomendado):

- **Flex:** Generador de analizadores léxicos.
- **GCC / G++:** Compilador nativo de <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/b70a6d38-d47d-4fc1-8131-fd96126c59d3" />.

## Instalación de Dependencias (Ubuntu <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/0a7d0ab6-04be-4492-8b86-441c6de7b13b" />)

```bash
sudo apt update

sudo apt install flex build-essential -y
```

## Instalación de Dependencias (Windows <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/ec844411-9bc4-403a-97b5-418b801ec434" />)

Para compilar y ejecutar este proyecto en Windows, se requiere configurar manualmente las herramientas de compilación o utilizar una terminal emulada. Siga uno de los siguientes métodos:

### Método 1: Configuración Manual 

- **Flex:** Descargue e instale el paquete binario de Flex para Windows desde el proyecto GnuWin32 (instalado típicamente en `C:\Program Files (x86)\GnuWin32\bin\flex.exe`).

- **Compilador C++ (MinGW/GCC):** Asegúrese de contar con un entorno GCC para Windows, como el incluido en **Dev-C++** o **MinGW-w64** (ubicado típicamente en `C:\Dev-Cpp\MinGW64\bin\g++.exe`).

- **Variable de Entorno (Opcional):** Se recomienda añadir ambas rutas binarias al `PATH` del sistema para poder invocar directamente los comandos `flex` y `g++` sin necesidad de escribir sus rutas absolutas.

### Método 2: Usando el Gestor de Paquetes Chocolatey (Alternativa Automatizada)
Si tiene instalado el gestor de paquetes Chocolatey en la PowerShell de Windows, puede instalar ambas herramientas ejecutando:

```bash
choco install winflexbison mingw -y
```
## 📁 Estructura de Archivos

Antes de iniciar con la compilación, asegúrese de que su directorio de trabajo contenga los siguientes archivos esenciales:

*   `lexer.l`: Archivo de especificación léxica de Flex que contiene las expresiones regulares y acciones en C++.
*   `programa_prueba.rs`: Archivo de prueba que simula un código fuente escrito bajo las reglas sintácticas y semánticas de $L_{Rust}$.

---

## 🚀 Instrucciones de Compilación y Ejecución

Siga rigurosamente el orden de los siguientes comandos en su terminal para generar el autómata y evaluar el código fuente:

### Paso 1: Generar el código fuente de C++ desde Flex
Este comando compila las expresiones regulares abstractas en un Autómata Finito Determinista (AFD) y exporta el analizador léxico como código nativo de C++.

```bash
flex -o lex.yy.cc lexer.l
```
> [!NOTE]
> Esto creará un nuevo archivo en su directorio llamado lex.yy.cc

### Paso 2: Compilar el código generado mediante G++
Se utiliza el compilador de C++ para empaquetar las rutinas de bajo nivel del buffer de Flex junto al ejecutable final optimizado.
```
g++ lex.yy.cc -o lexer_rust
```
> [!NOTE]
> Esto generará el binario ejecutable llamado lexer_rust (o lexer_rust.exe en entornos Windows nativos).

### Paso 3: Ejecutar el analizador léxico pasándole un archivo de prueba
Invoque el programa binario redirigiendo el flujo de lectura hacia su archivo de código de pruebas:

**En entornos Linux<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/d01336ce-8b5d-4b6b-acdc-73d885d2d65f" />
 / WSL / Git Bash:**

```
./lexer_rust programa_prueba.rs
```

**En entornos Windows<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/279acd9c-d2db-4c3b-b21d-38fcec54c64a" />
 (CMD / PowerShell sin alias):**
```
.\lexer_rust.exe programa_prueba.rs
```
