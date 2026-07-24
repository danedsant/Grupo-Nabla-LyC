import re
import sys
import difflib
from typing import List, Dict, Any, Tuple, Optional

# =====================================================================
# 1. Definicion de Vocabulario y Tipos de Tokens (segun lexer.l)
# =====================================================================

VOCABULARY = {
    # Palabras clave
    "fn": "TK_FN",
    "let": "TK_LET",
    "mut": "TK_MUT",
    "if": "TK_IF",
    "else": "TK_ELSE",
    "return": "TK_RETURN",
    "true": "TK_TRUE",
    "false": "TK_FALSE",
    "i32": "TK_I32",
    "f32": "TK_F32",
    "bool": "TK_BOOL",
    # Identificadores predefinidos (Built-ins)
    "print": "TK_IDENT"
}

# Tabla de Tokens para el Lexer Tradicional
TOKEN_PATTERNS = [
    # Comentarios y Espacios (seran ignorados o procesados)
    ("COMMENT", r"//.*"),
    ("WS", r"[ \t\r]+"),
    ("NEWLINE", r"\n"),
    
    # Operadores y Delimitadores (segun lexer.l)
    ("TK_ARROW", r"->"),
    ("TK_EQ", r"=="),
    ("TK_NE", r"!="),
    ("TK_LT", r"<"),
    ("TK_GT", r">"),
    ("TK_ASSIGN", r"="),
    ("TK_PLUS", r"\+"),
    ("TK_MINUS", r"-"),
    ("TK_MUL", r"\*"),
    ("TK_DIV", r"/"),
    ("TK_LBRACE", r"\{"),
    ("TK_RBRACE", r"\}"),
    ("TK_LPAREN", r"\("),
    ("TK_RPAREN", r"\)"),
    ("TK_COLON", r":"),
    ("TK_SEMI", r";"),
    ("TK_COMMA", r","),
    
    # Literales (incluyendo strings para soportar "no")
    ("TK_LIT_FLOAT", r"\d+\.\d+"),
    ("TK_LIT_INT", r"\d+"),
    ("TK_LIT_STR", r'"[^"\\]*(?:\\.[^"\\]*)*"'), # Soporte para literales de cadena
    
    # Identificadores / Palabras Clave base
    ("TK_IDENT", r"[a-zA-Z_][a-zA-Z0-9_]*"),
]

# =====================================================================
# Estructuras de Datos del Compilador
# =====================================================================

class Token:
    def __init__(self, type_: str, value: str, line: int, col: int, original_value: Optional[str] = None, correction_source: Optional[str] = None):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col
        self.original_value = original_value  # Si fue corregido, guarda el original
        self.correction_source = correction_source  # 'SequenceMatcher' o 'IA Fallback'

    def __repr__(self):
        corr_info = f" (corregido de '{self.original_value}' via {self.correction_source})" if self.original_value else ""
        return f"Token({self.type}, '{self.value}', L:{self.line}, C:{self.col}){corr_info}"

# =====================================================================
# 2. Mecanismos Hibridos y Fallback de IA
# =====================================================================

# Lista global para registrar sugerencias y correcciones para la salida final
AI_SUGGESTIONS = []

def registrar_sugerencia(fuente: str, detalle: str):
    AI_SUGGESTIONS.append(f"[{fuente}] {detalle}")

def fallback_ia(token_text: str, contexto: str) -> Tuple[str, str]:
    """
    Simula una consulta estructurada a un LLM para corregir tokens mal escritos
    o desconocidos en el contexto del codigo fuente de UnegScript.
    """
    token_lower = token_text.lower()
    
    # Caso comun prnt/prnt -> print
    if token_lower in ["prnt", "pront", "prn", "printf", "println"]:
        registrar_sugerencia("IA Fallback", f"Token desconocido '{token_text}' corregido a 'print' basado en contexto de funcion.")
        return "print", "TK_IDENT"
    
    # Intentar corregir palabras clave comunes
    correcciones = {
        "iff": ("if", "TK_IF"),
        "els": ("else", "TK_ELSE"),
        "ret": ("return", "TK_RETURN"),
        "fn_": ("fn", "TK_FN"),
        "lett": ("let", "TK_LET"),
    }
    
    if token_lower in correcciones:
        corr_val, corr_tok = correcciones[token_lower]
        registrar_sugerencia("IA Fallback", f"Token desconocido '{token_text}' corregido a palabra clave '{corr_val}'.")
        return corr_val, corr_tok
        
    # Si no puede deducir nada, lo reporta como identificador generico o error
    registrar_sugerencia("IA Fallback", f"No se pudo clasificar con alta certeza el token '{token_text}'. Se asume Identificador.")
    return token_text, "TK_IDENT"

