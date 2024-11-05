# Vamos a generar un gráfico de línea primero
# Gráfico de Líneas con Matplotlib
# Importar la biblioteca Matplotlib
import matplotlib.pyplot as plt

# Crear datos para el gráfico de línea
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  
ingresos = [220000, 240000, 190000, 210000, 230000, 200000, 180000, 160000, 270000, 99000, 110000, 98700]  

# Crear gráfico de línea
plt.plot(mes, ingresos)

# Añadir títulos y etiquetas
plt.title('Ingresos anuales')  # Título del gráfico
plt.xlabel('mes')  # Etiqueta para el eje X
plt.ylabel('ingresos (colones)')  # Etiqueta para el eje Y

# Mostrar gráfico
plt.show()


# Crea tu propio Gráfico de Líneas con Matplotlib

# Ahora vamos a crear un gráfico de barras usando datos nuevos.

# Importar la biblioteca Matplotlib
import matplotlib.pyplot as plt

# Crear los datos
# En este caso, vamos a mostrar la cantidad de libros leídos por 5 amigos en un mes
amigos = ['Juan', 'María', 'Pedro', 'Ana', 'Luis']
libros_leidos = [3, 5, 2, 4, 6]

# Crear tu propio gráfico de barras
# Usa la función plt.bar() para hacer el gráfico de barras
# Rellena la función plt.bar() con los datos de 'amigos' y 'libros_leidos'

plt.bar(amigos, libros_leidos)

# Añadir títulos y etiquetas
# Usa plt.title() para añadir un título al gráfico, algo como: "Libros leídos por amigos en un mes"
# Usa plt.xlabel() para poner una etiqueta para los amigos, algo como: "Amigos"
# Usa plt.ylabel() para poner una etiqueta para la cantidad de libros leídos, algo como: "Libros leídos"

plt.title('Cantidad de libros leídos')
plt.xlabel('Persona')
plt.ylabel('Cantidad')

# Mostrar el gráfico
# Finalmente, usa plt.show() para que se muestre el gráfico.

plt.show()


# Crea tu propio Gráfico de pastel con Matplotlib

# Ahora vamos a crear un gráfico de barras usando datos nuevos.

# Crear los datos
# Representaremos las actividades diarias de una persona
# actividades = ['Dormir', 'Comer', 'Trabajar', 'Estudiar', 'Ocio']
#horas = [8, 2, 8, 3, 3]  # Horas dedicadas a cada actividad en un día

encuesta=['si', 'no']
personas= [8, 4]

# Crear gráfico de pastel
# plt.pie(horas, labels=actividades, autopct='%1.1f%%', startangle=90)
plt.pie(personas, labels=encuesta, autopct='%1.1f%%', startangle=90)
# Añadir un título
# plt.title('Distribución de tiempo diario')

plt.title('Personas que dijeron que si y los que dijeron que no')
# Mostrar gráfico
# plt.show()

plt.show()