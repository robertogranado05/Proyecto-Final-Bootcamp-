from cmu_graphics import *
from cmu_graphics import cmu_graphics
import random

rotuloPregunta = Label('', 200, 100, tamaño=20, negrito=True)

### Listas de preguntas ###
ingles = [['Como se dice casa', 'House', 'Caseichon', 'Casin', 'Jaus'], 
            ['como se dice carro', 'car'], 
            ['como se dice mamá', 'Mom']]
mates = [['Cual es la raíz cuadrada de 9', '3'], 
        ['cuantos es dos más dos', '4'], 
        ['cuantos es 2 X 4', '8']]
general = [['¿Cuantos huesos tiene el cuerpo humano?', '206'], 
            ['¿Cuanto acabó la segunda guerra mundial', '1945'], 
            ['¿En que fecha se celebra la independencia en Colombia?', '20 de Julio']
            ]

pregunta = ''

# Toma un parametro con el nombre de la materia o conjunto de palabras
def obtenerPregunta(lista):
    global rotuloPregunta
    lista.lower()
    #Compara el parametro con las listas existentes
    if lista == 'ingles':
        #Obtiene un valor aleatorio de fila y toma una pregunta y su respuesta
        fila = random.randint(0, 2)
        pregunta = ingles[fila][0]     
        respuesta = ingles[fila][1]
        ingles.pop(ingles.index(pregunta))
    elif lista == 'matematicas':
        fila = random.randint(0, 2)
        pregunta = mates[fila][0]
        respuesta = mates[fila][1]
        mates.pop(mates.index(pregunta))
    elif lista == 'cultura general':
        fila = random.randint(0, 2)
        pregunta = general[fila][0]
        respuesta = general[fila][1]
        general.pop(general.index(pregunta))
    
    rotuloPregunta.valor = pregunta
    print(pregunta)
    return respuesta

vidaDragon = 99
vidaJugador = 99

def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 11
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 11

while vidaDragon > 0 and vidaJugador > 0:
    materia = input("¿Que materia desea escoger entre estas?\n Inglés\n Matemáticas\n Cultural General\n")
    for i in range(3):
        respuesta = obtenerPregunta(materia)
        respuestaJugador = input()
        comprobarVictoria(respuestaJugador, respuesta)

        print(f"El jugador tiene: {vidaJugador} de vida")
        print(f"El dragón tiene: {vidaDragon} de vida")

if vidaDragon == 0:
    print("Tú ganas")
elif vidaJugador == 0:
    print("El dragón gana")

cmu_graphics.run()