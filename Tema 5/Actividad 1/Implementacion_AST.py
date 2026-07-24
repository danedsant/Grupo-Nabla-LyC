# Definicion de una clase base genérica para todos los nodos del AST
class NodoAST:
    pass

# Definicion de una clase para los Nodos Hoja (Operandos: Identificadores o Números)
class Identificador(NodoAST):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f"ID({self.nombre})"

# Definicion de una clase para los Nodos Internos (Operadores)
class OperacionBinaria(NodoAST):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda  # Puede ser otro NodoAST (rama) o una Hoja
        self.operador = operador    # El símbolo de la operación (+, *, etc.)
        self.derecha = derecha      # Puede ser otro NodoAST (rama) o una Hoja
        
    def __str__(self):
        return f"BinOp({self.operador})"

# Definimos una función para imprimir el árbol estructurado de manera legible
def imprimir_arbol(nodo, nivel=0):
    indentacion = "  " * nivel
    
    # Si es una operación, se imprime el operador y luego sus hijos
    if isinstance(nodo, OperacionBinaria):

        print(f"{indentacion}└─> {nodo}")
        imprimir_arbol(nodo.izquierda, nivel + 1)
        imprimir_arbol(nodo.derecha, nivel + 1)

    # Si es un identificador, simplemente lo imprimimos
    elif isinstance(nodo, Identificador):
        print(f"{indentacion}└─> {nodo}")

# Impplementación de un ejemplo de uso del AST
# simular lo que hace el parser al leer: a + b * c
# Recordamos la precedencia: la multiplicación (b * c) se agrupa primero.

# Primero construimos el subárbol de la multiplicación
nodo_b = Identificador("b")
nodo_c = Identificador("c")
nodo_multiplicacion = OperacionBinaria(nodo_b, "*", nodo_c)

# Luego construimos la raíz de la suma, pasando 'a' y el subárbol anterior
nodo_a = Identificador("a")
raiz_suma = OperacionBinaria(nodo_a, "+", nodo_multiplicacion)

# Mostramos el resultado
print("Estructura del AST para:  \na + b * c")
imprimir_arbol(raiz_suma)