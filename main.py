#pgzero

"""
Version actual: [M7.L1 · Actividad #2: "Creando un mapa" ]
Objetivo del ejercicio: comprender como modificar el tamaño del mapa y como vamos a cargar nuestros mapas (tablas)

Paso Nº 1: Modificar las variables que definen la cant de casillas horiz y vert
Paso Nº 2: Crear una "tabla" (lista de listas) que represente nuestro mapa

Nota: en el próximo ejercicio es que se crean los actores para dibujar
> Para redimensionar assets https://imageresizer.com/bulk-resize/

Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

cant_celdas_ancho = 7 # Ancho del mapa (en celdas)
cant_celdas_alto = 7 # Altura del mapa (en celdas)

WIDTH =  celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorra Maldita" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

mapa = [ [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 1, 3, 1, 0],
         [0, 1, 1, 2, 1, 1, 0],
         [0, 3, 2, 1, 1, 3, 0],
         [0, 1, 1, 1, 3, 1, 0],
         [0, 1, 3, 1, 1, 2, 0],
         [0, 0, 0, 0, 0, 0, 0] ]

def draw():
    screen.fill((200,200,200))
    screen.draw.text(("Patrón celda: " + str(celda.image) + ".png"), center=(WIDTH/2, HEIGHT / 3 -50), color = "black", fontsize = 18)
    screen.draw.text(("Ancho: " + str(cant_celdas_ancho) + " casillas x " + str(celda.width) + " pixeles"), center=(WIDTH/2, HEIGHT / 3), color = "black", fontsize = 18)
    screen.draw.text(("Alto: " + str(cant_celdas_alto) + " casillas x " + str(celda.height) + " pixeles"), center=(WIDTH/2, HEIGHT / 2), color = "black", fontsize = 18)
    screen.draw.text(("Ventana de: " + str(WIDTH) + " x " + str(HEIGHT) + " px"), center=(WIDTH/2, HEIGHT / 3 * 2), color = "black", fontsize = 18)