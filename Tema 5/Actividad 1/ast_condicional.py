# Reutilizamos la clase base y el Identificador del ejemplo anterior
class NodoAST:
    pass

class Identificador(NodoAST):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f"ID({self.nombre})"

# 1. Nueva clase para valores literales (como el número 3)
class Literal(NodoAST):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return f"LITERAL({self.valor})"

# 2. Clase para operaciones lógicas/relacionales (x > 3)
class OperacionRelacional(NodoAST):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha
        
    def __str__(self):
        return f"RelOp({self.operador})"

# 3. Clase para llamadas a funciones ( print(x) )
class LlamadaFuncion(NodoAST):
    def __init__(self, nombre_funcion, argumento):
        self.nombre_funcion = nombre_funcion
        self.argumento = argumento # Simplificado a un solo argumento para este ejemplo
        
    def __str__(self):
        return f"CALL({self.nombre_funcion})"

# 4. Clase principal para la estructura de control IF
class EstructuraIf(NodoAST):
    def __init__(self, condicion, cuerpo_verdadero):
        self.condicion = condicion
        self.cuerpo_verdadero = cuerpo_verdadero
        
    def __str__(self):
        return "IF_STATEMENT"

# --- FUNCIÓN AUXILIAR PARA VISUALIZAR EL ÁRBOL ---
def imprimir_arbol_if(nodo, nivel=0):
    indentacion = "  " * nivel
    print(f"{indentacion}└─ {nodo}")
    
    if isinstance(nodo, EstructuraIf):
        print(f"{indentacion}    ├─ [Condición]")
        imprimir_arbol_if(nodo.condicion, nivel + 2)
        print(f"{indentacion}    └─ [Cuerpo]")
        imprimir_arbol_if(nodo.cuerpo_verdadero, nivel + 2)
        
    elif isinstance(nodo, OperacionRelacional):
        imprimir_arbol_if(nodo.izquierda, nivel + 1)
        imprimir_arbol_if(nodo.derecha, nivel + 1)
        
    elif isinstance(nodo, LlamadaFuncion):
        imprimir_arbol_if(nodo.argumento, nivel + 1)

# --- CONSTRUCCIÓN MANUAL DEL AST ---
# Simulamos el análisis de: if (x > 3) print(x)

# A. Construimos la condición: x > 3
nodo_x_condicion = Identificador("x")
nodo_3 = Literal(3)
nodo_condicion = OperacionRelacional(nodo_x_condicion, ">", nodo_3)

# B. Construimos el cuerpo: print(x)
nodo_x_cuerpo = Identificador("x")
nodo_print = LlamadaFuncion("print", nodo_x_cuerpo)

# C. Ensamblamos la estructura principal del IF
raiz_if = EstructuraIf(nodo_condicion, nodo_print)

# Mostramos el resultado
print("Estructura del AST para: if (x > 3) print(x)")
imprimir_arbol_if(raiz_if)