# Resolución TP5: Familias de Curvas con Distribuciones de Parámetros

## Problema planteado

El TP5 consiste en generar familias de curvas con distribuciones normales y uniformes de parámetros iniciales para analizar el efecto en el calentamiento del fluido. Específicamente, se solicita:

1. Distribución uniforme de 5 valores próximos de resistencias.
2. Distribución normal de 5 temperaturas iniciales del agua (Media 10°C, desvío estándar 5°C).
3. Distribución uniforme de 8 temperaturas iniciales del ambiente, entre -20°C y 50°C.
4. Distribución normal de 5 valores de tensión de alimentación (Media 12V, SD 4V).
5. Simulaciones que contengan todas las familias de curvas previas.

Este análisis permite evaluar la sensibilidad del sistema de calentamiento a variaciones en diferentes parámetros, ayudando a comprender su comportamiento bajo distintas condiciones operativas.

## Datos y parámetros utilizados

### Parámetros geométricos (del TP3)
- Diámetro: 8.0 cm
- Altura: 15.0 cm
- Radio: 4.0 cm
- Volumen: 753.98 cm³
- Capacidad: 0.75 litros

### Parámetros del aislante (del TP3)
- Espesor del aislante: 0.25 cm
- Coeficiente de conductividad térmica: 0.04 W/(m·K) (Fibra de vidrio)

### Parámetros eléctricos (valores base)
- Voltaje base: 12.0 V
- Resistencia base: 0.23 Ohms
- Potencia base: 626.09 W

### Parámetros del fluido
- Densidad del agua: 1.0 kg/L
- Masa del agua: 0.75 kg
- Calor específico del agua: 4180 J/(kg·°C)
- Temperatura inicial base: 20.0 °C
- Temperatura ambiente base: 20.0 °C

### Cálculo de pérdida de calor (del TP3)
- Superficie total: 0.033082 m²
- Coeficiente de pérdida de calor: 0.775 W/K

### Parámetros de simulación
- Tiempo total: 600 segundos
- Intervalo de tiempo: 5 segundos

## Enfoque y métodos utilizados

### A. Distribución uniforme de resistencias

Para analizar el efecto de variaciones en la resistencia eléctrica:

1. Se generaron 5 valores equidistantes de resistencia en el rango [0.18 Ω, 0.28 Ω] utilizando `np.linspace()`.
2. Para cada valor de resistencia, se calculó la potencia correspondiente según la fórmula: P = V²/R.
3. Se simuló el calentamiento considerando pérdidas térmicas para cada caso, donde:
   - La potencia efectiva se calculó como: Potencia efectiva = Potencia total - Pérdidas
   - Las pérdidas de calor dependen de la diferencia de temperatura: Pérdidas = k × (T - Tamb)
   - El incremento de temperatura en cada intervalo es: ΔT = (Potencia efectiva × Δt) / (m × c)

### B. Distribución normal de temperaturas iniciales

Para analizar el efecto de diferentes temperaturas iniciales del agua:

1. Se generaron 5 valores de temperatura inicial siguiendo una distribución normal con media 10°C y desviación estándar 5°C.
2. Se simuló el calentamiento con pérdidas térmicas utilizando la misma potencia base en todos los casos.
3. El modelo considera que las pérdidas térmicas dependen de la diferencia entre la temperatura actual y la temperatura ambiente.

### C. Distribución uniforme de temperaturas ambiente

Para evaluar el impacto de diferentes condiciones ambientales:

1. Se generaron 8 valores equidistantes de temperatura ambiente en el rango [-20°C, 50°C].
2. Se simuló el calentamiento considerando que las pérdidas térmicas son proporcionales a la diferencia entre la temperatura del agua y la temperatura ambiente.
3. A mayor diferencia de temperatura, mayores pérdidas, lo que afecta directamente a la potencia efectiva aplicada al fluido.

### D. Distribución normal de tensiones de alimentación

Para estudiar el efecto de fluctuaciones en la tensión de alimentación:

1. Se generaron 5 valores de tensión siguiendo una distribución normal con media 12V y desviación estándar 4V.
2. Se utilizó la ecuación diferencial que describe el calentamiento: dT/dt = P/(m×c) - k×(T-Tamb)/(m×c)
3. Se resolvió numéricamente la ecuación diferencial para cada valor de tensión mediante el método `odeint` de SciPy.

