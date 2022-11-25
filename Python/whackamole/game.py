from ili934xnew import color565
import tt14


class Game:
    
    # Konstruktor
    def __init__(self,display, lives):
        self.display = display
        self.points = 0
        self.time = 0
        self.lives = lives
        self.death = False
        
        
    # zeichnet einen Rahmen mit Text
    # auf dem Display
    def draw_frame(self):
        # Display leeren
        self.display.erase()
        # Rahmen zeichnen
        self.display.draw_rectangle(3,3,124,155,color565(255, 255, 255))
        self.display.draw_line(3,25,128,25,color565(255, 255, 255))
        # Text ausgeben
        self.display.set_pos(28,10)
        self.display.print("Whack a mole")

        self.display.set_pos(10,40)
        self.display.print("Punkte")

        self.display.set_pos(91,40)
        self.display.print("Leben")

        self.display.set_pos(10,80)
        self.display.print("Zeit")
        
        # Wenn der Rahmen gezeichnet wurde initial die Leben anzeigen
        self.update_live()
        
    # Incrementiert die Punkte und aktualisiert den Text auf dem Display
    def update_points(self):
        # löschen der letzten Anzeige der Punkte
        # hier wird einfach ein schwarzes Rechteck an die entsprechende
        # Stelle auf dem Display gezeichnet
        self.display.fill_rectangle(10, 54, 45, 20, color565(0,0, 0))
        
        # setzen der Schriftgroeße 14
        self.display.set_font(tt14)
        # Schriftfarbe auf weiss und Hintergrundfarbe auf schwarz
        self.display.set_color(color565(255, 255, 255), color565(0, 0, 0))
        # positionieren des Cursors zum schreiben von Text
        self.display.set_pos(20,57)
        # incrementieren der Punkte
        self.points +=1
        # schreiben des Textes, dabei wird zunaechst der Zahlenwert
        # in ein String umgewandelt
        self.display.print(str(self.points))


    # Aktualisieren der Leben, wenn diese Funktion aufgerufen wird,
    # dann wird ein Leben abgezogen.
    # Wenn der Wert der Variable self.lives gleich 0 ist, dann ist das
    # Spiel beendet.
    def update_live(self):
        self.display.fill_rectangle(91, 54, 35, 20, color565(0,0, 0))
        
        self.display.set_font(tt14)
        self.display.set_color(color565(255, 255, 255), color565(0, 0, 0))
        self.display.set_pos(101,57)
        self.lives -= 1
        self.display.print(str(self.lives))
        print(self.lives)
        # Wenn der Wert der Variable self.lives gleich 0 ist, dann...
        if self.lives == 0:
            # Wert der Variable self.death auf True setzen
            self.death = True
        else:
            # andernfalls auf False
            self.death = False
    
    # incrementiert die Zeit um 1
    # in unserem Fall wird jede Sekunde ein neues Rechteck
    # angezeigt
    def increment_time(self):
        self.time +=1
    
    # löscht den alten Wert und zeigt die neu verstrichene
    # Zeit auf dem TFT-Display an
    def show_time(self):
        self.display.fill_rectangle(10, 99, 115, 20, color565(0,0, 0))
        
        self.display.set_pos(30,99)        
        self.display.print(str(self.time)+" Sek.")
    
    # solange der Wert der Variable self.death nicht True ist gilt das
    # Spiel als nicht beendet
    def is_running(self):
        return not self.death
    
    # entfernt das Quadrat vom Display
    def remove_square(self, square):
        self.display.fill_rectangle(square.x, square.y, square.width, square.width, color565(0,0,0))
    
    # zeichnet das Quadrat auf dem Display
    def draw_square(self, square):
        self.display.fill_rectangle(square.x, square.y, square.width, square.width, square.color)

