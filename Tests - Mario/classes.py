import pyxel

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        self.longueur = 13
        self.taille = 16
        self.u = 0
        self.v = 0
        
    def mouvement(self):
        self.y += 1
        
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.y -= 30
            
        elif pyxel.btn(pyxel.KEY_A):
            self.x -= 3
            
        elif pyxel.btn(pyxel.KEY_D):
            self.x += 3
        
class Bloc:
    def __init__(self, x: int, y: int, u: int, v: int):
        self.x = x
        self.y = y
        
        self.u = u
        self.v = v
        
    def collision_sup(self, other):
        if ( self.x <= other.x + other.longueur ) and\
           ( self.y <= other.y + other.taille ) and\
           ( self.x + 16 >= other.x) and\
           ( self.y + 16 >= other.y):
            
            other.y -= (other.y % 16)
