import re

# =====================================================================
# 1. ANALIZADOR LÉXICO (LEXER COMÚN)
# =====================================================================
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokenize(code):
    tokens = []
    token_specification = [
        ('NUM',      r'\d+'),
        ('PLUS',     r'\+'),
        ('MUL',      r'\*'),
        ('SKIP',     r'[ \t\n]+'),
        ('MISMATCH', r'.'),
    ]
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUM':
            tokens.append(Token('NUM', int(value)))
        elif kind == 'PLUS':
            tokens.append(Token('PLUS', '+'))
        elif kind == 'MUL':
            tokens.append(Token('MUL', '*'))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Error Léxico: Carácter no reconocido '{value}'")
    tokens.append(Token('EOF', '$'))
    return tokens

# =====================================================================
# 2. IMPLEMENTACIÓN ANALIZADOR SINTÁCTICO LL(1) (Descendente)
# =====================================================================
class LL1Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.pos += 1
            self.current_token = self.tokens[self.pos]
        else:
            raise SyntaxError(f"Error Sintáctico LL: Se esperaba {token_type}, se recibió {self.current_token.type}")

    def parse(self):
        ast = self.E()
        if self.current_token.type != 'EOF':
            raise SyntaxError("Error Sintáctico LL: Entrada no consumida totalmente.")
        return ast

    def E(self):
        # E -> T E'
        node_t = self.T()
        return self.E_prime(node_t)

    def E_prime(self, left):
        # E' -> + T E' | ε
        if self.current_token.type == 'PLUS':
            self.consume('PLUS')
            right = self.T()
            node = ('+', left, right)
            return self.E_prime(node)
        return left

    def T(self):
        # T -> F T'
        node_f = self.F()
        return self.T_prime(node_f)

    def T_prime(self, left):
        # T' -> * F T' | ε
        if self.current_token.type == 'MUL':
            self.consume('MUL')
            right = self.F()
            node = ('*', left, right)
            return self.T_prime(node)
        return left

    def F(self):
        # F -> num
        if self.current_token.type == 'NUM':
            val = self.current_token.value
            self.consume('NUM')
            return val
        else:
            raise SyntaxError(f"Error Sintáctico LL: Se esperaba NUM, se recibió {self.current_token.type}")

# =====================================================================
# 3. IMPLEMENTACIÓN ANALIZADOR SINTÁCTICO LR (Ascendente / Shift-Reduce)
# =====================================================================
class LRParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = [0]
        self.val_stack = []
        self.pos = 0

    def parse(self):
        action_table = {
            0: {'NUM': 'S4'},
            1: {'PLUS': 'S5', 'EOF': 'ACC'},
            2: {'PLUS': 'R2', 'MUL': 'S6', 'EOF': 'R2'},
            3: {'PLUS': 'R4', 'MUL': 'R4', 'EOF': 'R4'},
            4: {'PLUS': 'R5', 'MUL': 'R5', 'EOF': 'R5'},
            5: {'NUM': 'S4'},
            6: {'NUM': 'S4'},
            7: {'PLUS': 'R1', 'MUL': 'S6', 'EOF': 'R1'},
            8: {'PLUS': 'R3', 'MUL': 'R3', 'EOF': 'R3'},
        }

        goto_table = {
            0: {'E': 1, 'T': 2, 'F': 3},
            5: {'T': 7, 'F': 3},
            6: {'F': 8},
        }

        while True:
            state = self.stack[-1]
            lookahead = self.tokens[self.pos].type
            action = action_table.get(state, {}).get(lookahead)

            if not action:
                raise SyntaxError(f"Error Sintáctico LR: Token no esperado '{self.tokens[self.pos]}'")

            if action == 'ACC':
                return self.val_stack[-1]

            elif action.startswith('S'):
                next_state = int(action[1:])
                self.stack.append(next_state)
                self.val_stack.append(self.tokens[self.pos].value)
                self.pos += 1

            elif action.startswith('R'):
                rule = int(action[1:])
                if rule == 1:   # E -> E + T
                    right = self.val_stack.pop()
                    self.val_stack.pop() # '+'
                    left = self.val_stack.pop()
                    self.val_stack.append(('+', left, right))
                    pop_count = 3
                    non_terminal = 'E'
                elif rule == 2: # E -> T
                    pop_count = 1
                    non_terminal = 'E'
                elif rule == 3: # T -> T * F
                    right = self.val_stack.pop()
                    self.val_stack.pop() # '*'
                    left = self.val_stack.pop()
                    self.val_stack.append(('*', left, right))
                    pop_count = 3
                    non_terminal = 'T'
                elif rule == 4: # T -> F
                    pop_count = 1
                    non_terminal = 'T'
                elif rule == 5: # F -> num
                    pop_count = 1
                    non_terminal = 'F'

                for _ in range(pop_count):
                    self.stack.pop()

                top_state = self.stack[-1]
                self.stack.append(goto_table[top_state][non_terminal])

# =====================================================================
# PRUEBA Y SALIDA
# =====================================================================
if __name__ == "__main__":
    entrada = "3 + 5 * 2"
    tokens = tokenize(entrada)

    print(f"Entrada analizada: '{entrada}'")
    
    parser_ll = LL1Parser(tokens)
    print("AST Generado por LL(1):", parser_ll.parse())

    parser_lr = LRParser(tokens)
    print("AST Generado por LR:   ", parser_lr.parse())