### E. Simulación combinada

Para analizar la interacción de todos los parámetros:

1. Se combinaron todas las variaciones anteriores en un único gráfico, utilizando distintos estilos de línea para cada familia de curvas.
2. Se utilizó una leyenda personalizada para ayudar a distinguir cada grupo de parámetros.
3. Para evitar saturar el gráfico con demasiadas curvas, se seleccionaron representantes de cada familia o se redujo la opacidad de algunas curvas.

## Resultados y discusión

### A. Efecto de la variación de resistencia

El análisis de la variación uniforme de resistencias muestra:

- Resistencias menores (R ≈ 0.18 Ω) producen mayor potencia y, por tanto, un calentamiento más rápido.
- Resistencias mayores (R ≈ 0.28 Ω) resultan en menor potencia y calentamiento más lento.
- La relación entre resistencia y velocidad de calentamiento no es lineal debido a la dependencia cuadrática de la potencia con la resistencia (P = V²/R).

### B. Efecto de la temperatura inicial

El análisis de las diferentes temperaturas iniciales muestra:

- Las curvas parten de diferentes temperaturas iniciales (rango aproximado 5-15°C) pero mantienen pendientes similares.
- Con el tiempo, la diferencia absoluta entre las temperaturas se mantiene relativamente constante.
- El tiempo necesario para alcanzar una temperatura objetivo varía significativamente dependiendo de la temperatura inicial.

### C. Efecto de la temperatura ambiente

El análisis de las diferentes temperaturas ambiente muestra:

- En ambientes muy fríos (-20°C), las pérdidas térmicas son significativamente mayores, reduciendo la eficiencia del calentamiento.
- En ambientes cálidos (50°C), el sistema calienta más rápido debido a menores pérdidas térmicas.
- Existe una relación aproximadamente lineal entre la temperatura ambiente y la temperatura final alcanzada en un tiempo determinado.

### D. Efecto de la tensión de alimentación

El análisis de las diferentes tensiones de alimentación muestra:

- Pequeñas variaciones en la tensión producen cambios significativos en la velocidad de calentamiento debido a la relación cuadrática (P = V²/R).
- Tensiones por encima de la nominal (>12V) pueden calentar el fluido mucho más rápidamente.
- Tensiones por debajo de la nominal (<12V) pueden resultar insuficientes para alcanzar la temperatura objetivo en el tiempo esperado.

### E. Análisis combinado

El análisis de todas las familias de curvas en conjunto permite observar:

- La tensión de alimentación y la resistencia tienen el mayor impacto en la velocidad de calentamiento.
- La temperatura ambiente afecta principalmente la temperatura de equilibrio a largo plazo.
- La temperatura inicial determina el "punto de partida" pero no altera significativamente la dinámica del sistema.

## Conclusiones

1. **Sensibilidad a parámetros eléctricos**: El sistema es extremadamente sensible a variaciones en los parámetros eléctricos (tensión y resistencia) debido a la relación cuadrática con la potencia. Pequeñas variaciones en estos parámetros pueden causar desviaciones significativas en el rendimiento térmico.

2. **Efecto de condiciones iniciales**: La temperatura inicial del agua afecta principalmente al tiempo necesario para alcanzar una temperatura objetivo, pero no altera significativamente el comportamiento dinámico del sistema.

3. **Influencia del ambiente**: La temperatura ambiente tiene un efecto significativo en la eficiencia energética del sistema. En ambientes fríos, el rendimiento se reduce considerablemente debido a mayores pérdidas térmicas.

4. **Robustez del diseño**: Para crear un sistema de calentamiento robusto, es crucial considerar las posibles variaciones en los parámetros eléctricos y ambientales, especialmente si se requiere un control preciso de la temperatura.

5. **Optimización del sistema**: Basándose en estas simulaciones, se podrían optimizar parámetros como el espesor del aislante o la potencia nominal para garantizar el rendimiento adecuado en el rango esperado de condiciones operativas.

Estas simulaciones proporcionan una comprensión valiosa del comportamiento del sistema bajo diferentes condiciones y pueden utilizarse para prever su rendimiento en diversos escenarios de operación, así como para guiar decisiones de diseño y optimización.
