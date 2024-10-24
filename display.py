import pygame
import sys
from colores import blanco, negro, rojo
import confi

#Inicializador de Pygame

pygame.init()

# prueba responsive

def responsive(ancho, alto, font_size):
    pantalla = pygame.display.set_mode((ancho, alto), pygame.NOFRAME)