def analizar_similitud_hibrida(token_text: str, line: int, col: int) -> Token:
    """
    Usa difflib.SequenceMatcher para comparar con el vocabulario base de UnegScript.
    Si la confianza >= 0.8, corrige automaticamente.
    Si la confianza < 0.8, activa el fallback de IA.
    """
    mejor_coincidencia = None
    mejor_ratio = 0.0
    
    for palabra_valida, tk_type in VOCABULARY.items():
        ratio = difflib.SequenceMatcher(None, token_text, palabra_valida).ratio()
        if ratio > mejor_ratio:
            mejor_ratio = ratio
            mejor_coincidencia = (palabra_valida, tk_type)
            
    if mejor_ratio >= 0.8:
        corr_val, corr_tok = mejor_coincidencia
        registrar_sugerencia(
            "SequenceMatcher", 
            f"Similitud alta ({mejor_ratio:.2f}) para '{token_text}'. Corregido a '{corr_val}'."
        )
        return Token(corr_tok, corr_val, line, col, original_value=token_text, correction_source="SequenceMatcher")
    else:
        # Activar fallback de IA debido a confianza baja
        corr_val, corr_tok = fallback_ia(token_text, f"Linea {line}, Columna {col}")
        return Token(corr_tok, corr_val, line, col, original_value=token_text, correction_source="IA Fallback")

# =====================================================================
# 3. Analizador Lexico (Lexer)
# =====================================================================

class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens: List[Token] = []
        
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.code):
            match_found = False
            for name, pattern in TOKEN_PATTERNS:
                regex = re.compile(pattern)
                match = regex.match(self.code, self.pos)
                if match:
                    text = match.group(0)
                    match_found = True
                    
                    if name == "COMMENT":
                        # Ignorar comentarios
                        self._actualizar_posicion(text)
                        break
                    elif name == "WS":
                        # Ignorar espacios en blanco
                        self._actualizar_posicion(text)
                        break
                    elif name == "NEWLINE":
                        self.line += 1
                        self.col = 1
                        self.pos += len(text)
                        break
                        
                    # Procesar tokens normales
                    t_line, t_col = self.line, self.col
                    self._actualizar_posicion(text)
                    
                    if name == "TK_IDENT":
                        # Verificar si es palabra clave exacta
                        if text in VOCABULARY:
                            self.tokens.append(Token(VOCABULARY[text], text, t_line, t_col))
                        else:
                            # Si es un identificador, validar si puede ser un error tipografico
                            # Para evitar corregir variables validas simples (ej. 'x'), solo analizamos
                            # palabras de longitud > 2 que no esten registradas o que se parezcan a built-ins/keywords.
                            es_posible_error = (
                                text not in ["x", "y", "z", "a", "b", "c"] and 
                                any(difflib.SequenceMatcher(None, text, kw).ratio() >= 0.6 for kw in VOCABULARY)
                            )
                            if es_posible_error and text not in VOCABULARY:
                                token_corregido = analizar_similitud_hibrida(text, t_line, t_col)
                                self.tokens.append(token_corregido)
                            else:
                                self.tokens.append(Token("TK_IDENT", text, t_line, t_col))
                    else:
                        # Remover comillas de literales de cadena
                        val = text
                        if name == "TK_LIT_STR":
                            val = text[1:-1]
                        self.tokens.append(Token(name, val, t_line, t_col))
                    break
            
            if not match_found:
                # Caracter desconocido / Error lexico. Activar recuperacion hibrida.
                caracter_invalido = self.code[self.pos]
                t_line, t_col = self.line, self.col
                self.pos += 1
                self.col += 1
                
                # Intentamos usar la IA para inferir este error lexico
                token_corregido = analizar_similitud_hibrida(caracter_invalido, t_line, t_col)
                self.tokens.append(token_corregido)
                
        self.tokens.append(Token("TK_EOF", "", self.line, self.col))
        return self.tokens

    def _actualizar_posicion(self, text: str):
        for char in text:
            if char == '\n':
                self.line += 1
                self.col = 1
            elif char != '\r':
                self.col += 1
        self.pos += len(text)

