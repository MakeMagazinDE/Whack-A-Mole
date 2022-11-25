# importieren der benötigen Module
from ili934xnew import color565

class Square:
    
    # Konstruktor
    # x - die X Position auf dem Display
    # y - die Y Position auf dem Display
    # width - die Breite für das Quadrat
    # color - ein ili934xnew.color565 Wert
    # display - eine Instanz des erzeugten ili934xnew Objektes
    # index - der Index des Quadrates
    def __init__(self, x, y, width, color, display, index):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.display = display
        self.index = index