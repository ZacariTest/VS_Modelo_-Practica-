import pygame
from colores import blanco, negro, rojo
import confi

# Inicializador de Pygame
pygame.init()

# prueba responsive
def responsive(ancho, alto):
    pantalla = pygame.display.set_mode((ancho, alto), pygame.NOFRAME)
