
import pygame
from constantes import *
from jugador import Jugador
from ui import UI
from utils import *


class Juego:
   
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Jardín Mágico - Cuida tus plantas")
        self.reloj = pygame.time.Clock()
        self.ui = UI(self.pantalla)
        
    def inicializar_partida(self):
        self.jugador = Jugador()
        self.plantas = crear_plantas_iniciales()
        self.plagas = []
        self.tiempo_juego = 0
        self.regando = False
        self.planta_actual = None
        self.mensaje = ""
        self.tiempo_mensaje = 0
        
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
                
            if evento.type == pygame.KEYDOWN:
                self._manejar_tecla_presionada(evento.key)
                
            if evento.type == pygame.KEYUP:
                self._manejar_tecla_soltada(evento.key)
                
        return True
    
    def _manejar_tecla_presionada(self, tecla):
        if tecla == pygame.K_r:
            self.regando = True
            
        elif tecla == pygame.K_p:
            self._usar_pesticida()
            
        elif tecla == pygame.K_w:
            self._intentar_recargar_agua()
            
    def _manejar_tecla_soltada(self, tecla):
        if tecla == pygame.K_r:
            self.regando = False
            self.planta_actual = None
            
    def _usar_pesticida(self):
        if self.jugador.usar_pesticida():
            eliminadas = eliminar_plagas_cercanas(self.jugador, self.plagas)
            if eliminadas > 0:
                self.jugador.añadir_puntos(eliminadas * PUNTOS_POR_PLAGA)
                self.mensaje = f"¡Eliminaste {eliminadas} plagas!"
                self.tiempo_mensaje = 120
                
    def _intentar_recargar_agua(self):
        if verificar_cerca_pozo(self.jugador):
            self.jugador.recargar_agua()
            self.mensaje = "¡Agua recargada!"
            self.tiempo_mensaje = 90
            
    def actualizar(self):
        self.tiempo_juego += 1
        
        if self.tiempo_juego % INTERVALO_SPAWN_PLAGAS == 0:
            self.plagas.append(generar_plaga())
            
        # Mover jugador
        teclas = pygame.key.get_pressed()
        self.jugador.mover(teclas)
        
        # Regar plantas
        self._actualizar_riego()
        
        # Actualizar plantas
        self._actualizar_plantas()
        
        # Mover plagas y aplicar daño
        self._actualizar_plagas()
        
        # Reducir tiempo de mensaje
        if self.tiempo_mensaje > 0:
            self.tiempo_mensaje -= 1
            
    def _actualizar_riego(self):
        if self.regando and self.jugador.agua_disponible > 0:
            planta = verificar_riego(self.jugador, self.plantas)
            if planta and planta.esta_viva:
                if self.jugador.usar_agua():
                    planta.regar(1)
                    self.planta_actual = planta
                    
    def _actualizar_plantas(self):
        for planta in self.plantas:
            planta.actualizar()
            # Dar puntos por flores
            if planta.tiene_flor and self.tiempo_juego % 60 == 0:
                self.jugador.añadir_puntos(PUNTOS_POR_FLOR)
                
    def _actualizar_plagas(self):
        for plaga in self.plagas:
            plaga.mover()
            
        verificar_plagas_en_plantas(self.plagas, self.plantas)
        
    def dibujar(self):
        self.ui.dibujar_escena()
        self.ui.dibujar_pozo()

        for planta in self.plantas:
            planta.dibujar(self.pantalla)

        for plaga in self.plagas:
            plaga.dibujar(self.pantalla)
        self.jugador.dibujar(self.pantalla)

        if self.regando and self.planta_actual:
            self.ui.dibujar_efecto_riego(self.jugador.x, self.jugador.y)
            
        plantas_vivas = contar_plantas_vivas(self.plantas)
        self.ui.dibujar_hud(self.jugador, plantas_vivas)
        
        if self.tiempo_mensaje > 0:
            self.ui.mostrar_mensaje_temporal(self.mensaje, self.tiempo_mensaje)
            
        pygame.display.flip()
        
    def verificar_game_over(self):
        """Verifica si el juego terminó"""
        plantas_vivas = contar_plantas_vivas(self.plantas)
        if plantas_vivas == 0:
            return True, plantas_vivas
        return False, plantas_vivas
        
    def ejecutar(self):
        if not self.ui.mostrar_menu_principal():
            return False
            
        self.inicializar_partida()
        jugando = True
        while jugando:
            self.reloj.tick(FPS)
            
            if not self.manejar_eventos():
                return False
                
            self.actualizar()
            
            self.dibujar()
            
            termino, plantas_vivas = self.verificar_game_over()
            if termino:
                continuar, reiniciar = self.ui.mostrar_pantalla_final(
                    self.jugador.puntos, plantas_vivas)
                return reiniciar
                
        return False
