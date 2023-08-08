import pyxel
import classes

class App:
    def __init__(self):
         pyxel.init(256, 240, title="01 - Mario")
         self.joueur = classes.Player(100, 100)
         self.blocs = [classes.Bloc(16 * i, 128, 16, 0) for i in range(16)]
         pyxel.run(self.update, self.draw)
         
    def update(self):
        self.joueur.mouvement()
        
        for bloc in self.blocs:
            bloc.collision_sup(self.joueur)
    
    def draw(self):
        pyxel.load("my_resource.pyxres", True, True, True, True)
        
        pyxel.cls(0)
        
        pyxel.blt(self.joueur.x, self.joueur.y,
                  0, self.joueur.u, self.joueur.v,
                  self.joueur.longueur, self.joueur.taille, 0)
        
        for bloc in self.blocs:
            pyxel.blt(bloc.x, bloc.y, 0, bloc.u, bloc.v, 16, 16, 0)
        
App()
