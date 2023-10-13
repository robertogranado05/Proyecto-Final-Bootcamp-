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

pregunta = ''
respuesta = ''
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

materia = input("¿Que materia desea escoger entre estas?\n Inglés\n Matemáticas\n Cultural General\n")
obtenerPregunta(materia)
