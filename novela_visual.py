import pygame
import sys

#Inicializador de Pygame

pygame.init()

#Sección de pruebas

ancho_pantalla = 640
alto_pantalla = 480
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Visual novel(Prueba)')

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
       self.select_index = 2

    def display(self):
        pantalla.fill(blanco)
        for index, item in enumerate(self.items):
            if index == self.select_index:
                texto_renderizado = fuente.render(f"> {item['mensaje']}", True, (255, 0, 0))
            else:
                texto_renderizado = fuente.render(f"> {item['mensaje']}", True, (0, 0, 0))
            pantalla.blit(texto_renderizado, (50, 50 + index * 40))


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
 

# Colores

blanco = (255, 255, 255)
negro = (0, 0, 0,)
rojo = (255, 0, 0) 

# Fuente y tamaño del texto
fuente = pygame.font.SysFont('Arial', 36)

# Mensajes

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

                menu.display()

                pygame.display.flip()

game_loop()
