# Trabajo Práctico 1: Diseño de Calentador de Agua Eléctrico

## Objetivo
Diseñar un calentador de agua eléctrico portátil utilizando una resistencia de NICROM (aleación de Níquel y Cromo) y establecer sus parámetros básicos de funcionamiento.

## Parámetros de Diseño

### 1. Material (aislante) a emplear
Para el aislamiento térmico se utilizará una capa doble de fibra de vidrio de 2.5 mm, que permitirá minimizar las pérdidas de calor durante el funcionamiento del dispositivo.

### 2. Forma y capacidad del recipiente
- **Forma**: Cilíndrica
- **Dimensiones**: Diámetro de 8 cm, altura de 15 cm
- **Capacidad**: 750 ml (0.75 litros)

### 3. Propósito del calentador
Calentar agua para preparar mate, con una temperatura objetivo de 80°C.

### 4. Fluido a calentar
Agua potable.

### 5. Tiempo en el que se desea alcanzar la temperatura
5 minutos (300 segundos).

### 6. Tensión de alimentación del dispositivo
12 Voltios DC (ideal para uso en automóviles o sistemas portátiles).

### 7. Resistencia Eléctrica necesaria

Para calcular la resistencia eléctrica necesaria, seguimos estos pasos:

**Paso 1**: Calcular la cantidad de calor (Q) necesaria para elevar la temperatura del agua:

Q = m × c × ΔT

Donde:
- m = 0.75 kg (masa del agua)
- c = 4180 J/(kg·°C) (calor específico del agua)
- ΔT = 80°C - 20°C = 60°C (incremento de temperatura deseado)

Q = 0.75 kg × 4180 J/(kg·°C) × 60°C = 188,100 J

**Paso 2**: Calcular la potencia (P) necesaria:

P = Q / t = 188,100 J / 300 s = 627 W

**Paso 3**: Calcular la resistencia (R) aplicando la ley de Ohm:

R = V² / P = (12 V)² / 627 W = 144 / 627 = 0.23 Ω

Por lo tanto, necesitamos una resistencia eléctrica de aproximadamente 0.23 Ω.

### 8. Temperatura inicial del fluido
Se considera una temperatura inicial del agua de 20°C (temperatura ambiente promedio).

### 9. Temperatura ambiente
20°C.

### 10. Cálculo del aumento de temperatura en 1 segundo

Para calcular el aumento de temperatura en 1 segundo:

**Paso 1**: Calcular la potencia aplicada:

P = V² / R = (12 V)² / 0.23 Ω = 627 W

**Paso 2**: Calcular la energía transferida en 1 segundo:

E = P × t = 627 W × 1 s = 627 J

**Paso 3**: Calcular el incremento de temperatura:

ΔT = E / (m × c) = 627 J / (0.75 kg × 4180 J/(kg·°C)) = 627 / 3135 = 0.20°C

Por lo tanto, la temperatura aumentará aproximadamente 0.20°C tras 1 segundo de funcionamiento, suponiendo que no hay pérdida de calor.
