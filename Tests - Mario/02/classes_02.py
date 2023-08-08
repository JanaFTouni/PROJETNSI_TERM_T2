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
        
    def mouvement(self):
        self.y += 0
        
        if pyxel.btn(pyxel.KEY_SPACE):
            self.y -= 2
            
        elif pyxel.btn(pyxel.KEY_A):
            self.x -= 1
            
        elif pyxel.btn(pyxel.KEY_D):
            self.x += 1
            
        elif pyxel.btn(pyxel.KEY_W):
            self.y -= 1
            
        elif pyxel.btn(pyxel.KEY_S):
            self.y += 1
        
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
            
            print(other.x, other.longueur, self.x)
            
            if other.y + 15 == self.y:
                other.y -= (other.y % 16)
                
            elif (self.y + 15) <= other.y <= (self.y + 16):
                other.y = self.y + 16
                
            elif other.x - other.longueur == self.x + 1:
                other.x = self.x - other.longueur
            
            elif other.x == self.x + 16:
                other.x = self.x + 16
            
