# Actividad 4: Aplicación de Metacompiladores (FLEX) en Seguridad Informática

Este módulo del repositorio contiene la documentación, el análisis teórico y la propuesta de diseño para la **Actividad 4** de la asignatura **Lenguajes y Compiladores** (Sección 01) en la **Universidad Nacional Experimental de Guayana (UNEG)**.

---

## 📌 Contexto del Caso de Estudio: Reglas de Snort (IDS/IPS)

El análisis de tráfico y la detección de amenazas en redes de computadoras exigen un rendimiento crítico en tiempo real. Para resolver este desafío, los Sistemas de Detección/Prevención de Intrusos (IDS/IPS) como **Snort** emplean un lenguaje específico basado en firmas (reglas).

Dado que un sensor de seguridad puede verse expuesto a procesar miles de paquetes por segundo bajo extensos conjuntos de firmas, la fase de **análisis léxico** (tokenización) debe ser extremadamente eficiente. En este escenario, la herramienta de metacompilación **FLEX** es idónea para generar tokenizadores basados en Autómatas Finitos Determinísticos (AFD) optimizados en lenguaje C.

---

## 📊 Propuesta de Tokenización

Tomando como base una firma estándar de detección de intrusiones en Snort:

```text
alert tcp $EXTERNAL_NET any ->$HOME_NET 80 (msg:"Intrusión Web"; sid:100001;)
