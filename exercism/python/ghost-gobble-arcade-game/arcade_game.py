#Reglas del Juego Pacman

def eat_ghost(power_pellet_active, touching_ghost):
    #Pacman puede comer fantasmas si el poder de la pelota esta activo y toca a un fantasma
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    #Pacman obtiene puntos  comiendo pelotas de poder o come un punto
    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    #Pacman pierde si toca a un fantasma y la pastilla no está activa
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    #Pacman gana si comio todos los puntos del juego y no a perdido(funcion lose)
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
    # , , , V
