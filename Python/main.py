# Module zum ansteuern des TFT Displays
from ili934xnew import ILI9341, color565
import glcdfont
import tt14
import tt24
import tt32

# Module zum ansteuern der Pin am RP2040
from machine import Pin, SPI
# Modul zum einlegen einer kleinen Pause
import time
# Modul zum entnehmen eines zufälligen Eintrages
# aus einer Liste
import random

# unsere Klassen aus dem Spiel "Whack a mole"
from whackamole import Game, Square

# Aufbau der SPI Verbindung
spi = SPI( 0, baudrate=15625000, miso=Pin(4), mosi=Pin(7), sck=Pin(6))

# Initialisieren des Display Objektes
display = ILI9341( spi, cs=Pin(13), dc=Pin(15), rst=Pin(14), w=160, h=128, r=4)

display.erase()
time.sleep(3)

# Variablen für
# - das zuletzt angezeigte Quadrat
# - der letzte betätigte Taster
last_square = None
last_button = None

lives = 4

game = Game(display, lives)
game.draw_frame()
game.update_points()
game.show_time()

# definieren der Quadrate für die Tasten
square_red = Square(8,125,25,color565(0,0, 255), display, 1)
square_green = Square(38,125,25,color565(0,255, 0), display, 2)
square_blue = Square(68,125,25,color565(255,0, 0), display, 3)
square_yellow = Square(98,125,25,color565(55,253, 255), display, 4)
squares = [square_red, square_green, square_blue, square_yellow]

# liefert ein Quadrat welches ungleich dem
# zuvor angezeigten ist
def find_square(square):
    # entnehmen eines zufälligen Eintrages
    # aus der Liste mit den Quadraten
    inner_square = random.choice(squares)
    # Wenn ein Quadrat gefunden wurde und dieses gleich dem zurvor
    # angezeigen ist, dann soll die Funktion erneut aufgerufen werden
    if square is not None and inner_square == square:
        return find_square(inner_square)
    else:
        # Wenn ein neues Quadrat gefunden wurde welche nicht zuvor
        # Angezeigt wurde, dann wird dieses zurück geliefert.
        return inner_square


# Taster definieren
button_red = Pin(16, Pin.IN, Pin.PULL_DOWN)
button_green = Pin(17, Pin.IN, Pin.PULL_DOWN)
button_blue = Pin(18, Pin.IN, Pin.PULL_DOWN)
button_yellow = Pin(19, Pin.IN, Pin.PULL_DOWN)

# Funktion welche aufgerufen wird wenn ein Taster betätigt wird.
# Parameter ist der Pin an welchem dieser Taster konfiguriert wurde.
def button_handler(pin):
    # zugriff auf die globalen Variablen außerhalb der Funktion
    global last_square, game, last_button
    
    # Wenn der Pin gleich button_red ist
    # und nicht der letzte Taster der selbe Taster ist, dann ...
    if pin is button_red and last_button is not pin:
        # setzen zuletzt betätigten Taster auf den aktuellen Pin
        last_button = pin
        # Wenn das angezeigte Quadrat den Index 1 hat,
        # also das erste ist, dann ...
        if last_square.index == 1:
            # aktualisieren der Punkte
            game.update_points()
        else:
            # wenn nicht dann ein leben abziehen
            game.update_live()
    elif pin is button_green and last_button is not pin:
        last_button = pin
        if last_square.index == 2:
            game.update_points()
        else:
            game.update_live()
    elif pin is button_blue and last_button is not pin:
        last_button = pin
        if last_square.index == 3:
            game.update_points()
        else:
            game.update_live()
    elif pin is button_yellow and last_button is not pin:
        last_button = pin
        if last_square.index == 4:
            game.update_points()
        else:
            game.update_live()
        
# erzeugen der Interrupts für die Taster
# Wenn der Pin auf HIGH gezogen wird dann
# soll die Funktion button_handler ausgeführt werden
button_red.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_green.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_blue.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_yellow.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

PAUSE = 1000
last_action = time.ticks_ms()
while game.is_running():
    if last_action < (time.ticks_ms()-PAUSE):
        last_action = time.ticks_ms()
        game.increment_time()
        game.show_time()
        
        if last_square:            
            game.remove_square(last_square)
    
        square = find_square(last_square)
        
        game.draw_square(square)
        
        last_square = square

