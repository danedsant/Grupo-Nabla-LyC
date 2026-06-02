## 📝 Especificación Sintáctica (EBNF) - Versión Python

A continuación se detalla la documentación formal de las estructuras de control (subprogramas, bucles y condicionales) utilizadas exactamente en el código fuente de Python, empleando la notación **EBNF (Extended Backus-Naur Form)**.

<pre>
(* Definiciones de Subprogramas *)
&lt;subprograma_collatz&gt;     ::= "def collatz(num):" &lt;bloque_collatz&gt;
&lt;subprograma_pedir&gt;       ::= "def pedir_numero():" &lt;bloque_pedir&gt;
&lt;subprograma_ejecutar&gt;    ::= "def ejecutar():" &lt;bloque_ejecutar&gt;
&lt;condicional_principal&gt;   ::= "if __name__ == '__main__':" &lt;bloque_principal&gt;

(* Bucles *)
&lt;bucle_while_collatz&gt;     ::= "while num > 1:" &lt;bloque_while_c&gt;
&lt;bucle_while_pedir&gt;       ::= "while True:" &lt;bloque_while_p&gt;
&lt;bucle_for_ejecutar&gt;      ::= "for i in range(1, n):" &lt;bloque_for&gt;

(* Condicionales *)
&lt;condicional_if_collatz&gt;  ::= "if num % 2 == 0:" &lt;bloque_if_par&gt; "else:" &lt;bloque_else_impar&gt;
&lt;condicional_if_pedir&gt;    ::= "if n <= 50:" &lt;bloque_if_error&gt; "else:" &lt;bloque_else_valido&gt;
&lt;estructura_try_except&gt;   ::= "try:" &lt;bloque_try&gt; "except ValueError:" &lt;bloque_except&gt;

(* Bloques de Código del Programa (Indentación) *)
&lt;bloque_collatz&gt;          ::= "pasos = 0" &lt;bucle_while_collatz&gt; "return pasos"
&lt;bloque_while_c&gt;          ::= &lt;condicional_if_collatz&gt; "pasos += 1"
&lt;bloque_if_par&gt;           ::= "num //= 2"
&lt;bloque_else_impar&gt;       ::= "num = 3 * num + 1"

&lt;bloque_pedir&gt;            ::= &lt;bucle_while_pedir&gt;
&lt;bloque_while_p&gt;          ::= 'respuesta = input("Ingresa un numero entero positivo mayor a 50: ")' &lt;estructura_try_except&gt;
&lt;bloque_try&gt;              ::= "n = int(respuesta)" &lt;condicional_if_pedir&gt;
&lt;bloque_if_error&gt;         ::= 'print("Error, el numero debe ser mayor a 50.")'
&lt;bloque_else_valido&gt;      ::= "return n"
&lt;bloque_except&gt;           ::= 'print("Error, ingresa un numero entero valido mayor a 50")'

&lt;bloque_ejecutar&gt;         ::= "n = pedir_numero()" "tiempo_inicio = time.perf_counter()" "pasos_totales = 0" &lt;bucle_for_ejecutar&gt; "tiempo_fin = time.perf_counter()" 'print(f"Pasos totales calculados: {pasos_totales}")' 'print(f"Tiempo: {(tiempo_fin - tiempo_inicio) * 1000:.4f} ms")'
&lt;bloque_for&gt;              ::= "pasos_totales += collatz(i)"

&lt;bloque_principal&gt;         ::= "ejecutar()"
</pre>

