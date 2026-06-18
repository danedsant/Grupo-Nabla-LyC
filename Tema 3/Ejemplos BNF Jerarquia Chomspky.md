# 📝 Ejemplos en Formato BNF de la Jerarquia de Chompsky

## Ejemplo Gramatica Tipo 3 (Regulares): Identificador
```
<identificador> ::= <letra> | <letra> <resto>
<resto>         ::= <letra> <resto> | <digito> <resto> | <letra> | <digito>
<letra>         ::= "a" | "b" | "c"
<digito>        ::= "0" | "1" | "2"
```
___
## Ejemplo Gramatica Tipo 2 (Libres de Contexto): Operaciones Aritmeticas Basicas
```
<expr>     ::= <expr> "+" <termino> | <termino>
<termino>  ::= <termino> "*" <factor> | <factor>
<factor>   ::= "(" <expr> ")" | <numero>
<numero>   ::= "1" | "2" | "3"
```
___
## Ejemplo Gramatica Tipo 1 (Sensibles al Contexto):
```
<letra_a> <B> <letra_c> ::= <letra_a> "b" <letra_c>
```
___
## Ejemplo Tipo 0 (Irrestrictas):
```
<A> <B> "1" ::= <C> "0" <A>
<C> ::= <vacio>
```