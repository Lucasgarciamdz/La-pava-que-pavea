# Resolución TP4: Curva de Calentamiento Con y Sin Pérdidas

## Problema planteado

El TP4 consiste en graficar la temperatura del fluido dentro del calentador sin pérdidas y con pérdidas para cada tick de tiempo, hasta llegar al tiempo deseado para que el dispositivo cumpla su tarea.

Para realizar el gráfico con pérdidas, se debe considerar los vatios efectivos entregados al fluido restando al calor producido por la resistencia, el calor perdido por las paredes del recipiente. Con este calor efectivo se calcula la variación de temperatura del fluido para cada tick de tiempo.

Adicionalmente, se ha incorporado un tercer escenario en el que, a los 50 segundos del inicio del calentamiento, se agregan 4 cubitos de hielo de 10 gramos cada uno, para analizar el impacto de esta perturbación térmica en la curva de calentamiento.

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

### Parámetros eléctricos (del TP1 y TP2)
- Voltaje: 12.0 V
- Resistencia: 0.23 Ohms
- Potencia calculada: 626.09 W

### Parámetros del fluido (del TP2)
- Densidad del agua: 1.0 kg/L
- Masa del agua: 0.75 kg
- Calor específico del agua: 4180 J/(kg·°C)
- Temperatura inicial: 20.0 °C
- Temperatura ambiente: 20.0 °C
- Temperatura objetivo: 80.0 °C

### Parámetros del hielo (nuevo escenario)
- Masa total de hielo: 40 g (4 cubitos de 10g cada uno)
- Temperatura inicial del hielo: 0.0 °C
- Calor latente de fusión: 334000 J/kg
- Tiempo de adición del hielo: 50 segundos

### Cálculo de pérdida de calor (del TP3)
- Superficie total: 0.033082 m²
- Coeficiente de pérdida de calor: 0.775 W/K

## Cálculos y enfoque

### Modelo sin pérdidas
Para el modelo sin pérdidas, la temperatura se calcula mediante la fórmula:

```
T(t) = T₀ + (P × t)/(m × c)
```

Donde:
- T(t) es la temperatura en el tiempo t
- T₀ es la temperatura inicial (20°C)
- P es la potencia (626.09 W)
- m es la masa del agua (0.75 kg)
- c es el calor específico del agua (4180 J/(kg·°C))
- t es el tiempo en segundos

### Modelo con pérdidas
Para el modelo con pérdidas, en cada intervalo de tiempo se calcula:

1. La pérdida de calor en función de la diferencia de temperatura con el ambiente:
   ```
   perdida_w = PERDIDA_CALOR * (temperatura_actual - TEMP_AMBIENTE)
   ```

2. La potencia efectiva (potencia total menos pérdidas):
   ```
   potencia_efectiva = POTENCIA - perdida_w
   ```

3. El incremento de temperatura en el intervalo:
   ```
   delta_t = (potencia_efectiva * INTERVALO) / (MASA_AGUA * CALOR_ESPECIFICO_AGUA)
   ```

4. La nueva temperatura:
   ```
   temperatura_actual = temperatura_actual + delta_t
   ```

### Modelo con pérdidas y adición de cubitos de hielo
Para el tercer escenario, se sigue el mismo proceso que en el modelo con pérdidas, pero en el instante t=50s se modela la adición de los cubitos de hielo:

1. Se calcula la energía necesaria para derretir el hielo (calor latente de fusión):
   ```
   energia_fusion = MASA_HIELO * CALOR_LATENTE_FUSION
   ```

2. Se calcula la energía necesaria para elevar la temperatura del agua resultante hasta la temperatura actual del fluido:
   ```
   energia_calentamiento = MASA_HIELO * CALOR_ESPECIFICO_AGUA * (temperatura_actual - TEMP_HIELO)
   ```

3. Se determina la energía total requerida:
   ```
   energia_total = energia_fusion + energia_calentamiento
   ```

