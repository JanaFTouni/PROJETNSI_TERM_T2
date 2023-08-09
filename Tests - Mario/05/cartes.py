import classes

def carte1_1() -> list:
    carte = []
    carte += [classes.Bloc(16*i, 208 + (16* j), 16, 0) for i in range(70) for j in range(2)]
    carte += [classes.Bloc(256, 144, 48, 16)]
    carte += [classes.Bloc(336 + 32*i, 144, 48, 16) for i in range(2)]
    carte += [classes.Bloc(320 + 32*i, 144, 32, 16) for i in range(3)]
    carte += [classes.Bloc(352, 80, 48, 16)]
    carte += [classes.Bloc(448, 176, 72, 16)]
    carte += [classes.Bloc(464, 176, 88, 16)]
    carte += [classes.Bloc(448, 192, 72, 32)]
    carte += [classes.Bloc(464, 192, 88, 32)]
    return carte
