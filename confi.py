import pygame
from colores import blanco, negro, rojo

# Fuente y tamaño del texto

font_size = 36
fuente = pygame.font.SysFont('Arial', font_size)

# pantalla

ancho_pantalla = 1024
alto_pantalla = 512
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla), pygame.NOFRAME)
pygame.display.set_caption('Visual novel(Prueba)')


# prueba responsive

def set_resolution(ancho, alto):
    global pantalla  # Usar global para modificar la variable en el ámbito global
    pantalla = pygame.display.set_mode((ancho, alto), pygame.NOFRAME)

""""
def set_resolution(ancho, alto):
    pantalla = pygame.display.set_mode((ancho, alto), pygame.NOFRAME)
    font_size 
"""