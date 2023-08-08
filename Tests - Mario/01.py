import pyxel
import classes

class App:
    def __init__(self):
         pyxel.init(256, 240, title="01 - Mario")
         self.joueur = classes.Player(0, 0)
         pyxel.run(self.update, self.draw)
         
    def update(self):
        self.joueur.x = 100
        self.joueur.y = 100
    
    def draw(self):
        pyxel.load("my_resource.pyxres", True, True, True, True)
        
        pyxel.cls(0)
        
        pyxel.blt(self.joueur.x, self.joueur.y,
                  0, self.joueur.u, self.joueur.v,
                  self.joueur.longueur, self.joueur.taille, 0)
        
App()