4. Se calcula la caída de temperatura en el fluido:
   ```
   caida_temperatura = energia_total / (masa_actual * CALOR_ESPECIFICO_AGUA)
   ```

5. Se actualiza la temperatura y la masa del fluido:
   ```
   temperatura_actual -= caida_temperatura
   masa_actual += MASA_HIELO
   ```

6. Para los cálculos subsiguientes, se utiliza la nueva masa total para determinar los incrementos de temperatura.

## Resultados

### Comparación de temperaturas en los tres escenarios

| Tiempo (s) | Sin Pérdidas (°C) | Con Pérdidas (°C) | Con Hielo (°C) |
|------------|-------------------|-------------------|----------------|
| 0          | 20.00             | 20.00             | 20.00          |
| 10         | 21.99             | 21.99             | 21.99          |
| 20         | 23.99             | 23.98             | 23.98          |
| 30         | 25.99             | 25.97             | 25.97          |
| 40         | 27.98             | 27.95             | 27.95          |
| 50         | 29.98             | 29.93             | 29.93          |
| 60         | 31.98             | 31.90             | 22.37          |
| 70         | 33.97             | 33.86             | 24.14          |
| 80         | 35.97             | 35.83             | 25.89          |
| 90         | 37.97             | 37.78             | 27.62          |
| 100        | 39.96             | 39.73             | 29.34          |

### Efecto de la adición de hielo

A los 50 segundos, justo después de la adición de los cubitos de hielo, se observó:

- Temperatura antes de agregar hielo: 29.93°C
- Caída de temperatura: 7.56°C 
- Temperatura después de agregar hielo: 22.37°C
- Nueva masa de agua: 0.790 kg

## Análisis de resultados

1. El modelo básico sin pérdidas muestra un calentamiento constante y lineal, alcanzando aproximadamente 40°C a los 100 segundos.

2. El modelo con pérdidas presenta una curva ligeramente inferior, con una diferencia que aumenta gradualmente con el tiempo, alcanzando aproximadamente 39.7°C a los 100 segundos.

3. La adición de hielo a los 50 segundos produce un efecto doble:
   - Una caída inmediata y abrupta de la temperatura de aproximadamente 7.6°C.
   - Una disminución en la tasa de calentamiento posterior debido al aumento de la masa de agua que debe ser calentada.

4. Al final de la simulación (t=100s), la temperatura en el escenario con hielo (29.3°C) es aproximadamente 10.4°C menor que en el escenario con pérdidas sin hielo (39.7°C).

5. La adición de hielo tiene un efecto más significativo en la temperatura que las pérdidas por conducción térmica a través de las paredes, al menos en el período analizado.

## Conclusiones

1. Las pérdidas de calor a través de las paredes tienen un impacto relativamente pequeño en los primeros 100 segundos de calentamiento, reduciendo la temperatura final en menos de 1°C respecto al modelo ideal.

2. La adición de los cubitos de hielo representa una perturbación significativa en el sistema, con dos efectos principales:
   - Un efecto inmediato debido a la absorción de calor para derretir el hielo y elevar su temperatura.
   - Un efecto permanente en la tasa de calentamiento debido al aumento de la masa total de agua.

3. En sistemas de calentamiento reales, es importante considerar no solo las pérdidas térmicas a través de las paredes, sino también posibles perturbaciones como la adición de nuevos elementos al sistema.

4. Para aplicaciones donde es necesario mantener una temperatura estable o alcanzar un objetivo en un tiempo determinado, se debe tener en cuenta la posibilidad de perturbaciones térmicas y diseñar sistemas con capacidad suficiente para compensarlas.

5. La simulación demuestra la importancia de modelar correctamente tanto los procesos de transferencia de calor continuos (conducción a través de las paredes) como los eventos discretos (adición de hielo) para obtener predicciones realistas del comportamiento térmico del sistema.
