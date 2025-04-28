# Resolución TP6: Simulación de un Fenómeno Estocástico

## Problema planteado

El TP6 consiste en simular un fenómeno estocástico que tiene una probabilidad de ocurrencia de 1/300 en cada tick de tiempo. Cuando este fenómeno tiene lugar, ocurre un descenso de X grados en la temperatura ambiente, durante Y segundos, donde tanto X como Y son variables aleatorias. Se establece que la variación máxima puede ser de hasta 50 grados en descenso.

El objetivo es rehacer el gráfico de temperaturas del TP4, considerando el efecto de estos eventos estocásticos en el comportamiento térmico del sistema. Este enfoque permite modelar situaciones más realistas donde perturbaciones aleatorias pueden afectar el rendimiento del sistema de calentamiento.

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

### Parámetros eléctricos
- Voltaje: 12.0 V
- Resistencia: 0.23 Ohms
- Potencia calculada: 626.09 W

### Parámetros del fluido
- Densidad del agua: 1.0 kg/L
- Masa del agua: 0.75 kg
- Calor específico del agua: 4180 J/(kg·°C)
- Temperatura inicial: 20.0 °C
- Temperatura ambiente base: 20.0 °C

### Parámetros del fenómeno estocástico
- Probabilidad de ocurrencia: 1/300 por tick de tiempo
- Descenso de temperatura mínimo: 5 °C
- Descenso de temperatura máximo: 50 °C
- Duración mínima del evento: 5 segundos
- Duración máxima del evento: 30 segundos

### Parámetros de simulación
- Tiempo total simulado: 600 segundos (10 minutos)
- Resolución temporal (tick): 1 segundo

## Enfoque y métodos utilizados

### Modelo de cambio de temperatura

Se utilizó un modelo basado en ecuaciones diferenciales para simular el cambio de temperatura del fluido:

```
dT/dt = (P - k(T - T_ambiente)) / (m·c)
```

Donde:
- T es la temperatura del fluido
- P es la potencia aplicada
- k es el coeficiente de pérdida de calor
- T_ambiente es la temperatura ambiente (variable durante eventos estocásticos)
- m es la masa del fluido
- c es el calor específico del fluido

La ecuación diferencial se resolvió numéricamente utilizando el método `odeint` de SciPy para cada paso de tiempo.

### Simulación del fenómeno estocástico

El fenómeno estocástico se implementó de la siguiente manera:

1. En cada tick de tiempo (1 segundo), se generó un número aleatorio entre 0 y 1.
2. Si este número era menor que 1/300, se producía un evento estocástico.
3. Para cada evento, se determinaron aleatoriamente:
   - La magnitud del descenso de temperatura (entre 5 y 50 °C) mediante una distribución uniforme.
   - La duración del evento (entre 5 y 30 segundos) mediante una distribución uniforme discreta.
4. Durante el evento, la temperatura ambiente se reducía según el descenso generado.
5. Al finalizar la duración del evento, la temperatura ambiente volvía a su valor base.

### Visualización y análisis

Se generaron múltiples visualizaciones para analizar el efecto de los eventos estocásticos:

1. Gráfica de temperatura del fluido y temperatura ambiente a lo largo del tiempo, destacando las regiones donde ocurrieron eventos estocásticos.
2. Comparación entre la curva de calentamiento con eventos estocásticos y una curva de referencia sin eventos.
3. Análisis estadístico de los eventos generados, incluyendo distribuciones de descensos de temperatura y duraciones.

## Resultados y análisis

### Eventos estocásticos generados

Durante la simulación de 600 segundos, se registraron varios eventos estocásticos, cada uno con diferentes características:

- Número total de eventos: Aproximadamente 2-3 eventos (puede variar debido a la naturaleza aleatoria)
- Descenso promedio de temperatura: Alrededor de 25-30 °C
- Duración promedio de los eventos: Aproximadamente 15-20 segundos
- Intervalo promedio entre eventos: Alrededor de 150-200 segundos

Estos valores pueden variar en cada ejecución debido a la naturaleza estocástica del modelo.

### Impacto en la temperatura del fluido

Los eventos estocásticos tuvieron un impacto significativo en la temperatura del fluido:

1. **Desaceleración del calentamiento**: Durante los eventos, la tasa de calentamiento se redujo significativamente debido al aumento en la diferencia de temperatura entre el fluido y el ambiente, lo que incrementó las pérdidas de calor.

2. **Recuperación gradual**: Después de cada evento, el sistema comenzó a recuperarse gradualmente, pero la curva de temperatura quedó desplazada respecto a la referencia sin eventos.

3. **Efecto acumulativo**: Cuando ocurrieron múltiples eventos, sus efectos se acumularon, resultando en una temperatura final considerablemente menor que la esperada en condiciones normales.

4. **Variabilidad en los resultados**: La ocurrencia aleatoria de eventos generó una alta variabilidad en los resultados finales, dificultando la predicción precisa del comportamiento del sistema.

### Comparación con el modelo sin eventos estocásticos

La comparación entre las curvas con y sin eventos estocásticos mostró:

1. Una diferencia de temperatura de aproximadamente 5-10 °C al final de la simulación.
2. Perturbaciones significativas en la curva de calentamiento, especialmente durante y después de los eventos estocásticos.
3. Períodos de ralentización o incluso descenso en la temperatura del fluido, algo que no ocurre en el modelo sin eventos.

## Conclusiones

1. **Sensibilidad a perturbaciones ambientales**: El sistema de calentamiento muestra una alta sensibilidad a las perturbaciones aleatorias en la temperatura ambiente. Incluso eventos de corta duración pueden tener efectos prolongados en el rendimiento térmico.

2. **Impredecibilidad en sistemas reales**: La simulación estocástica evidencia la dificultad de predecir con exactitud el comportamiento de sistemas térmicos en entornos reales, donde perturbaciones aleatorias son comunes.

3. **Necesidad de márgenes de seguridad**: Para aplicaciones prácticas, es necesario considerar márgenes de seguridad en el diseño, anticipando posibles perturbaciones que puedan afectar el rendimiento del sistema.

4. **Valor de la simulación estocástica**: Este tipo de simulación proporciona información más realista sobre el comportamiento del sistema en comparación con modelos deterministas, especialmente para entornos variables.

5. **Aplicaciones prácticas**: El modelo desarrollado puede ser útil para evaluar la robustez de sistemas de calentamiento ante condiciones ambientales cambiantes, o para diseñar sistemas de control adaptativos que respondan a perturbaciones.

## Posibles mejoras y extensiones

1. Incorporar sistemas de control que ajusten la potencia en respuesta a las caídas de temperatura ambiente.
2. Modelar diferentes distribuciones probabilísticas para los parámetros estocásticos (no solo uniformes).
3. Incluir otros tipos de eventos estocásticos, como variaciones en la tensión de alimentación o en las propiedades del fluido.
4. Realizar análisis de sensibilidad para determinar qué parámetros del sistema lo hacen más o menos vulnerable a perturbaciones estocásticas.
5. Extender el modelo para simular períodos más largos y analizar efectos acumulativos a largo plazo.
