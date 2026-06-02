// Grupo Nabla
// Conjetura de Collatz en Rust
// para todos los números menores a N, con N ingresado por el usuario

use std::io::{self, Write};
use std::time::Instant;
use std::hint::black_box;

fn collatz(mut num: u64) -> u64 {
    let mut pasos = 0;
    while num > 1 {
        if num % 2 == 0 {
            num /= 2;
        } else {
            num = 3 * num + 1;
        }
        pasos += 1;
    }
    pasos
}

fn pedir_numero() -> u64 {
    loop {
        print!("Ingresa un numero entero positivo mayor a 50: ");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u64>() {
            Ok(n) if n > 50 => return n,
            Ok(_) => println!("Error, el numero debe ser mayor a 50."),
            Err(_) => println!("Error, ingresa un numero valido."),
        }
    }
}

fn main() {
    let n = pedir_numero();

    let tiempo_inicio = Instant::now();
    let mut pasos_totales = 0;
    
    for i in 1..n { 
        pasos_totales += collatz(i);
    }
    
    // Evita que el compilador LLVM optimice la variable
    black_box(pasos_totales);
    
    let tiempo_fin = tiempo_inicio.elapsed();

    println!("Pasos totales calculados: {}", pasos_totales);
    println!("Tiempo: {:.4} ms", tiempo_fin.as_secs_f64() * 1000.0);
}