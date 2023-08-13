import pyxel
import classes

def collision_generale(blocs, entites):
    "Collision entre les entites ou le joueur et les blocs"
    recul = 0
    for bloc in blocs:
        for entite in entites:
            if type(entite) == classes.Player:
                temp = bloc.collision(entite)
                if temp == -9:
                    blocs.remove(bloc)
                    continue
                elif abs(temp) > 0:
                    recul = temp
            else:
                bloc.collision(entite)
            
    return recul

def mouvement_general(monde, recul, joueur):
    "On mouvemente le monde autour du joueur, blocs et entites"
    for chose in monde:
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            if joueur.mini:
                joueur.u, joueur.v = 32, 0
            else:
                joueur.u, joueur.v = 46, 32
            joueur.inverse = False
            chose.x -= 1
            
        elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            if joueur.mini:
                joueur.u, joueur.v = 32, 0
            else:
                joueur.u, joueur.v = 46, 32
            joueur.inverse = True
            chose.x += 1
        chose.x += recul
        
def mouvement_entites(entites):
    "Le mouvement independant des entites"
    for entite in entites:
        if -116 <= entite.x <= 248:
            entite.mouvement()
            
def collision_entites(entites):
    "Si les entites se touchent"
    for entite_1 in entites:
        if not entite_1.vivant and entite_1.t <= 0:
            entites.remove(entite_1)
        elif -16 <= entite_1.x <= 264:
            for entite_2 in entites:
                if (-16 <= entite_2.x <= 264) and (entite_1 != entite_2) and entite_2.vivant:
                    if ( entite_1.x < entite_2.x + entite_2.longueur ) and\
                       ( entite_1.y < entite_2.y + entite_2.taille ) and\
                       ( entite_1.x + entite_1.longueur > entite_2.x) and\
                       ( entite_1.y + entite_1.taille > entite_2.y):
                        entite_1.direction *= -1

