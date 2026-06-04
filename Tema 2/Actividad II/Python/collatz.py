import time

def collatz(num):
    pasos = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        pasos += 1
    return pasos

def pedir_numero():
    while True:
        respuesta = input("Ingresa un numero entero positivo mayor a 50: ")
        try:
            n = int(respuesta)
            if n <= 50:
                print("Error, el numero debe ser mayor a 50.")
            else:
                return n
        except ValueError:
            print("Error, ingresa un numero entero valido mayor a 50")

def ejecutar():
    n = pedir_numero()
    
    tiempo_inicio = time.perf_counter()
    pasos_totales = 0
    
    for i in range(1, n):
        pasos_totales += collatz(i)
        
    tiempo_fin = time.perf_counter()
    
    print(f"Pasos totales calculados: {pasos_totales}")
    print(f"Tiempo: {(tiempo_fin - tiempo_inicio) * 1000:.4f} ms")

if __name__ == "__main__":
    ejecutar()