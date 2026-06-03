# 📚 Tema 2: Los Lenguajes de Programacion


## Benchmarking de Conjetura de Collatz

La conjetura establece que para cualquier numero entero positivo **N**, eventualmente siempre llegaremos a 1 si aplicamos repetidamente las siguientes operaciones:


>1) Si el número es **par**, se divide entre 2

>2) Si el número es **impar**, se multiplica por 3 y se le suma 1.

El programa no debe evaluar un unico valor, sino que debe calcular de forma iterativa y continua los pasos requeridos para todos los numeros estrictamente menores al **N** ingresado por el usuario, donde **N > 50**

## Estructura
```
├── python/
│   └── collatz.py
├── javascript/
│   └── collatz.js
├── rust/
│   └── src/
│       └── main.rs
├── zig/
│   └── collatz.zig
└── README.md
```

## Dependencias

Para ejecutar los siguientes lenguajes se pueden instalar sus respectivas dependencias mediante `winget` en la terminal de windows basados en la siguiente tabla:

| Lenguaje | Dependencia | Comando de terminal|
| ----------- | ----------- | ----------- |
| **Python** | Python 3.14 | winget install python3
| **Javascript** | Node.js | winget install -e --id OpenJS.NodeJS
| **Zig** | Zig 0.13.0 | winget install zig.zig --version 0.13.0

### Para Rust:
| Lenguaje | Descarga | Observacion |
| ----------- | ----------| ----------|
| **Rust** | https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe | Para compilar y ejecutar el codigo de rust en windows es necesario personalizar la instalacion usando el **GNU ABI toolchain**, por lo que durante la instalacion via `rustup-init.exe` se debe cambiar el `default host triple` de `x86_64-pc-windows-msvc` a `x86_64-pc-windows-gnu` para una instalacion minima

> [!NOTE]
> La instalacion de las dependencias descritas añade automaticamente al PATH cada lenguaje respectivamente


## Ejecucion de los codigos

### Python
 - Abrir una terminal en la carpeta Python/
 - Ejecutar el siguiente comando:

 ```
python collatz.py
```

### Javascript
 - Abrir una terminal en la carpeta Javascript/
 - Ejecutar el siguiente comando:

 ```
node collatz.js
```

### Rust
 - Abrir una terminal en la carpeta Rust/
 - Ejecutar el siguiente comando:

 ```
cargo run --release
```

### Zig
 - Abrir una terminal en la carpeta Zig/
 - Ejecutar el siguiente comando:

 ```
zig run collatz.zig
```

## Especificaciones del entorno de prueba
| Item | Descripcion |
| ----------- | ----------- |
| Sistema Operativo | Windows 11 Pro  |
| CPU | Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (1.80 GHz) |
| Memoria RAM | 16 GB |

## Resultado del Benchmarking
| Lenguaje | Tiempo en ms |
| ----------- | ----------- |
| Rust | 5,1656 ms |
| Zig  | 5,6156 ms |
| Javascript | 21,6821 ms |
|Python | 660,3963 ms |

Al analizar estos resultados, ordenados de manera ascendente, podemos notar que indiscutiblemente Rust se posiciona como el ganador en esta ocasión, lo que evidencia y valida cómo las decisiones del diseño léxico y sintáctico en cada lenguaje impactan directamente en el rendimiento del hardware. Asimismo, es posible observar cómo la flexibilidad y velocidad de escritura que Python ofrece al desarrollador tiene un costo computacional severo: al carecer de tokens de tipado estricto, obliga a la máquina a inferir y validar dinámicamente, en cada iteración, si una variable es un entero antes de aplicar una operación matemática, sacrificando así la velocidad de procesamiento.
