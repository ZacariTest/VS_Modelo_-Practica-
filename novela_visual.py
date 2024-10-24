import pygame
import sys
from colores import blanco, negro, rojo, fuente
from menu import Menu 
from display import ancho_pantalla, alto_pantalla, pantalla

#Inicializador de Pygame

pygame.init()

# Bucle del juego

def game_loop():
    indice_mensaje = 0
    menu = Menu()
    while True:
           for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_DOWN:
                    if menu.select_index < len(menu.items)-1:
                        menu.select_index =  menu.select_index + 1
                if event.key == pygame.K_UP:
                    if menu.select_index > 0: #MENOR O IGUAL
                        menu.select_index = menu.select_index - 1

                if event.key == pygame.K_RETURN:
                    if menu.items[menu.select_index]['mensaje'] == 'Iniciar':
                                texto = fuente.render("nos vimos vampiro...", True, (255, 0, 0))
                            
                                pantalla.fill(blanco)
                                pantalla.blit(texto, (100, 200))
                                pygame.display.flip()
                                pygame.time.wait(2000)

                if event.key == pygame.K_RETURN:
                    if menu.items[menu.select_index]['mensaje'] == 'Salir':
                                texto = fuente.render("nos vimos vampiro...", True, (255, 0, 0))
                                # igual aqui ponemos otra imagen despues pantalla.fill(blanco)
                                pantalla.blit(texto, (100, 200))
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                pygame.quit()
                                sys.exit()     
                    """
                    fuente.render() para convertir texto en imágenes.
                    pantalla.blit() para dibujar esas imágenes en la pantalla.
                    pygame.display.flip() para actualizar la ventana.
                    pygame.time.wait() para pausar el juego si quieres mostrar algo por un tiempo.
                    """


            menu.display()

            pygame.display.flip()

game_loop()
