from cmu_graphics import *

#CASTILLO
imagen= Imagen('cmu://612287/25324480/castillo2.jpg', -30, 160)

imagen.ancho = 280
imagen.altura = 239
imagen.centroY = 227
imagen.centroX = 100

#CAMINO
Rect(0, 320, 400, 320, relleno=gradiente('marVerde', 'marVerdeOscuro'))
Poligono(80, 320, 80, 340, 80, 358, 100, 375, 97, 400, 135, 400, 130, 357, 115, 320,
relleno=gradiente('varillaDoradaClaraAmarilla', 'varillaDoradaPálida', inicio="inferior"))
