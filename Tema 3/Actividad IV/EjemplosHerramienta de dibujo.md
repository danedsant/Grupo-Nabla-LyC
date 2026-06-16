### Ejemplos de Herramienta de dibujo

1. **Ejemplo:** El Cubo (Proyección Tridimensional sobre Plano 2D)

- **Objetivo:** Representar un hexaedro regular aplicando desplazamiento lineal simétrico para superponer dos caras cuadradas interconectadas por aristas oblicuas o de profundidad.

- **Cadena resultante esperada:** acacacacgcacaaacatcacagcacacaacatcaca

**Proceso de Derivación Formal:**

S → acacacacC1 (Aplicando Regla 1) 
→ acacacac(gcacaaacatC2) (Aplicando Regla 4: C1 → gcacaaacatC2) 
→ acacacacgcacaaacat(cacagcacacaacatC3) (Aplicando Regla 5:  C2 → cacagcacacaacatC3)  
→ acacacacgcacaaacatcacagcacacaacat(caca) (Aplicando Regla 6:  C3 → caca) 
→ acacacacgcacaaacatcacagcacacaacatcaca (Cadena terminal validada)

### Árbol de Análisis Sintáctico: 

<img width="535" height="251" alt="image" src="https://github.com/user-attachments/assets/0a357527-ca99-4734-8c4e-88a1f4695e5b" />

**Mecanismo de Ejecución Gráfica:** Ejecuta la secuencia inicial acacacac para constituir por completo el cuadrado bidimensional frontal. En vértices clave específicos, el terminal g congela la coordenada bidimensional y efectúa un desfase geométrico para trazar las líneas de profundidad y estructurar el cuadrado posterior. Con la terminal t se recupera el nodo original eliminando la necesidad de trazar líneas repetidas sobre los mismos ejes. Finalmente, las terminales c y a se utilizan para completar las caras restantes del cubo, asegurando que cada vértice y arista se conecte correctamente para formar la figura tridimensional proyectada.

**2. Ejemplo:** La Escalera Uniforme (Caso Adicional Libres)

- Objetivo: Construir una secuencia continua simétrica de peldaños idénticos en dirección diagonal.
- Cadena resultante esperada: acacacacacacac

**Proceso de Derivación Formal:**

S → acacacacC (Aplicando Regla 1) 
→ acacacac(caca) (Derivación directa simplificada bajo sustitución de subconjunto de terminales)
→ acacacacacacac (Cadena terminal alcanzada)

**Mecanismo de Ejecución Gráfica:** Alterna de forma iterativa y secuencial pasos de avance vertical (a), rotación angular orientativa (c), y avance horizontal (a), generando una figura de peldaños en serie perfectamente balanceada. 
