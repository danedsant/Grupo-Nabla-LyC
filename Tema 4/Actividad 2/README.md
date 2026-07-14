# Analizador Léxico para Archivos Docker (Dockerfile)

## 📌 Descripción de la Actividad II

Esta actividad consiste en un analizador léxico implementado en el lenguaje de programación Python. Su objetivo principal es la verificación y tokenización de archivos de configuración `Dockerfile` mediante el uso estricto de Expresiones Regulares (Regex).

El analizador lee el archivo de entrada carácter a carácter y evalúa si las cadenas se ajustan a las estructuras léxicas definidas para el subconjunto de instrucciones de Docker (ej. `FROM`, `RUN`, `CMD`) Además, implementa manejo de errores mediante estados fallidos, el cual detiene el análisis al encontrar el primer carácter no reconocido y notifica al usuario la línea y columna exacta del error léxico.

## 🛠️ Tecnologías y Requisitos

* **Lenguaje:** Python 3.x
* **Librerías:** 
    - `re` - Expresiones Regulares nativas
    - `sys` - Interacción con el sistema.
* **Dependencias:** Ninguna. 


## ⚙️ Diccionario de Tokens y Jerarquía Léxica

El motor de expresiones regulares evalua los componentes léxicos en el siguiente orden jerárquico evitando colisiones:

1. **Elementos Ignorables:** `TK_COMMENT`, `TK_SPACE`, `TK_NEWLINE`.
2. **Palabras Reservadas:** `TK_FROM`, `TK_RUN`, `TK_WORKDIR`, `TK_COPY`, `TK_CMD`.
3. **Estructuras Cerradas:** `TK_STRING` (Cadenas entre comillas).
4. **Valores Genéricos:** `TK_ARGUMENT` (Rutas, versiones, nombres de imágenes).
5. **Manejo de Errores:** `TK_MISMATCH` (Atrapa cualquier carácter no válido).

## 🚀 Instalación y Ejecución

Al ser un script nativo de Python, no requiere un proceso de instalación complejo. 

1. Extraer el contenido del archivo comprimido `Lexer.rar` en una carpeta local.
2. Abrir una terminal (Símbolo del sistema, PowerShell o Bash) en la ruta de la carpeta del proyecto.
3. Ejecutar el script pasando como argumento el nombre del archivo de prueba que se desea analizar:

```bash
# Para ejecutar la prueba exitosa básica:
python lexer_docker.py dockerfile_1

# Para ejecutar la prueba con comentarios:
python lexer_docker.py dockerfile_2

# Para ejecutar la prueba que detona el error léxico:
python lexer_docker.py dockerfile_3
```
Alternativamente se puede ejecutar el archivo `ejecutar_lexer.bat` contenido en el archivo comprimido `Lexer.rar`, el cual ejecuta las 3 pruebas consecuentemente.
> [!NOTE]
> Se debe pulsar la tecla enter para continuar con las pruebas.