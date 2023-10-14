from cmu_graphics import *
from cmu_graphics import cmu_graphics
import random
import BatallaElecciones as pantallaElección

pantallaElección.alFondo()
rotuloPregunta = Label('', 90, 320, tamaño=20, negrito=True)

### Listas de preguntas ###
ingles = [['Traduce: CASA', 'House'], 
            ['Traduce: CARRO', 'car'], 
            ['Traduce: MADRE', 'Mom'],
            ['Traduce: MANZANA', 'Apple'],
            ['Traduce: HABITACIÓN', 'Room'],
            ['Traduce: AZÚCAR', 'Sugar']
        ]
mates = [['Raíz cuadrada de 9', '3'], 
        ['2 + 2', '4'], 
        ['2 X 4', '8'],
        ['¿Cuantos segundos hay en un minuto?', '60'],
        ['2 X 2 + 10', '14'],
        ['¿Cuantos angulos tiene un triangulo?', '3'],
        ['El único numero primo par', '2']
        ]
general = [['¿Cuantos huesos tiene el cuerpo humano?', '206'], 
            ['¿Cuanto acabó la segunda guerra mundial', '1945'], 
            ['¿En que fecha se celebra la independencia en Colombia?', '20 de Julio'],
            ['¿En que año se descubrió América?', '1492'],
            ['¿Cual es el pais mas grande del mundo?', 'Rusia'],
            ['¿Cual es el animal más grande del planeta?', 'Ballena azul'],
            ['¿Cual es la capital de Colombia?', 'Bogotá']
            ]

pregunta = ''
preguntasUsadas = list()

# Toma un parametro con el nombre de la materia o conjunto de palabras
def obtenerPregunta(lista):
    global rotuloPregunta, pregunta
    lista.lower()
    #Compara el parametro con las listas existentes
    if lista == 'ingles':
        #Obtiene un valor aleatorio de fila y toma una pregunta y su respuesta
        fila = random.randint(0, len(ingles) - 1)
        pregunta = ingles[fila][0]     
        respuesta = ingles[fila][1]
    elif lista == 'matematicas':
        fila = random.randint(0, len(mates) - 1)
        pregunta = mates[fila][0]
        respuesta = mates[fila][1]
    elif lista == 'cultura general':
        fila = random.randint(0, len(general) - 1)
        pregunta = general[fila][0]     
        respuesta = general[fila][1]
    
    rotuloPregunta.valor = pregunta
    # print(pregunta)
    return respuesta

vidaDragon = 99
vidaJugador = 99

def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 5
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 5

while vidaDragon > 0 and vidaJugador > 0:
    materia = input("¿Que materia desea escoger entre estas?\n Inglés\n Matemáticas\n Cultural General\n")
    for i in range(7):
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