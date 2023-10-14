from cmu_graphics import *
from cmu_graphics import cmu_graphics
import random
import seleccionDeActividades as select
from seleccionDeActividades import botones
import BatallaElecciones as pantallaElección

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

opcionesIngles = [['Hosing', 'House', 'Tree'], 
                  ['Audi', 'Wheel', 'Car'],
                  ['Mom', 'Mami', 'Nana'],
                  ['Apple', 'Mango', 'Apol'],
                  ['Habitation', 'Room', 'Living'],
                  ['Sweet', 'Sour', 'Sugar']]

opcionesMates = [['9', '3', 'No tiene'],
                 ['4', '2', '7'],
                 ['16', '70', '8'],
                 ['80', '60', '100'],
                 ['24', '38', '12'],
                 ['3', '180', '360'],
                 ['6', '2', '8']]

opcionesGeneral = [['365', '206', '50'],
                   ['2004', '1845', '1945'],
                   ['7 de agosto', '1 de Enero', '20 de julio'],
                   ['1492', '1955', '2018'],
                   ['China', 'Rusia', 'Colombia'],
                   ['Ballena azul', 'Elefante', 'Hormiga'],
                   ['Cali', 'Bogotá', 'Buenaventura']]

pregunta = ''
preguntasUsadas = list()
opciones = list()
respuesta = ''
fila = 0

# Toma un parametro con el nombre de la materia o conjunto de palabras
def obtenerPregunta(lista):
    global rotuloPregunta, pregunta, opciones, respuesta, fila
    lista.lower()
    #Compara el parametro con las listas existentes
    if lista == 'ingles':
        #Obtiene un valor aleatorio de fila y toma una pregunta y su respuesta
        fila = random.randint(0, len(ingles) - 1)
        opciones = opcionesIngles[fila]
        pregunta = ingles[fila][0]     
        respuesta = ingles[fila][1]
    elif lista == 'matematicas':
        fila = random.randint(0, len(mates) - 1)
        opciones = opcionesMates[fila]
        pregunta = mates[fila][0]
        respuesta = mates[fila][1]
    elif lista == 'cultura general':
        fila = random.randint(0, len(general) - 1)
        opciones = opcionesGeneral[fila]
        pregunta = general[fila][0]     
        respuesta = general[fila][1]
    
    rotuloPregunta.valor = pregunta
    if pregunta in preguntasUsadas:
        pass
    else:
        print(pregunta)
    preguntasUsadas.append(pregunta)

    if lista == 'ingles':
        ingles.remove(ingles[fila])
    elif lista == 'matematicas':
        mates[fila].remove(pregunta)
    elif lista == 'cultura general':
        general[fila].remove(pregunta)

    return respuesta

vidaDragon = 100
vidaJugador = 100

def obtenerOpciones():
    print('a)', opciones[0])
    print('b)', opciones[1])
    print('c)', opciones[2])

def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 5
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 5

def luchar(materia):
    while vidaDragon > 0 and vidaJugador > 0:
        for i in range(7):
            respuesta = obtenerPregunta(materia)
            obtenerOpciones()
            respuestaJugador = input()
            comprobarVictoria(respuestaJugador, respuesta)

            print(f"El jugador tiene: {vidaJugador} de vida")
            print(f"El dragón tiene: {vidaDragon} de vida")

def onMousePress(x, y):
    for boton in botones:
        if boton.toca(x, y):
            # luchar(boton.nombre)
            pantallaElección.dibujarBatalla()


if vidaDragon == 0:
    print("Tú ganas")
elif vidaJugador == 0:
    print("El dragón gana")

cmu_graphics.run()