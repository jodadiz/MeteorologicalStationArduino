import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np


def getSerialData(self,Samples,numData,serialConnection, lines):
    for i in range(numData):
        valor  = float(serialConnection.readline().strip())  # Lectura de cualsea sensor
        data[i].append(valor) # Guarda lectura en la última posición
        lines[i].set_data(range(Samples),data[i]) # Dibujar nueva linea

        
PuertoSerial = 'COM3' # Depende a que puerto se encuentre conectado
Baudiosrango = 9600  # Baudios

try:
  serialConnection = serial.Serial(PuertoSerial, Baudiosrango) # Intento de conexion con el puerto Serial
except:
  print('No se logro la conexion con dicho puerto')

Samples = 50  #Cantidad de muestas
sampleTime = 150  #Tiempo en el que se toma una cantidad de muestras
numData = 3 #Son tres toma de datos a considerar


# Limites de los ejes
xmin = 0
xmax = Samples
ymin = [0, 0 , -50 ,0]
ymax = [6, 6 , 50 , 100]
lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='blue'))
  
fig = plt.figure()# Crea una nueva figura
ax1 = fig.add_subplot(2, 2, 1,xlim=(xmin, xmax), ylim=(ymin[0] , ymax[0]))
ax1.title.set_text('Grafica de Temperatura')
ax1.set_xlabel("Datos")
ax1.set_ylabel("Temperatura")
ax1.add_line(lines[0])

ax2 = fig.add_subplot(2, 2, 2,xlim=(xmin, xmax), ylim=(ymin[1] , ymax[1]))
ax2.title.set_text('Grafica de Humedad')
ax2.set_xlabel("Datos")
ax2.set_ylabel("Humedad")
ax2.add_line(lines[1])

ax3 = fig.add_subplot(2, 2, 3,xlim=(xmin, xmax), ylim=(ymin[2] , ymax[2]))
ax3.title.set_text('Grafia de luminiscencia')
ax3.set_xlabel("Datos")
ax3.set_ylabel("luminiscencia")
ax3.add_line(lines[2])

# Mantiene una animacion a tiempo real de las graficas de los diferentes datos en un tiempo establecido
anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)
plt.show()

serialConnection.close() # cerrar puerto serial/ close serial port
 
