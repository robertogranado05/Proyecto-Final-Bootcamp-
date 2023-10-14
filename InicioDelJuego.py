from cmu_graphics import *
from cmu_graphics import cmu_graphics

#FONDO CASTILLO
Rect(0,0,400,400,relleno=gradiente('azulCieloClaro','azulAlica',inicio='superior'))
Rect(0,320,400,320,relleno=gradiente('verde','verdeMilitar',inicio='inferior'))

#CASTILLO

DragonMalo = Grupo(
    ##PATAS
    Poligono(170, 320, 130, 370, 130, 395, 170, 390, 170, 375,
    relleno=gradiente('carmesí', 'rojoOscuro')),
    Poligono(190, 320, 230, 370, 230, 395, 190, 390, 190, 360,
    relleno=gradiente('carmesí', 'rojoOscuro')),
    Poligono(130, 370, 120, 340, 143, 355, relleno=gradiente('carmesí', 'rojoOscuro', 'grisPizarraOscuro', inicio="inferior")),
    Poligono(230, 370, 240, 340, 217, 355, relleno=gradiente('carmesí', 'rojoOscuro', 'grisPizarraOscuro', inicio="inferior")),
    
    ##ALA IZQUIERDA
    Poligono(150, 250, 135, 235, 125, 220, 115, 205, 105, 180, 
    105, 80, 60, 125, 40, 160, 25, 205, 20, 230, 20, 255, 45,310,55, 245, 80, 310, 90, 255, 115, 325, 120,
    260, 140, 315, borde='grisPizarraOscuro', anchuraDeBorde=5, relleno=gradiente('cian', 'azulMedianoche', 'azulAcero')),
    ##Vena1
    Linea(80, 310, 74, 250, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(74, 250, 65, 190, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(65, 160, 80, 130, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(65, 190, 65, 160, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(80, 130, 105, 80, relleno=gradiente("rojo", 'rojoOscuro')),
    ##Vena2
    Linea(45, 310, 35, 245, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(45, 187, 55, 157, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(69, 125, 105, 80, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(35, 245, 45, 187, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(55, 157, 69, 125, relleno=gradiente("rojo", 'rojoOscuro')),
    ##Vena3
    Linea(115, 325, 105, 250, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(91, 188, 90, 165, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(90, 135, 105, 80, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(105, 250, 91, 188, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(90, 165, 90, 135, relleno=gradiente("rojo", 'rojoOscuro')),
    
    ##ALA DERECHA
    Poligono(210, 250, 225, 235, 235, 220, 245, 205, 255, 180, 255, 80, 300, 125, 320, 160, 335, 205, 340, 
    230, 340, 255, 315, 310, 305, 245, 280, 310, 270, 255, 245, 325, 240, 260, 220, 315,
    borde='grisPizarraOscuro', anchuraDeBorde=5, relleno=gradiente('cian', 'azulMedianoche', 'azulAcero')),
    
    ##Vena1
    Linea(280, 310, 286, 250, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(286, 250, 295, 190, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(295, 160, 280, 130, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(295, 190, 295, 160, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(280, 130, 255, 80, relleno=gradiente("rojo", 'rojoOscuro')),
    ##Vena2
    Linea(315, 310, 325, 245, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(315, 187, 305, 157, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(291, 125, 255, 80, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(325, 245, 315, 187, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(305, 157, 291, 125, relleno=gradiente("rojo", 'rojoOscuro')),
    ##Vena3
    Linea(245, 325, 255, 250, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(269, 188, 270, 165, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(270, 135, 255, 80, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(255, 250, 269, 188, relleno=gradiente("rojo", 'rojoOscuro')),
    Linea(270, 165, 270, 135, relleno=gradiente("rojo", 'rojoOscuro')),
    
    ##CUERPO
    Óvalo(180, 297, 80, 160, relleno=gradiente('carmesí', 'rojoOscuro')),
    Óvalo(180, 297, 65, 130, relleno=gradiente('rojo','carmesí', 'rojoOscuro')),
    
    ##Cuernos
    Poligono(120, 160, 125, 85, 160, 120, relleno=gradiente('tomate', 'rojoOscuro', inicio="inferior")),
    Poligono(240, 160, 240, 85, 200, 120, relleno=gradiente('tomate', 'rojoOscuro', inicio="inferior")),
    Poligono(200, 120, 200, 100, 185, 120, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
    Poligono(160, 120, 165, 100, 175, 120, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
    Poligono(119, 200, 110, 170, 130, 180, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
    Poligono(240, 200, 250, 170, 225, 180, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
    
    #CABEZA
    Poligono(160, 240, 119, 200, 130, 180, 120, 160, 160, 120, 200, 120, 240, 160, 225, 180, 240, 200, 200, 240, 
    relleno=gradiente('carmesí', 'rojoOscuro')),

    ##BOCA
    Óvalo(180, 200, 50, 20, relleno="rojoOscuro"),
    Poligono(154, 200, 206, 200, 200, 214, 190, 222, 170, 222, 160, 215, relleno="rojoOscuro"),
    Poligono(170, 222, 174, 205, 178, 222, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
    Poligono(190, 222, 185, 205, 180, 222, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
    Poligono(175, 190, 180, 210, 185, 190, relleno=gradiente("blanco", 'ladrillo', inicio="inferior")),
    Poligono(195, 190, 190, 208, 184, 190, relleno=gradiente("blanco", 'ladrillo', inicio="inferior")),
    Poligono(163, 190, 169, 210, 175, 190, relleno=gradiente("blanco", 'ladrillo', inicio="inferior")),
    Poligono(190, 222, 196, 204, 200, 215, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
    Poligono(169, 222, 163, 204, 160, 215, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
    
    ##OJOS
    Poligono(150, 145, 170, 175, 145, 160, relleno=gradiente('azulGandul','rojoOscuro', 'negro')),
    Poligono(210, 145, 190, 175, 215, 160, relleno=gradiente('azulGandul', 'rojoOscuro', 'negro')),
    Poligono(216, 165, 190, 185, 220, 173, relleno=gradiente('azulGandul', 'rojoOscuro', 'negro')),
    Poligono(144, 165, 170, 185, 140, 173, relleno=gradiente('azulGandul', 'rojoOscuro', 'negro')),
    )
DragonMalo.altura = 160
DragonMalo.ancho = 160
DragonMalo.centroX = 320
DragonMalo.centroY = 70

castillo=Grupo(
    Rect(0,160,50,170,relleno=gradiente('grisOscuro','grisTurbio',inicio='izquierda')),
    Rect(110,160,35,170,relleno=gradiente('grisOscuro','grisTurbio',inicio='izquierda')),
    Rect(135,200,50,130,relleno=gradiente('grisOscuro','grisTurbio',inicio='izquierda')),
    Rect(40,210,85,110,relleno='grisOscuro',borde='grisTurbio'),
    Rect(27,250,110,80,relleno='grisOscuro',borde='grisTurbio'),
    Rect(40,200,16,10,relleno='grisTurbio'),
    Rect(70,200,22,10,relleno='grisTurbio'),
    Rect(105,200,19,10,relleno='grisTurbio'),
    Poligono(60,160,0,80,0,160,relleno=gradiente('coral','marronCuero',inicio='izquierda')),
    Poligono(100,160,155,160,125,100,relleno=gradiente('coral','marrónCuero',inicio='izquierda')),
    Poligono(126,200,194,200,160,170,relleno=gradiente('coral','marrónCuero',inicio='superior')),
    
    #PRINCIPE
    Rect(280, 280, 20, 40, relleno='rojo'),
    Circulo(290, 270, 15, relleno="caqui"),
    Linea(275, 250, 305, 250, anchuraDeLinea=20, guion=True, relleno='oro'),
    Rect(275, 250, 30, 13, relleno='oro'),
    
    Ovalo(60,230,20,28,borde='marrónCuero'),
    Ovalo(105,230,20,28,borde='marrónCuero'),
    Rect(50,237,20,10,relleno='grisOscuro'),
    Rect(50,237,20,10,relleno='grisOscuro'),
    Rect(95,237,20,10,relleno='grisOscuro'),
    Rect(60,280,45,50,relleno='chocolate',borde='marronCuero'),
    Linea(83,280,83,330,relleno='marrónCuero'),
    
    Ovalo(160,225,20,30,borde='marrónCuero'),
    Ovalo(160,280,15,25,borde='marrónCuero'),
    Ovalo(18,195,25,40,borde='marrónCuero'),
    Ovalo(127,175,15,30,borde='marrónCuero'),
    Ovalo(45,270,10,15,borde='marrónCuero'),
    Ovalo(120,270,10,15,borde='marrónCuero'),
    Poligono(200,320,240,320,220,280,relleno='violeta'),
    Circulo(220,270,15,relleno='caqui')
    
)

cmu_graphics.run()