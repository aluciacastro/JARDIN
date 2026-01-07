
import pygame
import random
from constantes import *


class Plaga:
   
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad_x = random.choice([-2, -1, 1, 2])
        self.velocidad_y = random.choice([-1, 1])
        self.tamaño = TAMAÑO_PLAGA
        self.viva = True
        
    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        
        if self.x < 0 or self.x > ANCHO:
            self.velocidad_x *= -1
            
        if self.y < ALTO // 2 or self.y > ALTO - 100:
            self.velocidad_y *= -1
            
    def dibujar(self, pantalla):
        # Cuerpo principal
        pygame.draw.circle(pantalla, ROJO_PLAGA, 
                          (int(self.x), int(self.y)), self.tamaño)
        
        # Ojos
        pygame.draw.circle(pantalla, AMARILLO, 
                          (int(self.x - 3), int(self.y - 2)), 2)
        pygame.draw.circle(pantalla, AMARILLO, 
                          (int(self.x + 3), int(self.y - 2)), 2)
        
        # Patas
        for i in range(3):
            x_pata = int(self.x - 6 + i * 6)
            y_inicio = int(self.y + self.tamaño)
            y_fin = int(self.y + self.tamaño + 5)
            pygame.draw.line(pantalla, NEGRO, 
                           (x_pata, y_inicio), (x_pata, y_fin), 2)
