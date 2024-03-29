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

def mouvement_general(blocs, recul, joueur):
    for bloc in blocs:
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            joueur.u, joueur.v = 32, 0
            joueur.inverse = False
            bloc.x -= 1
            
        elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            joueur.u, joueur.v = 32, 0
            joueur.inverse = True
            bloc.x += 1
        bloc.x += recul
      
class App:
    def __init__(self):
         pyxel.init(256, 240, title="06 - Tous les blocs", fps=60)
         self.joueur = classes.Player(100, 190)
         self.blocs = cartes.carte1_1_blocs()
         self.entites = cartes.carte1_1_entites()
         self.recul = 0
         pyxel.run(self.update, self.draw)
         
    def update(self):    
        self.joueur.mouvement_vertical()
        
        mouvement_general(self.blocs, self.recul, self.joueur)
        self.recul = collision_generale(self.blocs, self.joueur)
    
    def draw(self):
        pyxel.load("my_resource.pyxres", True, True, True, True)
        
        pyxel.bltm(0, 0, 0, 0, 0, 256, 240)
        
        if self.joueur.inverse: #Dessin inverse
            pyxel.blt(self.joueur.x, self.joueur.y,
                  0, self.joueur.u, self.joueur.v,
                  -self.joueur.longueur, self.joueur.taille, 0)
        else:
            pyxel.blt(self.joueur.x, self.joueur.y,
                      0, self.joueur.u, self.joueur.v,
                      self.joueur.longueur, self.joueur.taille, 0)
        
        for bloc in self.blocs:
            if - 100 <= bloc.x <= 348:
                pyxel.blt(bloc.x, bloc.y, 0, bloc.u, bloc.v, 16, 16, 8)
        
App()
