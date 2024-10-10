#pgzero

"""
Version actual: [M7.L1 · Actividad #3: "Bucles anidados" ]
Objetivo del ejercicio: Implementar bucles for anidados que dibujen nuestro mapa

Paso Nº 1: Crear los Actores que contienen nuestros tipos de casillas
Paso Nº 2: Crear mi Función dibujar_mapa(mapa) que convierte los datos de una tabla (mapa) en los gráficos de nuestro nivel
Paso Nº 3: Crear una variable que almacene la habitación actual
Paso Nº 4: Eliminamos el código del draw() que nos mostraba el tamaño de la pantalla
Paso Nº 5: Agregamos nuestro update(dt)

Nota: en el próximo ejercicio es que se crean los actores para dibujar

Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
    > Para redimensionar assets https://imageresizer.com/bulk-resize/
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

""" ******************************************************************* """

# Paleta de terrenos:
pared =  Actor("border") # 0: Pared de bloques
piso =   Actor("floor")  # 1: Suelo liso (sin decoración)
crack =  Actor("crack")  # 2: Suelo resquebrajado/quebradizo
huesos = Actor("bones")  # 3: Suelo con una pilita de huesos

""" ******************************************************************* """

cant_celdas_ancho = 7 # Ancho del mapa (en celdas)
cant_celdas_alto = 7 # Altura del mapa (en celdas)

WIDTH =  celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorra Maldita" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

################## MAPAS ##################

mapa = [ [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 1, 3, 1, 0],
         [0, 1, 1, 2, 1, 1, 0],
         [0, 3, 2, 1, 1, 3, 0],
         [0, 1, 1, 1, 3, 1, 0],
         [0, 1, 3, 1, 1, 2, 0],
         [0, 0, 0, 0, 0, 0, 0] ]

mapa_2 = [ [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 3, 1, 1, 0],
           [0, 1, 3, 1, 3, 1, 0],
           [0, 3, 1, 1, 1, 3, 0],
           [0, 3, 1, 1, 1, 3, 0],
           [0, 1, 3, 3, 3, 1, 0],
           [0, 0, 0, 0, 0, 0, 0] ]

##########################################

mapa_actual = mapa # mapa a dibujar // cambiar valor si cambiamos de habitación

### FUNCIONES PROPIAS ###

def dibujar_mapa(mapa):

  for fila in range(len(mapa)):
    for columna in range(len(mapa[fila])):

      """
      Lista códigos terrenos
      
      0: pared
      1: piso (sin nada)
      2: piso (roto/resquebrajado)
      3: piso (c/ huesitos)
      """

      if (mapa[fila][columna] == 0): # pared
        pared.left = pared.width * columna
        pared.top = pared.height * fila
        pared.draw()

      elif (mapa[fila][columna] == 1): # piso (sin nada)
        piso.left = piso.width * columna
        piso.top = piso.height * fila
        piso.draw()

      elif (mapa[fila][columna] == 2): # piso (roto/resquebrajado)
        crack.left = crack.width * columna
        crack.top = crack.height * fila
        crack.draw()

      elif (mapa[fila][columna] == 3): # piso (c/ huesitos)
        huesos.left = huesos.width * columna
        huesos.top = huesos.height * fila
        huesos.draw()
    
    # Agregar texto?

### FUNCIONES PG-ZERO ###

def draw():
    #screen.fill((200,200,200))
        
    screen.draw.text(("  Ventana de " + str(cant_celdas_ancho) + " x " + str(cant_celdas_alto) + "  "), center=(WIDTH/2, int(celda.height /2)), color = "white", background = "black", fontsize = int(celda.height /2))

    screen.draw.text("Pulse [Espacio] para alternar el diseño del mapa", center=(WIDTH/2, ((cant_celdas_alto * celda.height) - int(celda.height /2))), color = "white", background = "black", fontsize = int(celda.height /3))

""" >>> Probamos dibujar mapa <<< """

def update(dt):
    global mapa_actual
    
    if keyboard.space:
        if mapa_actual == mapa:
            mapa_actual = mapa_2
        else:
            mapa_actual = mapa

    dibujar_mapa(mapa_actual)