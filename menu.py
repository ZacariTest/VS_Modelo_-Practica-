import pygame
import sys
from colores import blanco, negro, rojo, fuente
from display import ancho_pantalla, alto_pantalla, pantalla

#Inicializador de Pygame

pygame.init()

# Menu (Prueba)

class Menu:
    def __init__(self):
       self.items = [
        { "mensaje": "Iniciar",
         "action": self.start_game
        },
        { "mensaje": "Cargar",
         "action": self.load_progress
        },
        { "mensaje": "Salir",
         "action": self.exit_game
        },


    ]
       self.select_index = 0
       self.fondo_menu = pygame.image.load('imagenes/Portada.png')
       

    def display(self):
        pantalla.blit(self.fondo_menu, (0, 0))
 
        for index, item in enumerate(self.items):

            x_pos = ancho_pantalla * 0.1
            y_pos = alto_pantalla * (0.3 + index * 0.1)

            if index == self.select_index:
                texto_renderizado = fuente.render(f"> {item['mensaje']}", True, (255, 0, 0))
            else:
                texto_renderizado = fuente.render(f"> {item['mensaje']}", True, (0, 0, 0))

            pantalla.blit(texto_renderizado, (x_pos, y_pos))


    def select(self):
        action = self.items[self.select_index]["action"]
        action()
         

    def start_game(self):
        print("Bienvenido.")
        

    def load_progress(self):
        print("Progreso cargado.")

    def exit_game(self):
        print("nos vimos vampiro...")  
        pygame.quit()
        sys.exit()      
 
