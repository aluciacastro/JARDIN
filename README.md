# Jardín 

Es un juego donde manejas una regadera para regar plantas. Las plantas van creciendo si las cuidas bien, pero hay bichos que las atacan y tienes que eliminarlos. Si todas las plantas se mueren, perdés.

## Cómo se instala

Primero necesitas tener Python instalado (yo usé Python 3.9 pero creo que funciona con cualquier versión 3.x)

```bash
pip install pygame
```

Después solo ejecutás:

```bash
python main.py
```

## Cómo se juega

**Controles:**
- Flechas del teclado para moverte
- R para regar (tenés que estar cerca de la planta)
- P para usar el pesticida (mata los bichos rojos cerca tuyo)
- W para recargar el agua en el pozo (círculo azul arriba a la izquierda)

**Lo importante:**
- Las plantas necesitan agua todo el tiempo, si se quedan sin agua baja su felicidad
- Cuando están contentas crecen y les sale una flor
- Los bichos rojos son plagas que las atacan, usá el pesticida para matarlos (solo tenés 3 usos)
- Ganás puntos por cada planta con flor y por matar plagas
- El juego termina cuando todas las plantas se mueren

## Estructura del código

El proyecto está dividido en varios archivos :

- **main.py** - Ejecutar el Archivo principal
- **constantes.py** - Todos los valores que uso (colores, tamaños, etc)
- **planta.py** - La clase Planta con toda su lógica
- **plaga.py** - La clase de los enemigos
- **jugador.py** - La clase del jugador (la regadera)
- **ui.py** - Todo lo visual (menús, pantallas, etc)
- **utils.py** - Funciones que uso en varios lados
- **juego.py** - Acá está el loop principal del juego

## Si algo no funciona

**Error de "No module named pygame":**
Te falta instalar pygame, ejecutá: `pip install pygame`

**El juego va lento:**
Cerrá otros programas, el juego está configurado para correr a 60 FPS

**Las plantas se mueren muy rápido:**
Es parte del juego, hay que estar atento regándolas y matando plagas. Al principio cuesta pero después le agarrás la mano.

## Detalle

El juego corre a 60 FPS. Las plantas consumen agua cada 60 frames (1 segundo). Las plagas aparecen cada 180 frames (3 segundos). 

Usé clases porque me parecía más ordenado que tener un montón de listas y diccionarios sueltos. Cada clase se encarga de lo suyo: la Planta maneja todo lo de crecer y morir, la Plaga se mueve sola, el Jugador tiene los controles, etc.

Separé todo en archivos para que así sea más fácil de modificar si después se requiere  agregar algo.

