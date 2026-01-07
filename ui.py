import pygame
from constantes import *


class UI:   
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 28)
        self.fuente_grande = pygame.font.Font(None, 32)
        self.reloj = pygame.time.Clock()
        
    def mostrar_menu_principal(self):
        en_menu = True
        
        while en_menu:
            self.pantalla.fill(CIELO)
            #  menú
            titulo = self.fuente_grande.render("JUEGO DEL JARDÍN", True, MORADO)
            inst1 = self.fuente.render("Cuida tus plantas para que crezcan y florezcan", 
                                      True, NEGRO)
            inst2 = self.fuente.render("FLECHAS: Mover  |   R: Regar   |   P: Pesticida   |   W: Pozo",
                                        True, NEGRO)
            inst3 = self.fuente.render("Las plantas necesitan agua constante", 
                                      True, VERDE_OSCURO)
            inst4 = self.fuente.render("Elimina las plagas antes que dañen tus plantas", 
                                      True, ROJO_PLAGA)
            inicio = self.fuente_grande.render("-> PRESIONA ESPACIO PARA EMPEZAR <-", True, VERDE_PLANTA)
            
            # Dibujar textos
            self.pantalla.blit(titulo, (ANCHO//2 - 200, 100))
            self.pantalla.blit(inst1, (ANCHO//2 - 280, 220))
            self.pantalla.blit(inst2, (ANCHO//2 - 300, 280))
            self.pantalla.blit(inst3, (ANCHO//2 - 230, 340))
            self.pantalla.blit(inst4, (ANCHO//2 - 270, 380))
            self.pantalla.blit(inicio, (ANCHO//2 - 240, 500))
            
            pygame.display.flip()
            
            # Manejar eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return True
            
            self.reloj.tick(30)
        
        return False
    
    def mostrar_pantalla_final(self, puntos, plantas_vivas):
        en_pantalla = True
        
        while en_pantalla:
            self.pantalla.fill(CIELO)
            
            # Determinar mensaje según resultado
            if plantas_vivas > 0:
                texto1 = self.fuente_grande.render("¡FELICITACIONES!", 
                                                   True, VERDE_PLANTA)
                texto2 = self.fuente.render(f"Mantuviste vivas {plantas_vivas} plantas", 
                                           True, NEGRO)
            else:
                texto1 = self.fuente_grande.render("GAME OVER", True, ROJO_PLAGA)
                texto2 = self.fuente.render("Todas tus plantas murieron", True, NEGRO)
                
            texto3 = self.fuente.render(f"Puntos totales: {puntos}", True, MORADO)
            texto4 = self.fuente.render("ESPACIO - Jugar de nuevo | ESC - Salir", 
                                       True, NEGRO)
            
            # Dibujar textos
            self.pantalla.blit(texto1, (ANCHO//2 - 200, 200))
            self.pantalla.blit(texto2, (ANCHO//2 - 200, 280))
            self.pantalla.blit(texto3, (ANCHO//2 - 120, 340))
            self.pantalla.blit(texto4, (ANCHO//2 - 250, 450))
            
            pygame.display.flip()
           
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False, False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return True, True
                    if evento.key == pygame.K_ESCAPE:
                        return False, False
                        
            self.reloj.tick(30)
    
    def dibujar_escena(self):
        # Cielo
        self.pantalla.fill(CIELO)
        
        # Suelo
        pygame.draw.rect(self.pantalla, TIERRA, (0, ALTO - 100, ANCHO, 100))
        
    def dibujar_pozo(self):
        pozo_x, pozo_y = POSICION_POZO
        
        # Círculo externo
        pygame.draw.circle(self.pantalla, GRIS_OSCURO, 
                          (pozo_x, pozo_y), RADIO_POZO)
        # Agua interior
        pygame.draw.circle(self.pantalla, AZUL_AGUA, 
                          (pozo_x, pozo_y), RADIO_POZO - 10)
        # Letra W
        texto_pozo = self.fuente.render("W", True, BLANCO)
        self.pantalla.blit(texto_pozo, (pozo_x - 8, pozo_y - 12))
        
    def dibujar_efecto_riego(self, jugador_x, jugador_y):
        import random
        for i in range(5):
            x_gota = jugador_x + random.randint(-10, 10)
            y_gota = jugador_y + 10 + i * 8
            pygame.draw.circle(self.pantalla, AZUL_AGUA, (x_gota, y_gota), 3)
            
    def dibujar_hud(self, jugador, plantas_vivas):
        # Estadísticas del jugador
        texto_agua = self.fuente.render(f"Agua: {jugador.agua_disponible}%", 
                                        True, AZUL_AGUA)
        texto_pesticida = self.fuente.render(f"Pesticida: {jugador.pesticida}", 
                                             True, ROJO_PLAGA)
        texto_puntos = self.fuente.render(f"Puntos: {jugador.puntos}", 
                                         True, MORADO)
        texto_vivas = self.fuente.render(f"Plantas: {plantas_vivas}/5", 
                                        True, VERDE_PLANTA)
        
        self.pantalla.blit(texto_agua, (ANCHO - 180, 10))
        self.pantalla.blit(texto_pesticida, (ANCHO - 180, 40))
        self.pantalla.blit(texto_puntos, (ANCHO - 180, 70))
        self.pantalla.blit(texto_vivas, (ANCHO - 180, 100))
        
    def mostrar_mensaje_temporal(self, mensaje, tiempo_restante):
        if tiempo_restante > 0:
            texto = self.fuente.render(mensaje, True, AMARILLO)
            # Fondo oscuro para el mensaje
            pygame.draw.rect(self.pantalla, NEGRO, 
                           (ANCHO//2 - 150, 200, 300, 40))
            self.pantalla.blit(texto, (ANCHO//2 - 140, 210))
