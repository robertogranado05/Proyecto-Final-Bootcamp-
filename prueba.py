import random

ingles = [['Como se dice casa', 'House'], 
            ['como se dice carro', 'car'], 
            ['como se dice mamá', 'Mom']]
mates = [['Cual es la raíz cuadrada de 9', '3'], 
        ['cuantos es dos más dos', '4'], 
        ['cuantos es 2 X 4', '8']]
general = [['¿Cuantos huesos tiene el cuerpo humano?', '206'], 
            ['¿Cuanto acabó la segunda guerra mundial', '1945'], 
            ['¿En que fecha se celebra la independencia en Colombia?', '20 de Julio']
            ]

listaElegida = list()

def obtenerPregunta(lista):
    # for lista in listaDePreguntas:
    lista.lower()
    if lista == 'ingles':
        fila = random.randint(0, 2)
        pregunta = ingles[fila][0]            
        respuesta = ingles[fila][1]
    elif lista == 'matematicas':
        fila = random.randint(0, 2)
        pregunta = mates[fila][0]            
        respuesta = mates[fila][1]
    elif lista == 'cultura general':
        fila = random.randint(0, 2)
        pregunta = general[fila][0]            
        respuesta = general[fila][1]
    
    print(pregunta)
    return respuesta

vidaDragon = 99
vidaJugador = 99

def comprobarVictoria(rJugador, r):
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon -= 11
    else:
        print("Incorrecto")
        vidaJugador -= 11

while vidaDragon > 0 and vidaJugador > 0:
    materia = input("¿Que materia desea escoger entre estas?\n Inglés\n Matemáticas\n Cultural General\n")
    respuesta = obtenerPregunta(materia)
    respuestaJugador = input()

    comprobarVictoria(respuestaJugador, respuesta)

    print("El jugador tiene: {vidaJugador} de vida".format())
    print("El dragón tiene: {vidaDragon} de vida".format())
    # print(r)
    # print(rJugador)

if vidaDragon == 0:
    print("Tú ganas")
elif vidaJugador == 0:
    print("El dragón gana")