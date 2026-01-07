import pygame
import random
import math
from constantes import *


class Planta:
   
    def __init__(self, x, y, tipo=1):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.agua = AGUA_INICIAL_PLANTA
        self.felicidad = FELICIDAD_INICIAL
        self.tamaño = TAMAÑO_INICIAL
        self.crecimiento = 0
        self.esta_viva = True
        self.tiempo_sin_agua = 0
        self.tiene_flor = False
        self.color_flor = self._elegir_color_aleatorio()
        
    def _elegir_color_aleatorio(self):
        colores = [(255, 0, 127), (255, 215, 0), (138, 43, 226), (255, 69, 0)]
        return random.choice(colores)
        
    def actualizar(self):
        if not self.esta_viva:
            return
            
        self._consumir_agua()
        self._actualizar_felicidad()
        self._crecer()
        self._verificar_muerte()
        self._limitar_valores()
        
    def _consumir_agua(self):
        self.tiempo_sin_agua += 1
        if self.tiempo_sin_agua >= INTERVALO_CONSUMO:
            self.agua -= CONSUMO_AGUA
            self.tiempo_sin_agua = 0
            
    def _actualizar_felicidad(self):
        if self.agua <= 0:
            self.felicidad -= 2
            self.agua = 0
            
    def _crecer(self):
        if self.felicidad > 50 and self.agua > 30:
            self.crecimiento += 0.5
            if self.crecimiento >= 100:
                self.tamaño += 5
                self.crecimiento = 0
                if self.tamaño >= 60:
                    self.tiene_flor = True
                    
    def _verificar_muerte(self):
        if self.felicidad <= 0:
            self.esta_viva = False
            
    def _limitar_valores(self):
        self.agua = min(self.agua, 100)
        self.felicidad = min(self.felicidad, 100)
            
    def regar(self, cantidad=30):
        self.agua += cantidad
        if self.agua > 100:
            self.agua = 100
            
    def recibir_daño(self, cantidad=1):
        self.felicidad -= cantidad
            
    def curar(self, cantidad=20):
        self.felicidad += cantidad
        if self.felicidad > 100:
            self.felicidad = 100
            
    def dibujar(self, pantalla):
        if not self.esta_viva:
            self._dibujar_muerta(pantalla)
            return
            
        self._dibujar_tallo(pantalla)
        self._dibujar_hojas(pantalla)
        
        if self.tiene_flor:
            self._dibujar_flor(pantalla)
            
        self._dibujar_barra_agua(pantalla)
        
    def _dibujar_muerta(self, pantalla):
        pygame.draw.line(pantalla, VERDE_OSCURO, 
                        (self.x, self.y), 
                        (self.x + 10, self.y + 20), 3)
        pygame.draw.circle(pantalla, NEGRO, (self.x + 5, self.y - 5), 8)
        
    def _dibujar_tallo(self, pantalla):
        altura_tallo = self.tamaño
        pygame.draw.line(pantalla, VERDE_PLANTA,
                        (self.x, self.y), 
                        (self.x, self.y - altura_tallo), 4)
        
    def _dibujar_hojas(self, pantalla):
        altura_tallo = self.tamaño
        num_hojas = max(2, self.tamaño // 15)
        
        for i in range(num_hojas):
            y_hoja = self.y - (i * altura_tallo // num_hojas) - 10
            # Hoja izquierda
            pygame.draw.ellipse(pantalla, VERDE_PLANTA,
                              (self.x - 10, y_hoja - 5, 15, 10))
            # Hoja derecha
            pygame.draw.ellipse(pantalla, VERDE_PLANTA,
                              (self.x, y_hoja - 5, 15, 10))
                              
    def _dibujar_flor(self, pantalla):
        centro_flor_y = self.y - self.tamaño - 10
        
        # Pétalos alrededor
        for angulo in range(0, 360, 45):
            rad = math.radians(angulo)
            x_petalo = self.x + math.cos(rad) * 12
            y_petalo = centro_flor_y + math.sin(rad) * 12
            pygame.draw.circle(pantalla, self.color_flor, 
                             (int(x_petalo), int(y_petalo)), 8)
        
        # Centro amarillo
        pygame.draw.circle(pantalla, AMARILLO, (self.x, centro_flor_y), 6)
        
    def _dibujar_barra_agua(self, pantalla):
        barra_x = self.x - 15
        barra_y = self.y + 10
        barra_ancho = 30
        barra_alto = 5
        
        # Marco
        pygame.draw.rect(pantalla, NEGRO, 
                        (barra_x, barra_y, barra_ancho, barra_alto), 1)
        
        # Relleno según nivel de agua
        ancho_agua = int((self.agua / 100) * barra_ancho)
        color_barra = AZUL_AGUA if self.agua > 30 else ROJO_PLAGA
        pygame.draw.rect(pantalla, color_barra, 
                        (barra_x, barra_y, ancho_agua, barra_alto))
