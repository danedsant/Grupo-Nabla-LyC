import re
import sys

# Definicion del diccionario de tokens y expresiones regulares para Dockerfile

tokens_docker = [
    # ELEMENTOS IGNORABLES Y DE CONTROL
    ('TK_COMMENT', r'#.*'),
    ('TK_SPACE', r'[\t ]+'),
    ('TK_NEWLINE', r'\n'),

    # PALABRAS RESERVADAS
    ('TK_FROM', r'\bFROM\b'),
    ('TK_RUN', r'\bRUN\b'),
    ('TK_WORKDIR', r'\bWORKDIR\b'),
    ('TK_COPY', r'\bCOPY\b'),
    ('TK_CMD', r'\bCMD\b'),

    # ESTRUCTURAS CERRADAS
    ('TK_STRING', r'"[^"]*"'),

    # VALORES GENERICOS 
    ('TK_ARGUMENT', r'[a-zA-Z0-9_./:\-]+'),

    # MANEJO DE ERRORES 
    ('TK_MISMATCH', r'.')
]

# Funcion principal del Analizador Lexico
def lexer(texto_fuente):

    # Unir todas las regex en una sola utilizando grupos nombrados de Python
    regex_maestra = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in tokens_docker)
    
    linea_actual = 1
    inicio_linea = 0
    
    print("\n--[ INICIO DEL ANALISIS LEXICO ]--\n")
    
    # Se emplea la funcion finditer que escanea el string de izquierda a derecha buscando coincidencias
    for coincidencia in re.finditer(regex_maestra, texto_fuente):

        # Se obtiene el tipo de token y el lexema correspondiente a la coincidencia encontrada
        tipo_token = coincidencia.lastgroup
        lexema = coincidencia.group(tipo_token)
        
        # Si se encuentra un salto de linea, se actualiza la linea actual y el inicio de la línea
        if tipo_token == 'TK_NEWLINE': 
            inicio_linea = coincidencia.end()
            linea_actual += 1
            
        elif tipo_token in ['TK_SPACE', 'TK_COMMENT']:
            continue # Ignoramos los espacios y los comentarios de Docker
            
        elif tipo_token == 'TK_MISMATCH':

            # Si se encuentra un token no reconocido, se indica el error lexico y se detiene la ejecucion del programa
            columna = coincidencia.start() - inicio_linea
            print(f"\nERROR LEXICO: Caracter no reconocido '{lexema}' en la linea {linea_actual}, columna {columna}")
            sys.exit(1) 
            
        else:
            # Token valido encontrado
            columna = coincidencia.start() - inicio_linea
            print(f"Token: {tipo_token:<15} | Lexema: {lexema:<20} | Línea: {linea_actual}")

# Lectura del archivo dockerfile
def cargar_archivo(nombre_archivo):

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
        
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        sys.exit(1)

# Punto de entrada del script
if __name__ == '__main__':

    # Validamos que se pase el archivo dockerfile por argumento
    if len(sys.argv) < 2:
        
        print("Uso correcto: python lexer_docker.py <archivo_dockerfile>")
        sys.exit(1)
        
    ruta_archivo = sys.argv[1]
    codigo_fuente = cargar_archivo(ruta_archivo)
    
    lexer(codigo_fuente)
    print("\n--[ FIN DEL ANALISIS LEXICO ]--")