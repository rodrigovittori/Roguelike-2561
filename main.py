#pgzero

"""
Version actual: [M7.L1: Actividad #1]
Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

cant_celdas_ancho = 5 # Ancho del mapa (en celdas)
cant_celdas_alto = 5 # Altura del mapa (en celdas)

WIDTH =  celda.width  * cant_celdas_ancho # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * cant_celdas_alto  # Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorra Maldita" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

def draw():
    screen.fill((200,200,200))
    screen.draw.text(("Patrón celda: " + str(celda.image) + ".png"), center=(WIDTH/2, HEIGHT / 3 -50), color = "black", fontsize = 18)
    screen.draw.text(("Ancho: " + str(cant_celdas_ancho) + " casillas x " + str(celda.width) + " pixeles"), center=(WIDTH/2, HEIGHT / 3), color = "black", fontsize = 18)
    screen.draw.text(("Alto: " + str(cant_celdas_alto) + " casillas x " + str(celda.height) + " pixeles"), center=(WIDTH/2, HEIGHT / 2), color = "black", fontsize = 18)
    screen.draw.text(("Ventana de: " + str(WIDTH) + " x " + str(HEIGHT) + " px"), center=(WIDTH/2, HEIGHT / 3 * 2), color = "black", fontsize = 18)