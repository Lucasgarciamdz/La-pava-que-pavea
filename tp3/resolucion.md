# Trabajo Práctico 3: Cálculo de Pérdidas de Calor

## Objetivo
Calcular la pérdida de calor del calentador de agua eléctrico diseñado en los TP anteriores, según sus especificaciones de diseño.

## Especificaciones del Calentador

Recordemos las especificaciones de nuestro calentador, definidas en el TP1:

- **Material aislante**: Fibra de vidrio (espesor de 2.5 mm)
- **Forma**: Cilíndrica
- **Dimensiones**: Diámetro de 8 cm, altura de 15 cm
- **Capacidad**: 750 ml (0.75 litros)
- **Resistencia de NICROM**: 0.23 Ω
- **Voltaje**: 12 V

## Cálculo de la Pérdida de Calor

Para calcular la pérdida de calor utilizaremos la fórmula:

> Calor perdido (W/K) = CCT × Sup / Esp

Donde:
- **CCT**: Coeficiente de Conductividad Térmica (W/m·K)
- **Sup**: Superficie total del dispositivo (m²)
- **Esp**: Espesor de las paredes del dispositivo (m)

### 1. Cálculo de la Superficie Total

Para un cilindro, la superficie total se compone de la superficie lateral y las dos bases:

Superficie total = Superficie lateral + Superficie de las bases
Superficie total = 2π × r × h + 2π × r²

Donde:
- r = radio del cilindro = 8 cm / 2 = 4 cm = 0.04 m
- h = altura del cilindro = 15 cm = 0.15 m

Superficie lateral = 2π × 0.04 m × 0.15 m = 0.038 m²
Superficie de las bases = 2π × (0.04 m)² = 2π × 0.0016 m² = 0.010 m²
Superficie total = 0.038 m² + 0.010 m² = 0.048 m²

### 2. Coeficiente de Conductividad Térmica (CCT)

Para la fibra de vidrio, el CCT es aproximadamente 0.04 W/(m·K).

### 3. Espesor de las Paredes

El espesor de las paredes de fibra de vidrio es de 2.5 mm = 0.0025 m.

### 4. Cálculo de Pérdida de Calor

Aplicando la fórmula:

Pérdida de calor = 0.04 W/(m·K) × 0.048 m² / 0.0025 m = 0.768 W/K

## Análisis del Resultado

La pérdida de calor calculada para nuestro calentador con aislamiento de fibra de vidrio es de aproximadamente 0.768 W/K. Esto significa que, por cada grado Kelvin (o Celsius) de diferencia entre la temperatura del agua y la temperatura ambiente, el calentador perderá 0.768 Watts de potencia térmica.

Como referencia, en la consigna se mencionaba que un dispositivo de telgopor de 1 litro y espesor de 1 mm suele tener pérdidas de aproximadamente 2.1 W/K. Nuestro diseño, con un aislamiento de fibra de vidrio de 2.5 mm de espesor, tiene una pérdida considerablemente menor por unidad de temperatura, lo que demuestra la eficiencia del material y el espesor seleccionados.

## Implicaciones para el Rendimiento del Calentador

La pérdida de calor calculada influirá en el tiempo total necesario para calentar el agua hasta la temperatura objetivo. A medida que la temperatura del agua se eleve por encima de la temperatura ambiente, estas pérdidas serán más significativas.

Para nuestro calentador, con una potencia de 627 W (calculada en el TP1), y considerando una diferencia máxima de temperatura de 60°C (de 20°C a 80°C), la pérdida de calor máxima sería:

Pérdida máxima = 0.768 W/K × 60 K = 46.08 W

Esto representa aproximadamente el 7.35% de la potencia total disponible, lo que deberá ser considerado en las simulaciones posteriores para obtener un tiempo de calentamiento más realista.

En el próximo trabajo práctico, incorporaremos esta pérdida de calor en nuestra simulación para analizar cómo afecta a la curva de calentamiento del agua.