# =====================================================================
# 4. Arbol de Sintaxis Abstracta (AST)
# =====================================================================

class ASTNode:
    def repr_tree(self, indent: int = 0) -> str:
        raise NotImplementedError()

class ProgramNode(ASTNode):
    def __init__(self, statements: List[ASTNode]):
        self.statements = statements
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        res = f"{space}ProgramNode\n"
        for stmt in self.statements:
            res += stmt.repr_tree(indent + 1)
        return res

class AssignNode(ASTNode):
    def __init__(self, name: str, value: ASTNode):
        self.name = name
        self.value = value
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        res = f"{space}AssignNode(name='{self.name}')\n"
        res += self.value.repr_tree(indent + 1)
        return res

class BinOpNode(ASTNode):
    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        res = f"{space}BinOpNode(op='{self.op}')\n"
        res += self.left.repr_tree(indent + 1)
        res += self.right.repr_tree(indent + 1)
        return res

class IfNode(ASTNode):
    def __init__(self, condition: ASTNode, then_branch: ASTNode, else_branch: Optional[ASTNode] = None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        res = f"{space}IfNode\n"
        res += f"{space}  Condition:\n" + self.condition.repr_tree(indent + 2)
        res += f"{space}  Then:\n" + self.then_branch.repr_tree(indent + 2)
        if self.else_branch:
            res += f"{space}  Else:\n" + self.else_branch.repr_tree(indent + 2)
        return res

class CallNode(ASTNode):
    def __init__(self, func_name: str, args: List[ASTNode]):
        self.func_name = func_name
        self.args = args
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        res = f"{space}CallNode(func='{self.func_name}')\n"
        for arg in self.args:
            res += arg.repr_tree(indent + 1)
        return res

class LiteralNode(ASTNode):
    def __init__(self, value: Any, type_: str):
        self.value = value
        self.type = type_
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        return f"{space}LiteralNode(value={repr(self.value)}, type='{self.type}')\n"

class IdentifierNode(ASTNode):
    def __init__(self, name: str):
        self.name = name
        
    def repr_tree(self, indent: int = 0) -> str:
        space = "  " * indent
        return f"{space}IdentifierNode(name='{self.name}')\n"

# =====================================================================
# 5. Analizador Sintactico (Parser)
# =====================================================================

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        
    def peek(self) -> Token:
        return self.tokens[self.pos]
        
    def consume(self, expected_type: str = None) -> Token:
        tok = self.peek()
        if expected_type and tok.type != expected_type:
            # Error sintactico. Sugerir correccion usando IA y continuar.
            registrar_sugerencia(
                "Parser Error Recovery", 
                f"L:{tok.line}, C:{tok.col} -> Se esperaba token '{expected_type}', pero se obtuvo '{tok.type}' ('{tok.value}')."
            )
            # Retornar un token ficticio del tipo esperado para no detener la compilacion
            return Token(expected_type, f"<auto_gen_{expected_type.lower()}>", tok.line, tok.col)
        self.pos += 1
        return tok

    def parse(self) -> ProgramNode:
        statements = []
        while self.peek().type != "TK_EOF":
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return ProgramNode(statements)

    def parse_statement(self) -> Optional[ASTNode]:
        tok = self.peek()
        
        # Declaracion 'if'
        if tok.type == "TK_IF":
            return self.parse_if()
            
        # Asignacion o Llamada a funcion (identificadores)
        elif tok.type == "TK_IDENT":
            # Guardamos la posicion para mirar adelante
            next_tok = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            
            if next_tok and next_tok.type == "TK_ASSIGN":
                return self.parse_assignment()
            else:
                expr = self.parse_expression()
                # Opcionalmente consumir punto y coma
                if self.peek().type == "TK_SEMI":
                    self.consume("TK_SEMI")
                return expr
        
        elif tok.type == "TK_SEMI":
            self.consume("TK_SEMI")
            return None
            
        else:
            # Fallback para continuar parseando ante tokens inesperados
            err_tok = self.consume()
            registrar_sugerencia("Parser Error Recovery", f"Se omitio token no esperado en sentencia: '{err_tok.value}' ({err_tok.type})")
            return None

    def parse_assignment(self) -> AssignNode:
        name_tok = self.consume("TK_IDENT")
        self.consume("TK_ASSIGN")
        expr = self.parse_expression()
        if self.peek().type == "TK_SEMI":
            self.consume("TK_SEMI")
        return AssignNode(name_tok.value, expr)

    def parse_if(self) -> IfNode:
        self.consume("TK_IF")
        condition = self.parse_expression()
        
        # El cuerpo del then
        then_branch = self.parse_statement()
        
        else_branch = None
        if self.peek().type == "TK_ELSE":
            self.consume("TK_ELSE")
            else_branch = self.parse_statement()
            
        return IfNode(condition, then_branch, else_branch)

    def parse_expression(self) -> ASTNode:
        # Parseamos expresion binaria simple o primaria
        left = self.parse_primary()
        
        op_tok = self.peek()
        if op_tok.type in ["TK_GT", "TK_LT", "TK_EQ", "TK_NE", "TK_PLUS", "TK_MINUS", "TK_MUL", "TK_DIV"]:
            self.consume()
            right = self.parse_expression()
            return BinOpNode(left, op_tok.value, right)
            
        return left

    def parse_primary(self) -> ASTNode:
        tok = self.peek()
        
        if tok.type == "TK_LIT_INT":
            self.consume()
            return LiteralNode(int(tok.value), "Int")
        elif tok.type == "TK_LIT_FLOAT":
            self.consume()
            return LiteralNode(float(tok.value), "Float")
        elif tok.type == "TK_LIT_STR":
            self.consume()
            return LiteralNode(tok.value, "String")
        elif tok.type in ["TK_TRUE", "TK_FALSE"]:
            self.consume()
            return LiteralNode(tok.value == "true", "Bool")
        elif tok.type == "TK_IDENT":
            # Podria ser un identificador simple o una llamada a funcion
            ident_tok = self.consume("TK_IDENT")
            if self.peek().type == "TK_LPAREN":
                self.consume("TK_LPAREN")
                args = []
                if self.peek().type != "TK_RPAREN":
                    args.append(self.parse_expression())
                    while self.peek().type == "TK_COMMA":
                        self.consume("TK_COMMA")
                        args.append(self.parse_expression())
                self.consume("TK_RPAREN")
                return CallNode(ident_tok.value, args)
            return IdentifierNode(ident_tok.value)
        else:
            # Error sintactico en expresion primaria
            registrar_sugerencia("Parser Error Recovery", f"Expresion primaria invalida: se obtuvo '{tok.value}' ({tok.type})")
            self.consume()
            return LiteralNode(None, "Error")

# =====================================================================
# 6. Ejecucion y Salida Estetica
# =====================================================================

def main():
    codigo_entrada = 'pront x=5; if x>3 prnt(x) else prnt("no")'
    
    print("\n" + "=" * 80)
    print(" ASISTENTE DE COMPILACION HIBRIDO DE UNEGSCRIPT ".center(80, "#"))
    print("=" * 80)
    
    print(f"\nCodigo de Entrada:\n  {codigo_entrada}\n")
    
    # 1. Fase de Lexer Hibrido
    lexer = Lexer(codigo_entrada)
    tokens = lexer.tokenize()
    
    print("-" * 80)
    print(f"{'TOKEN':<25} {'LEXEMA':<25} {'LINEA':<10} {'COLUMNA':<10}")
    print("-" * 80)
    for tok in tokens:
        if tok.type == "TK_EOF":
            continue
        token_str = tok.type
        lexema_str = tok.value
        if tok.original_value:
            lexema_str = f"{tok.original_value} -> {tok.value}"
        print(f"{token_str:<25} {lexema_str:<25} {tok.line:<10} {tok.col:<10}")
    print("-" * 80)
    
    # 2. Fase de Parser & Recuperacion
    parser = Parser(tokens)
    ast = parser.parse()
    
    print("\n" + " ARBOL DE SINTAXIS ABSTRACTA (AST) ".center(80, "-"))
    print(ast.repr_tree())
    print("-" * 80)
    
    # 3. Mostrar sugerencias y correcciones de IA / SequenceMatcher
    print("\n" + " SUGERENCIAS DE LA IA & CORRECCIONES ".center(80, "-"))
    if AI_SUGGESTIONS:
        for idx, sug in enumerate(AI_SUGGESTIONS, 1):
            print(f"  {idx}. {sug}")
    else:
        print("  Ninguna sugerencia o correccion fue necesaria.")
    print("-" * 80 + "\n")

if __name__ == "__main__":
    main()
