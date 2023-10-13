import random

ingles = [['Como se dice casa', 'House'], 
            ['como se dice carro', 'car'], 
            ['como se dice mamá', 'Mom']
        ]
mates = [['Cual es la raíz cuadrada de 9', '3'], 
        ['cuantos es dos más dos', '4'], 
        ['cuantos es 2 X 4', '8']]
general = [['¿Cuantos huesos tiene el cuerpo humano?', '206'], 
            ['¿Cuanto acabó la segunda guerra mundial', '1945'], 
            ['¿En que fecha se celebra la independencia en Colombia?', '20 de Julio']
            ]

listaDePreguntas  = [ingles, mates, general]
pregunta = ''
respuesta = ''

def obtenerPregunta():
    for lista in listaDePreguntas:
        for fila in range(3):
            pregunta = lista[fila][0]
            respuesta = lista[fila][1]
            print(pregunta)

while True:
    obtenerPregunta()