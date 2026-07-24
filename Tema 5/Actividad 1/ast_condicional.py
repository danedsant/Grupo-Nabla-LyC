# Definicion de una clase base genérica para todos los nodos del AST
class NodoAST:
    pass

class Identificador(NodoAST):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f"ID({self.nombre})"

#  Definicion de clase para valores literales (como el número 3)
class Literal(NodoAST):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return f"LITERAL({self.valor})"

#  Definicion de Clase para operaciones lógicas/relacionales (x > 3)
class OperacionRelacional(NodoAST):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha
        
    def __str__(self):
        return f"RelOp({self.operador})"

#  Definicion de Clase para llamadas a funciones ( print(x) )
class LlamadaFuncion(NodoAST):
    def __init__(self, nombre_funcion, argumento):
        self.nombre_funcion = nombre_funcion
        self.argumento = argumento # Simplificado a un solo argumento para este ejemplo
        
    def __str__(self):
        return f"CALL({self.nombre_funcion})"

#  Definicion de Clase principal para la estructura de control IF
class EstructuraIf(NodoAST):
    def __init__(self, condicion, cuerpo_verdadero):
        self.condicion = condicion
        self.cuerpo_verdadero = cuerpo_verdadero
        
    def __str__(self):
        return "IF_STATEMENT"

#  Definicion de una función para imprimir el árbol estructurado de manera legible
def imprimir_arbol_if(nodo, nivel=0):
    indentacion = "  " * nivel
    print(f"{indentacion}└─> {nodo}")
    
    if isinstance(nodo, EstructuraIf):
        print(f"{indentacion}    ├─> [Condición]")
        imprimir_arbol_if(nodo.condicion, nivel + 2)
        print(f"{indentacion}    └─> [Cuerpo]")
        imprimir_arbol_if(nodo.cuerpo_verdadero, nivel + 2)
        
    elif isinstance(nodo, OperacionRelacional):
        imprimir_arbol_if(nodo.izquierda, nivel + 1)
        imprimir_arbol_if(nodo.derecha, nivel + 1)
        
    elif isinstance(nodo, LlamadaFuncion):
        imprimir_arbol_if(nodo.argumento, nivel + 1)

# Implementación de un ejemplo de uso del AST para una estructura condicional
# Simulamos el análisis de: if (x > 3) print(x)

# Construccion de la condición: x > 3
nodo_x_condicion = Identificador("x")
nodo_3 = Literal(3)
nodo_condicion = OperacionRelacional(nodo_x_condicion, ">", nodo_3)

# Construccion de el cuerpo: print(x)
nodo_x_cuerpo = Identificador("x")
nodo_print = LlamadaFuncion("print", nodo_x_cuerpo)

# Construccion de la estructura principal del IF
raiz_if = EstructuraIf(nodo_condicion, nodo_print)

# Imprimir la estructura del AST resultante
print("Estructura del AST para: if (x > 3) print(x)")
imprimir_arbol_if(raiz_if)