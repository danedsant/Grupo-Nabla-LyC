// Grupo Nabla
// Conjetura de Collatz en JavaScript 
// para todos los números menores a N, con N ingresado por el usuario

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function collatz(num) {
    let pasos = 0;

    while (num > 1) {
        if (num % 2 === 0) {
            num /= 2;
        } else {
            num = 3 * num + 1;
        }
        pasos++;
    }

    return pasos;
}

function pedirNumero() {

    return new Promise((resolve) => {

        rl.question('Ingresa un número entero positivo: ', (respuesta) => {
            
            if (isNaN(respuesta) || parseInt(respuesta) <= 50) {
                console.log(isNaN(respuesta) ? 'Error: ingresar un número valido.' : 'Error: El numero debe ser mayor a 50.');
                resolve(pedirNumero());
                
            } else {
                resolve(respuesta);

            }
        });
    });
}

async function ejecutar() {

    const intN = parseInt(await pedirNumero());
    
    const tiempo_inicio = performance.now();
    
    let pasos_totales = 0;

    for (let i = 1; i < intN; i++) {
        pasos_totales += collatz(i);
    }

    const tiempo_fin = performance.now();

    console.log(`Pasos totales calculados: ${pasos_totales}`);
    console.log(`Tiempo: ${(tiempo_fin - tiempo_inicio).toFixed(4)} ms`);
    
    rl.close();
}

ejecutar();