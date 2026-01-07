
import math
import random
from constantes import *
from planta import Planta
from plaga import Plaga


def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def crear_plantas_iniciales():
    plantas = []
    for x in POSICIONES_PLANTAS_X:
        tipo = random.randint(1, 3)
        planta = Planta(x, ALTO - 120, tipo)
        plantas.append(planta)
    return plantas


def generar_plaga():
    x = random.randint(50, ANCHO - 50)
    y = random.randint(ALTO // 2, ALTO - 150)
    return Plaga(x, y)


def verificar_riego(jugador, plantas, distancia_maxima=40):
    for planta in plantas:
        if not planta.esta_viva:
            continue
            
        distancia = calcular_distancia(jugador.x, jugador.y, 
                                       planta.x, planta.y)
        if distancia < distancia_maxima:
            return planta
    return None


def verificar_plagas_en_plantas(plagas, plantas):
    for plaga in plagas:
        for planta in plantas:
            if not planta.esta_viva:
                continue
                
            distancia = calcular_distancia(plaga.x, plaga.y, 
                                          planta.x, planta.y)
            if distancia < 30:
                planta.recibir_daño(DAÑO_PLAGA)


def eliminar_plagas_cercanas(jugador, plagas, radio=60):
    eliminadas = 0
    for plaga in plagas[:]:
        distancia = calcular_distancia(jugador.x, jugador.y, 
                                       plaga.x, plaga.y)
        if distancia < radio:
            plagas.remove(plaga)
            eliminadas += 1
    return eliminadas


def contar_plantas_vivas(plantas):
    return sum(1 for planta in plantas if planta.esta_viva)


def verificar_cerca_pozo(jugador, distancia_maxima=50):
    pozo_x, pozo_y = POSICION_POZO
    distancia = calcular_distancia(jugador.x, jugador.y, pozo_x, pozo_y)
    return distancia < distancia_maxima
