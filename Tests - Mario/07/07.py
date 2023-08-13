import pyxel
import classes
import cartes
import fonctions
        
class App:
    def __init__(self):
         pyxel.init(256, 240, title="07 - Ennemis", fps=60)
         self.joueur = classes.Player(100, 190)
         self.blocs = cartes.carte1_1_blocs()
         self.entites = cartes.carte1_1_entites()
         self.recul = 0
         pyxel.run(self.update, self.draw)
         
    def update(self):    
        self.joueur.mouvement_vertical()
        
        fonctions.mouvement_general(self.blocs + self.entites, self.recul, self.joueur)
        fonctions.collision_entites(self.entites)
        fonctions.mouvement_entites(self.entites)
        self.joueur.collision_ennemi(self.entites)
        self.recul = fonctions.collision_generale(self.blocs, [self.joueur] + self.entites)
        
        if self.joueur.mort:
            self.new_game()
        
    
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
            if -16 <= bloc.x <= 264: #On ne fait qu'apparaitre les blocs visibles
                pyxel.blt(bloc.x, bloc.y, 0, bloc.u, bloc.v, 16, 16, 8)
                
        for entite in self.entites: #Meme chose pour les entites
            if -16 <= entite.x <= 264:
                pyxel.blt(entite.x, entite.y, 0, entite.u, entite.v, entite.longueur, entite.taille, 5)
                
    def new_game(self):
        self.joueur = classes.Player(100, 190)
        self.blocs = cartes.carte1_1_blocs()
        self.entites = cartes.carte1_1_entites()
        
App()
