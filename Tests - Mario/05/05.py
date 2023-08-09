import pyxel
import classes
import cartes

def collision_generale(blocs, joueur):
    recul = 0
    for bloc in blocs:
        temp = bloc.collision(joueur)
        if abs(temp) > 0:
            recul = temp
            
    return recul

def mouvement_general(blocs, recul):
    for bloc in blocs:
        if pyxel.btn(pyxel.KEY_D):
            bloc.x -= 1
            
        elif pyxel.btn(pyxel.KEY_A):
            bloc.x += 1
        bloc.x += recul
      
class App:
    def __init__(self):
         pyxel.init(256, 240, title="04 - Mouvement :)")
         self.joueur = classes.Player(100, 100)
         self.blocs = cartes.carte1_1()
         self.recul = 0
         pyxel.run(self.update, self.draw)
         
    def update(self):    
        self.joueur.mouvement()
        
        print(self.recul)
        mouvement_general(self.blocs, self.recul)
        self.recul = collision_generale(self.blocs, self.joueur)
    
    def draw(self):
        pyxel.load("my_resource.pyxres", True, True, True, True)
        
        pyxel.bltm(0, 0, 0, 0, 0, 256, 240)
        
        pyxel.blt(self.joueur.x, self.joueur.y,
                  0, self.joueur.u, self.joueur.v,
                  self.joueur.longueur, self.joueur.taille, 0)
        
        for bloc in self.blocs:
            pyxel.blt(bloc.x, bloc.y, 0, bloc.u, bloc.v, 16, 16, 8)
        
App()
