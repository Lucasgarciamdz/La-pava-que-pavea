# Consigna tp1

TP 7: Modelo y Simulación de un Sistema de Atención al Público

Introducción.
Estamos presenciando un aumento de la competencia entre los diversos prestadores de servicios, que intentan captar más clientes y lograr mayor participación de mercado, manteniendo los clientes actuales, sin perderlos, con los perjuicios que ello ocasiona.

Por ello, este modelo tiende a demostrar cuál es la mejor alternativa de habilitación de boxes de atención, para lograr mayor cantidad de personas atendidas, en el menor tiempo posible.

El modelo es aplicable a cajas de supermercados, a bancos, locales de comida y, en general, en todos los centros de prestación en donde los clientes se ubican en colas que pueden derivar en pérdidas importante de tiempo. Como se dice habitualmente "time is money". Muchas veces las empresas pierden de vista el valor estratégico de la pronta y correcta atención de los clientes.
Un mal diseño de este servicio puede derivar en la pérdida de operaciones y en la lisa y llana pérdida del cliente, con todas las operaciones potenciales que no se realizarán nunca con estas personas.

Descripción.
Se trata de un local de servicios que puede contar con 1 a 10 boxes de atención de clientes,.
Al momento de iniciar la simulación se elige este parámetro.
Luego, la simulación responde a las siguientes reglas e hipótesis:
1) El local abre de 8 a 12 horas.
2) El cliente que ingresa es atendido en la zona de atención o pasa a una cola.
3) Los clientes que están en cola o siendo atendidos pueden permanecer luego de la hora de cierre.
4) Los clientes que no están siendo atendidos abandonarán el local a los 30 minutos.
5) En cada segundo que transcurre, desde la apertura del local, la probabilidad de que ingrese un cliente es p=1/144.
6) La cantidad de boxes activos se establece antes de correr la simulación.
7) El tiempo de atención en cada box responde a una distribución normal, con media=10 minutos y desvio estándar=5 minutos.
8) Mantener el box abierto durante toda la mañana cuesta $1000.
9) Cada cliente que se va sin ser atendido representa una pérdida de $10.000.
10) Todo dato requerido para diseñar y programar la simulación puede ser asumido o especificado adicionalmente por cada uno de Ustedes.

Resultados.
Al final de cada simulación, deberemos responder a los siguientes interrogantes:
1) Cuántos clientes ingresaron al local?
2) Cuántos clientes fueron atendidos?
3) Cuántos clientes no fueron atendidos? Es decir abandonaron el local por demoras.
4) Tiempo mínimo de atención en box.
5) Tiempo máximo de atención en box.
6) Tiempo mínimo de espera en salón.
7) Tiempo máximo de espera en salón.
8) Costo de la operación: costo del box+costo por pérdida de clientes.
9) Presentación gráfica animada de cada proceso simulado, con diversas velocidades. Archivo AVI.