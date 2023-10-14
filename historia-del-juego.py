#FONDO CASTILLO#
Rect(0,0,400,400,relleno=gradiente('azulCieloClaro','azulAlica',inicio='superior'))
Rect(0,230,400,320,relleno=gradiente('verde','verdeMilitar',inicio='inferior'))

###Castillo###

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
    Poligono(100,160,155,160,125,100,relleno=gradiente('coral','marronCuero',inicio='izquierda')),
    Poligono(126,200,194,200,160,170,relleno=gradiente('coral','marronCuero',inicio='izquierda'))
    )
castillo.centroY-=70
castillo.opacidad=75

#PRINCESA
princesa= Grupo (
    Poligono(200,320,240,320,220,280,relleno='violeta'),
    Circulo(220,270,15,relleno='caqui'),
    )
    
Línea(260,263,290,263, anchuraDeLinea=20,guión=True,relleno='oro'),
Rect(260,263,35,13,relleno='oro')

princesa.centroX=280
princesa.centroY=300

principe= Grupo (
    Rect(280,280,20,40,relleno='rojo'),
    Circulo(290,270,15,relleno='caqui'),
    Línea(275,250,305,250, anchuraDeLinea=20,guión=True,relleno='oro'),
    Rect(275,250,30,13,relleno='oro')
    )
principe.centroX=320
principe.centroY=293

pergamino= Grupo(
    
    Rect(15,60,370,280,relleno=gradiente('mocasin','varillaDoradaPalida',inicio='superior'),opacidad=75),
    Rótulo('En una aldea muy lejana, se encuentra un gran castillo,',200,100,fuente='caveat',tamaño=19),
    Rótulo('vive una hermosa princesa y su enamorado el principe' ,200,120,fuente='caveat',tamaño=19),
    Rótulo('encantador.Esa tarde, todo transcurria con normalidad',200,140,fuente='caveat',tamaño=19),
    Rótulo('en la aldea, todos ejercian sus tareas;pero de repente...',200,160,fuente='caveat',tamaño=19),
    Rótulo('¡Un feroz dragón irrumpio con la tranquilidad del gran',200,180,fuente='caveat',tamaño=19),
    Rótulo('castillo! El principe al escuchar su desgarrador grito,',200,200,fuente='caveat',tamaño=19),
    Rótulo('que informaba que el dragon consiguió raptarla,',200,220,fuente='caveat',tamaño=19),
    Rótulo('de manera desesperada intenta encontrar una forma de',200,240,fuente='caveat',tamaño=19),
    Rótulo('salvar a su amada.',200,260,fuente='caveat',tamaño=19)
    )



