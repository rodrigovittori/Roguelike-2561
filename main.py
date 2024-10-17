#pgzero
import random

"""
Version actual: [M7.L2 · Actividad #2 "Generando enemigos"]
NOTA: La Actividad # 1 es actualizar el mapa de sueños
Objetivo del ejercicio: Agregar generación aleatoria de enemigos con atributos randomizados

Pasos:
#1: Importar random
#2: creamos una constante que determine la cantidad de enemigos a spawnear (5)
#3: Creamos un bucle FOR donde calculamos la posición, la validamos, creamos los actores enemigos y les asignamos su salud y ataque con valores randomizados
#4: Agregamos un bucle FOR en nuestro draw() para mostrar los enemigos en pantalla

Nota: Pronto calcularemos las colisiones contra ellos

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

cant_celdas_ancho = 9 # Ancho del mapa (en celdas)
cant_celdas_alto = 10 # Altura del mapa (en celdas)

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

################## VARIABLES ##################
CANT_ENEMIGOS_A_SPAWNEAR = 5

# Listas:
lista_enemigos = []

################## GENERAR ENEMIGOS ##################

# To-Do: migrar a función
for enemigo_a_spawnear in range(CANT_ENEMIGOS_A_SPAWNEAR):
    x = (random.randint(2, cant_celdas_ancho - 2) * celda.width)
    y = (random.randint(2, cant_celdas_alto - 3) * celda.height)
    # To-Do: Agregar variable para determinar tipo de enemigo a spawnear
    # To-do: agregar una posicion especifica para que spawnee el jugador
    
    nvo_enemigo = Actor("enemy", topleft = (x, y))

    # Checkeamos que no se repitan las coordenadas
    posicion_duplicada = False
    for enemigo in lista_enemigos:
        if (nvo_enemigo.pos == enemigo.pos): # Si la posición de nvo_enemigo es IGUAL a la de CUALQUIER enemigo en la lista,
            posicion_duplicada = True        # Actualizamos la flag que indica que la posicion está duplicada
    if (posicion_duplicada):
        enemigo_a_spawnear -= 1              # restamos 1 al iterando (del for ppal)
    else:
        nvo_enemigo.salud = random.randint(10, 20)
        nvo_enemigo.ataque = random.randint(5, 10)
        lista_enemigos.append(nvo_enemigo)

################## MAPAS ##################

mapa =   [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1] ] # Fila extra para mostrar el texto

mapa_2 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 1, 1, 1, 1, 1, 1, 1, 0], 
           [0, 1, 1, 3, 1, 3, 1, 1, 0], 
           [0, 1, 1, 3, 1, 3, 1, 1, 0], 
           [0, 1, 1, 1, 1, 1, 1, 1, 0], 
           [0, 3, 1, 1, 1, 1, 1, 3, 0], 
           [0, 1, 3, 1, 1, 1, 3, 1, 0], 
           [0, 1, 1, 3, 3, 3, 1, 1, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1] ] # Fila extra para mostrar el texto

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
    screen.fill("#2f3542") # rgb = (47, 53, 66)
    dibujar_mapa(mapa_actual)

    for enemigo in lista_enemigos:
      enemigo.draw()
    
    personaje.draw()

    # Mostramos valores personaje:
    screen.draw.text(("Salud: " + str(personaje.salud)), midleft=(30, (HEIGHT - int(celda.height/2))), color = 'white', fontsize = 24)
    screen.draw.text(("Ataque: " + str(personaje.ataque)), midright=((WIDTH - 30), (HEIGHT - int(celda.height/2))), color = 'white', fontsize = 24)


def on_key_down(key):
  
  if ((keyboard.right or keyboard.d) and (personaje.x < (WIDTH - celda.width * 2))):
    # ¿Xq 2?: Una (a la que me voy a desplazar) y otra (por la pared, que NO puedo atravesar)
    personaje.x += celda.width
    personaje.image = "stand" # xq stand mira a la dcha
        
  elif ((keyboard.left or keyboard.a) and (personaje.x > (celda.width * 2))):
    personaje.x -= celda.width
    personaje.image = "left" # xq mira a la izq
        
  elif ((keyboard.down or keyboard.s) and (personaje.y < HEIGHT - celda.height * 3)):
    # ¿Xq 3?: Una (a la que me voy a desplazar), otra (por la pared, que NO puedo atravesar) Y UNA TERCERA (para mostrar el texto)
    personaje.y += celda.height
    
  elif ((keyboard.up or keyboard.w) and (personaje.y > (celda.height * 2))):
        personaje.y -= celda.height