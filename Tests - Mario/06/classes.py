import pyxel

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        self.longueur = 16
        self.taille = 16
        
        self.centre = (self.longueur // 2, self.taille // 2)
        
        self.u = 0
        self.v = 0
        self.inverse = False #dessin inverse
        
        self.saut = False
        self.t = 0 # Temps du saut
        
    def mouvement_vertical(self):
        self.y += 2
        
        if self.t > 0:
            self.t -= 1
            self.y -= 4
            if self.t <= 16:
                self.y += 2
        
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and self.saut:
            self.u, self.v = 0, 16
            self.saut = False
            self.t = 48
        
        #Le joueur n'a pas de point d'appuis pour sauter
        self.saut = False
            
class Bloc:
    def __init__(self, x: int, y: int, u: int, v: int):
        self.x = x
        self.y = y
        
        self.u = u
        self.v = v
        
    def collision(self, other):
        recul = 0

        if ( self.x < other.x + other.longueur ) and\
           ( self.y < other.y + other.taille ) and\
           ( self.x + 16 > other.x) and\
           ( self.y + 16 > other.y):
            
            if other.y + 15 <= self.y + 1: #Collision supérieure
                other.y -= 2
                if other.t < 1:
                    other.saut = True
                    if not (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)):
                        other.u, other.v = 0,0
                
            elif (self.y + 13) <= other.y <= (self.y + 16): #Collision inférieure
                other.y = self.y + 16
                other.t = 0
            
            elif other.x <= self.x: #Collision gauche
                recul = 1
                
            elif other.x <= (self.x + 16): #Collision droite
                recul = -1
            
        return recul
    
class Entite:
    pass
    
