
## 📝 Especificación Sintáctica (EBNF)

A continuación, se detalla la documentación formal de las estructuras de control (subprogramas, bucles y condicionales) utilizadas exactamente en el código fuente de Rust, empleando la notación **EBNF (Extended Backus-Naur Form)** para describir la jerarquía sintáctica construida.


 ###  DEFINICIONES DE SUBPROGRAMAS
```
subprograma_collatz    ::= "fn collatz(mut num: u64) -> u64" , bloque_collatz ;
subprograma_pedir      ::= "fn pedir_numero() -> u64" , bloque_pedir ;
subprograma_main       ::= "fn main()" , bloque_main ;
```

 ###  ESTRUCTURAS CÍCLICAS (BUCLES)
```   
bucle_while_collatz    ::= "while num > 1" , bloque_while ;
bucle_loop_pedir       ::= "loop" , bloque_loop ;
bucle_for_main         ::= "for i in 1..n" , bloque_for ;
```

###   ESTRUCTURAS CONDICIONALES
```
condicional_if_collatz ::= "if num % 2 == 0" , bloque_if_par , [ "else" , bloque_else_impar ] ;
estructura_match_pedir ::= "match input.trim().parse::<u64>()" , bloque_match ;
```

###   BLOQUES DE CÓDIGO DEL PROGRAMA
```
bloque_collatz         ::= "{" , "let mut pasos = 0;" , bucle_while_collatz , "pasos" , "}" ;
bloque_while           ::= "{" , condicional_if_collatz , "pasos += 1;" , "}" ;
bloque_if_par          ::= "{" , "num /= 2;" , "}" ;
bloque_else_impar      ::= "{" , "num = 3 * num + 1;" , "}" ;

bloque_pedir           ::= "{" , bucle_loop_pedir , "}" ;
bloque_loop            ::= "{" , "print!(...);" , "io::stdout().flush().unwrap();" , "let mut input = String::new();" , "io::stdin().read_line(&mut input).unwrap();" , estructura_match_pedir , "}" ;
bloque_match           ::= "{" , "Ok(n) if n > 50 => return n," , "Ok(_) => println!(...)," , "Err(_) => println!(...)," , "}" ;

bloque_main            ::= "{" , "let n = pedir_numero();" , "let tiempo_inicio = Instant::now();" , "let mut pasos_totales = 0;" , bucle_for_main , "black_box(pasos_totales);" , "let tiempo_fin = tiempo_inicio.elapsed();" , "println!(...);" , "println!(...);" , "}" ;
bloque_for             ::= "{" , "pasos_totales += collatz(i);" , "}" ;
```
