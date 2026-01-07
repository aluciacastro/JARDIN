import pygame
from constantes import *


class Jugador:
    def __init__(self):
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.velocidad = VELOCIDAD_JUGADOR
        self.agua_disponible = AGUA_INICIAL_JUGADOR
        self.puntos = 0
        self.pesticida = PESTICIDA_INICIAL
        
    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 20:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x < ANCHO - 20:
            self.x += self.velocidad
        if teclas[pygame.K_UP] and self.y > 20:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.y < ALTO - 20:
            self.y += self.velocidad
            
    def usar_agua(self, cantidad=1):
        if self.agua_disponible >= cantidad:
            self.agua_disponible -= cantidad
            return True
        return False
            
    def recargar_agua(self):
        self.agua_disponible = AGUA_INICIAL_JUGADOR
        
    def usar_pesticida(self):
        if self.pesticida > 0:
            self.pesticida -= 1
            return True
        return False
        
    def añadir_puntos(self, cantidad):
        self.puntos += cantidad
        
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, GRIS, 
                        (self.x - 10, self.y - 8, 20, 16))
        
        pygame.draw.line(pantalla, GRIS_OSCURO, 
                        (self.x + 10, self.y), 
                        (self.x + 20, self.y - 5), 3)
        
        pygame.draw.circle(pantalla, GRIS, (self.x + 20, self.y - 5), 5)
