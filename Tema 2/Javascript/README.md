## 📝 Especificación Sintáctica (EBNF)

A continuación, se detalla la documentación formal de las estructuras de control (subprogramas, bucles y condicionales) utilizadas exactamente en el código fuente de Python, empleando la notación **EBNF (Extended Backus-Naur Form)** para describir la jerarquía sintáctica construida.

<pre>
(* ==========================================
   DEFINICIONES DE SUBPROGRAMAS
   ========================================== *)
subprograma_collatz    ::= "def collatz(num):" , bloque_collatz ;
subprograma_pedir      ::= "def pedir_numero():" , bloque_pedir ;
subprograma_ejecutar   ::= "def ejecutar():" , bloque_ejecutar ;
condicional_principal  ::= "if __name__ == '__main__':" , bloque_principal ;

(* ==========================================
   ESTRUCTURAS CÍCLICAS (BUCLES)
   ========================================== *)
bucle_while_collatz    ::= "while num > 1:" , bloque_while_c ;
bucle_while_pedir      ::= "while True:" , bloque_while_p ;
bucle_for_ejecutar     ::= "for i in range(1, n):" , bloque_for ;

(* ==========================================
   ESTRUCTURAS CONDICIONALES
   ========================================== *)
condicional_if_collatz ::= "if num % 2 == 0:" , bloque_if_par , [ "else:" , bloque_else_impar ] ;
condicional_if_pedir   ::= "if n <= 50:" , bloque_if_error , [ "else:" , bloque_else_valido ] ;
estructura_try_except  ::= "try:" , bloque_try , "except ValueError:" , bloque_except ;

(* ==========================================
   BLOQUES DE CÓDIGO DEL PROGRAMA
   ========================================== *)
bloque_collatz         ::= "pasos = 0" , bucle_while_collatz , "return pasos" ;
bloque_while_c         ::= condicional_if_collatz , "pasos += 1" ;
bloque_if_par          ::= "num //= 2" ;
bloque_else_impar      ::= "num = 3 * num + 1" ;

bloque_pedir           ::= bucle_while_pedir ;
bloque_while_p         ::= 'respuesta = input("Ingresa un numero entero positivo mayor a 50: ")' , estructura_try_except ;
bloque_try             ::= "n = int(respuesta)" , condicional_if_pedir ;
bloque_if_error        ::= 'print("Error, el numero debe ser mayor a 50.")' ;
bloque_else_valido     ::= "return n" ;
bloque_except          ::= 'print("Error, ingresa un numero entero valido mayor a 50")' ;

bloque_ejecutar        ::= "n = pedir_numero()" , "tiempo_inicio = time.perf_counter()" , "pasos_totales = 0" , bucle_for_ejecutar , "tiempo_fin = time.perf_counter()" , "print(...);" , "print(...);" ;
bloque_for             ::= "pasos_totales += collatz(i)" ;

bloque_principal       ::= "ejecutar()" ;
</pre>
