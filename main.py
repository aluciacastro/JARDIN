import pygame
from juego import Juego
def main():
    juego = Juego()
 
    while True:
        reiniciar = juego.ejecutar()
        
        if not reiniciar:
            break
            
        juego.inicializar_partida()
        
    pygame.quit()


if __name__ == "__main__":
    main()
