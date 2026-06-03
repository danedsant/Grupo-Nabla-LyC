## 📝 Especificación Sintáctica (EBNF) - Versión Python

A continuación se detalla la documentación formal de las estructuras de control (subprogramas, bucles y condicionales) utilizadas exactamente en el código fuente de Python, empleando la notación **EBNF (Extended Backus-Naur Form)**.


###   DEFINICIONES DE SUBPROGRAMAS
```
subprograma_collatz    ::= "function collatz(num)" , bloque_collatz ;
subprograma_pedir      ::= "function pedirNumero()" , bloque_pedir ;
subprograma_ejecutar   ::= "async function ejecutar()" , bloque_ejecutar ;
```

###   ESTRUCTURAS CÍCLICAS (BUCLES)
 ``` 
bucle_while_collatz    ::= "while (num > 1)" , bloque_while_c ;
bucle_for_ejecutar     ::= "for (let i = 1; i < intN; i++)" , bloque_for ;
```

###   ESTRUCTURAS CONDICIONALES
``` 
condicional_if_collatz ::= "if (num % 2 === 0)" , bloque_if_par , [ "else" , bloque_else_impar ] ;
condicional_if_pedir   ::= "if (isNaN(respuesta) || parseInt(respuesta) <= 50)" , bloque_if_error , [ "else" , bloque_else_valido ] ;
```
### BLOQUES DE CÓDIGO DEL PROGRAMA (DELIMITADORES DE BLOQUE)
``` 
bloque_collatz         ::= "{" , "let pasos = 0;" , bucle_while_collatz , "return pasos;" , "}" ;
bloque_while_c         ::= "{" , condicional_if_collatz , "pasos++" , "}" ;
bloque_if_par          ::= "{" , "num /= 2;" , "}" ;
bloque_else_impar      ::= "{" , "num = 3 * num + 1;" , "}" ;

bloque_pedir           ::= "{" , "return new Promise((resolve) => {" , "rl.question('Ingresa un número entero positivo: ', (respuesta) => {" , condicional_if_pedir , "});" , "});" , "}" ;
bloque_if_error        ::= "{" , "console.log(isNaN(respuesta) ? 'Error...' : 'Error...');" , "resolve(pedirNumero());" , "}" ;
bloque_else_valido     ::= "{" , "resolve(respuesta);" , "}" ;

bloque_ejecutar        ::= "{" , "const intN = parseInt(await pedirNumero());" , "const tiempo_inicio = performance.now();" , "let pasos_totales = 0;" , bucle_for_ejecutar , "const tiempo_fin = performance.now();" , "console.log(...);" , "rl.close();" , "}" ;

bloque_for             ::= "{" , "pasos_totales += collatz(i);" , "}" ;
```
