import pyxel

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        self.longueur = 13
        self.taille = 16
        
        self.centre = (self.longueur // 2, self.taille // 2)
        
        self.u = 0
        self.v = 0
        
        self.chute = False
        self.t = 0 # Temps du saut en mont
        
    def mouvement(self):
        self.y += 1
        
        if self.t > 0:
            self.t -= 1
            self.y -= 2
        
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.chute:
            self.chute = True
            self.t = 64
            
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
            
            if other.y + 15 == self.y:
                other.y -= (other.y % 16)
                if other.t < 30:
                    other.chute = False
                
            elif (self.y + 15) <= other.y <= (self.y + 16):
                other.y = self.y + 16
                other.t = 0
            
            elif other.x <= self.x:
                recul = 1
                
            elif other.x <= (self.x + 16):
                recul = -1
            
        return recul
