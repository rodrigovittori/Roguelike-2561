#pgzero

"""
Version actual: [M7.L1 · Actividad #5: "Atributos"]
Objetivo del ejercicio: Familiarizarnos con los atributos agregand salud y ataque a nuestro personaje
> Creamos nuestro personaje como un objeto Actor() con sus respectivos atributos y los mostramos por pantalla

NOTA: La actividad #4 fue resuelta con el código de la actividad #3

Pasos:
#1: Creamos Actor() personaje
#2: Le damos sus atributos
#3: Eliminamos update() y modificamos nuestra función draw()

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

""" ******************************************************************* """

# Personaje:

personaje = Actor("stand")
# Nota: si quieren llevar control de la vida, pueden crear dos atributos: "salud_max" y "salud_actual"
personaje.salud = 100
# Nota: si quieren hacer más interesante el combate pueden agregar atributos para el valor mínimo de ataque y el máximo
#       (también pueden implementar un sistema de miss y critical hits)
personaje.ataque = 5

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

""" #####################
   # FUNCIONES PG-ZERO #
  #####################  """

def draw():
    #screen.fill((200,200,200))
    dibujar_mapa(mapa_actual)

    personaje.draw()

    # Mostramos valores personaje:
    screen.draw.text(("PS: " + str(personaje.salud)), midright=((WIDTH - 15), 14), color = 'white', fontsize = 16)
    screen.draw.text(("ATK: " + str(personaje.ataque)), midright=((WIDTH - 15), 36), color = 'white', fontsize = 16)