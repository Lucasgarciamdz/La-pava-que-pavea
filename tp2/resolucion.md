# Trabajo Práctico 2: Curva de Calentamiento Sin Pérdidas

## Objetivo
Graficar la curva de calentamiento (temperatura en función del tiempo) para el calentador de agua eléctrico diseñado en el TP1, sin considerar pérdidas de calor.

## Parámetros del Calentador

Mantenemos los parámetros establecidos en el TP1:

- **Material aislante**: Fibra de vidrio (2.5 mm)
- **Forma y capacidad**: Cilíndrica, 750 ml (0.75 L)
- **Propósito**: Calentar agua para mate (temperatura objetivo: 80°C)
- **Fluido**: Agua potable
- **Tiempo deseado**: 5 minutos (300 segundos)
- **Voltaje**: 12 V DC
- **Resistencia eléctrica**: 0.23 Ω
- **Temperatura inicial**: 20°C
- **Temperatura ambiente**: 20°C

## Cálculo de la Curva de Calentamiento

Para calcular la temperatura en cada instante de tiempo, utilizamos la siguiente fórmula básica:

1. Potencia entregada por la resistencia:
   P = V²/R = (12 V)²/0.23 Ω = 627 W

2. Energía transferida en un intervalo de tiempo dt:
   E = P × dt

3. Incremento de temperatura en ese intervalo:
   ΔT = E/(m × c) = P × dt/(m × c)

4. Temperatura en cada instante:
   T(t) = T₀ + (P × t)/(m × c)

Donde:
- T₀ es la temperatura inicial (20°C)
- m es la masa del agua (0.75 kg)
- c es el calor específico del agua (4180 J/(kg·°C))
- t es el tiempo transcurrido en segundos

## Resultados de la Simulación

La simulación se realizó con intervalos de 5 segundos, desde 0 hasta 360 segundos (6 minutos), para observar el comportamiento completo del calentamiento.

### Tiempo para Alcanzar la Temperatura Objetivo

Según la simulación, la temperatura objetivo de 80°C se alcanza aproximadamente a los 300 segundos (5 minutos), lo cual cumple con los requisitos de diseño establecidos inicialmente.

### Gráfico de la Curva de Calentamiento

En el gráfico adjunto se puede observar cómo la temperatura aumenta linealmente con el tiempo. Esta linealidad se debe a que estamos considerando un sistema ideal sin pérdidas de calor, donde toda la energía eléctrica se convierte en energía térmica que se transfiere al agua.

## Conclusiones

1. La curva de calentamiento sin pérdidas muestra un comportamiento lineal, como era de esperar teóricamente.
2. El calentador diseñado alcanza la temperatura objetivo en el tiempo deseado.
3. La tasa de calentamiento es de aproximadamente 0.20°C por segundo.
4. En un sistema real, la curva tendería a curvarse hacia una asíntota horizontal debido a las pérdidas de calor, que serán consideradas en trabajos prácticos posteriores.

En el próximo trabajo práctico, se analizarán las pérdidas de calor para obtener una simulación más realista del comportamiento del calentador.
