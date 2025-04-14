# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
# ---

# %% [markdown]
# # Simulación del calentador eléctrico - TP2
#
# Curva de calentamiento sin pérdidas de calor con intervalos de 5 segundos.
# Este notebook extiende el trabajo del TP1 para analizar la curva de calentamiento.

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## Parámetros del Calentador

# %%
# Parámetros iniciales (mantenemos los del TP1)
TEMPERATURA_INICIAL = 20  # Temperatura inicial del agua en °C
TEMPERATURA_AMBIENTE = 20  # Temperatura ambiente en °C
VOLTAJE = 12  # Voltaje en V
RESISTENCIA = 0.23  # Resistencia del calentador en ohmios
CALOR_ESPECIFICO = 4180  # Capacidad calorífica del agua en J/(kg·°C)
MASA_AGUA = 0.75  # Masa del agua en kg (750 ml)
TIEMPO_TOTAL = 360  # Tiempo total en segundos (6 minutos)

# Cálculo de la potencia
POTENCIA = VOLTAJE**2 / RESISTENCIA  # Potencia en Watts

# %% [markdown]
# ## Resumen de parámetros

# %%
print(f"--- Parámetros del Calentador ---")
print(f"Voltaje: {VOLTAJE} V")
print(f"Resistencia: {RESISTENCIA} Ω")
print(f"Potencia Calculada: {POTENCIA:.2f} W")
print(f"Masa del agua: {MASA_AGUA} kg")
print(f"Temperatura inicial: {TEMPERATURA_INICIAL} °C")
print(f"Tiempo total simulado: {TIEMPO_TOTAL} segundos")

# %% [markdown]
# ## Simulación de la curva de calentamiento

# %%
# Crear arreglo de tiempo con intervalos de 5 segundos
tiempo = np.arange(0, TIEMPO_TOTAL + 1, 5)

# Lista para almacenar las temperaturas
temperaturas = []

# Cálculo teórico para cada instante de tiempo
for t in tiempo:
    # Temperatura en función del tiempo sin pérdidas
    # T(t) = T₀ + (P × t)/(m × c)
    temperatura = TEMPERATURA_INICIAL + (POTENCIA * t) / (MASA_AGUA * CALOR_ESPECIFICO)
    temperaturas.append(temperatura)

# Convertir lista a array de NumPy
temperaturas = np.array(temperaturas)

# %% [markdown]
# ## Resultados cada 30 segundos

# %%
# Imprimir las temperaturas cada 30 segundos
print("\n--- Resultados de la Simulación ---")
for i, t in enumerate(tiempo):
    if i % 6 == 0 or t == 300:  # Cada 30 segundos o en t=300s
        print(f"Segundo {t}: {temperaturas[i]:.2f}°C")

# %% [markdown]
# ## Análisis de la temperatura objetivo

# %%
# Determinar en qué momento se alcanza la temperatura objetivo (80°C)
temp_objetivo = 80
if np.max(temperaturas) >= temp_objetivo:
    # Encontrar el índice del primer valor que supera la temperatura objetivo
    idx = np.where(temperaturas >= temp_objetivo)[0][0]
    tiempo_objetivo = tiempo[idx]
    print(f"\nTemperatura objetivo de {temp_objetivo}°C alcanzada en {tiempo_objetivo} segundos")
else:
    print(f"\nNo se alcanzó la temperatura objetivo de {temp_objetivo}°C en el tiempo simulado")

# %% [markdown]
# ## Gráfico de la curva de calentamiento

# %%
# Crear la gráfica
plt.figure(figsize=(10, 6))

# Gráfico de línea
plt.plot(tiempo, temperaturas, label='Temperatura del agua', marker='o', linestyle='-')

# Añadir línea de temperatura objetivo
plt.axhline(y=temp_objetivo, color='r', linestyle='--', 
            label=f'Temperatura objetivo ({temp_objetivo}°C)')

# Añadir punto donde se alcanza la temperatura objetivo (si se alcanza)
if np.max(temperaturas) >= temp_objetivo:
    plt.plot(tiempo_objetivo, temp_objetivo, 'ro', markersize=10)
    plt.annotate(f'{tiempo_objetivo} s', 
                 xy=(tiempo_objetivo, temp_objetivo),
                 xytext=(tiempo_objetivo+10, temp_objetivo-5),
                 arrowprops=dict(facecolor='black', shrink=0.05))

# Personalizar gráfico
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Temperatura (°C)')
plt.title('Calentamiento del Agua para Mate - Sin Pérdidas de Calor')
plt.grid(True)
plt.legend()

# Guardar el gráfico como imagen
plt.savefig('tp2/curva_calentamiento_sin_perdidas.png')

# Mostrar el gráfico
plt.show()
