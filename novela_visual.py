import pygame
import sys
from colores import blanco, negro, rojo  # Importa solo colores
from confi import ancho_pantalla, alto_pantalla, pantalla, fuente  # Importa 'fuente' desde 'confi'
from menu import Menu 

# Inicializador de Pygame
pygame.init()

# Bucle del juego
def game_loop():
    menu = Menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and menu.select_index < len(menu.items) - 1:
                    menu.select_index += 1
                if event.key == pygame.K_UP and menu.select_index > 0:
                    menu.select_index -= 1

                if event.key == pygame.K_RETURN:
                    if menu.items[menu.select_index]['mensaje'] == 'Iniciar':
                        texto = fuente.render("nos vimos vampiro...", True, (255, 0, 0))
                        pantalla.fill(blanco)
                        pantalla.blit(texto, (100, 200))
                        pygame.display.flip()
                        pygame.time.wait(2000)

                    if menu.items[menu.select_index]['mensaje'] == 'Salir':
                        texto = fuente.render("nos vimos vampiro...", True, (255, 0, 0))
                        pantalla.blit(texto, (100, 200))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        pygame.quit()
                        sys.exit()

            menu.display()
            pygame.display.flip()

game_loop()
