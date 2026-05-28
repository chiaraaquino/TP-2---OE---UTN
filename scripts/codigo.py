archivo = open('datos/datos.csv','r')
lineas = archivo.readlines ()
archivo.close()

total_goles = 0
puntos = {}
ganados = {}

for i in range(1, len(lineas)):
    linea = lineas[i].split(',')
    equipo_local = linea[0]
    equipo_visitante = linea[1]
    goles_local = int(linea[2])
    goles_visitante = int(linea[3])

    total_goles = total_goles + goles_local + goles_visitante

    if equipo_local not in puntos:
        puntos[equipo_local] = 0
        ganados[equipo_local] = 0
    if equipo_visitante not in puntos:
        puntos[equipo_visitante] = 0
        ganados[equipo_visitante] = 0

    if goles_local > goles_visitante:
        puntos[equipo_local] = puntos[equipo_local] + 3
        ganados[equipo_local] = ganados[equipo_local] + 1
    elif goles_visitante > goles_local:
        puntos[equipo_visitante] = puntos[equipo_visitante] + 3
        ganados[equipo_visitante] = ganados[equipo_visitante] + 1
    else:
        puntos[equipo_local] = puntos[equipo_local] + 1
        puntos[equipo_visitante] = puntos[equipo_visitante] + 1

promedio = total_goles / (len(lineas) - 1)

salida = open('resultados/resultados.txt', 'w')
salida.write('Promedio de goles por partido: ')
salida.write(str(promedio))
salida.write('\n\n')
salida.write('TABLA DE POSICIONES\n')
salida.write('Equipo Puntos Ganados\n')
salida.write('--------------------------------\n')

for equipo in puntos:
    salida.write(equipo)
    salida.write(' ')
    salida.write(str(puntos[equipo]))
    salida.write(' ')
    salida.write(str(ganados[equipo]))
    salida.write('\n')

salida.close()

import matplotlib.pyplot as plt
plt.bar(ganados.keys(), ganados.values())
plt.title('Partidos Ganados por Equipo')
plt.savefig('resultados/grafico.png')
plt.close()

print('Listo')
