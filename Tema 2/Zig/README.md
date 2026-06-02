## 📝 Especificación Sintáctica (EBNF)

A continuación, se detalla la documentación formal de las estructuras de control (subprogramas, bucles y condicionales) utilizadas exactamente en el código fuente de Zig, empleando la notación **EBNF (Extended Backus-Naur Form)** para describir la jerarquía sintáctica construida.

```text
(* ==========================================
   DEFINICIONES DE SUBPROGRAMAS
   ========================================== *)
subprograma_collatz    ::= "fn collatz(start_num: u64) u64" , bloque_collatz ;
subprograma_pedir      ::= "fn pedirNumero(stdout: anytype) !u64" , bloque_pedir ;
subprograma_main       ::= "pub fn main() !void" , bloque_main ;

(* ==========================================
   ESTRUCTURAS CÍCLICAS (BUCLES)
   ========================================== *)
bucle_while_collatz    ::= "while (num > 1)" , bloque_while_c ;
bucle_while_pedir      ::= "while (true)" , bloque_while_p ;
bucle_for_main         ::= "for (1..n) |i|" , bloque_for ;

(* ==========================================
   ESTRUCTURAS CONDICIONALES
   ========================================== *)
condicional_if_collatz ::= "if (num % 2 == 0)" , bloque_if_par , [ "else" , bloque_else_impar ] ;
condicional_if_capture ::= "if (try stdin.readUntilDelimiterOrEof(...)) |user_input|" , bloque_capture ;
estructura_catch_pedir ::= "const n = std.fmt.parseInt(...)" , "catch" , bloque_catch ;
condicional_if_pedir   ::= "if (n <= 50)" , bloque_if_error , [ "else" , bloque_else_valido ] ;

(* ==========================================
   BLOQUES DE CÓDIGO DEL PROGRAMA
   ========================================== *)
bloque_collatz         ::= "{" , "var num = start_num;" , "var pasos: u64 = 0;" , bucle_while_collatz , "return pasos;" , "}" ;
bloque_while_c         ::= "{" , condicional_if_collatz , "pasos += 1;" , "}" ;
bloque_if_par          ::= "{" , "num /= 2;" , "}" ;
bloque_else_impar      ::= "{" , "num = 3 * num + 1;" , "}" ;

bloque_pedir           ::= "{" , "const stdin = std.io.getStdIn().reader();" , "var buf: [100]u8 = undefined;" , bucle_while_pedir , "}" ;
bloque_while_p         ::= "{" , "try stdout.print(...);" , condicional_if_capture , "}" ;
bloque_capture         ::= "{" , "const line = std.mem.trimRight(...);" , estructura_catch_pedir , condicional_if_pedir , "}" ;
bloque_catch           ::= "{" , "try stdout.print(...);" , "continue;" , "}" ;
bloque_if_error        ::= "{" , "try stdout.print(...);" , "}" ;
bloque_else_valido     ::= "{" , "return n;" , "}" ;

bloque_main            ::= "{" , "const stdout = std.io.getStdOut().writer();" , "const n = try pedirNumero(stdout);" , "var timer = try std.time.Timer.start();" , "var pasos_totales: u64 = 0;" , bucle_for_main , "const tiempo_ns = timer.read();" , "std.mem.doNotOptimizeAway(pasos_totales);" , "const tiempo_ms = ...;" , "try stdout.print(...);" , "try stdout.print(...);" , "}" ;
bloque_for             ::= "{" , "pasos_totales += collatz(i);" , "}" ;
```
