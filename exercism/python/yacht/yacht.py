# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = [1,2,3,4,5]
BIG_STRAIGHT = [2,3,4,5,6]
CHOICE = []


def score(dice, category):
    diceorden = sorted(dice)  #lista ordenada
    dicemin = min(dice, key=dice.count) #minimo elemento
    dicemax= max(dice, key=dice.count) #maximo elemento
    
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return dice.count(category) * category
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        #si el tamaño de la lista tiene un unico elemento
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    elif category == FOUR_OF_A_KIND :
        for i in dice:
            if dice.count(i) >= 4:
                return i * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        if diceorden == LITTLE_STRAIGHT:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if diceorden == BIG_STRAIGHT:
            return 30
        else:
            return 0
    elif category == FULL_HOUSE:
        #numero de veces que min aparece en la lista dice
        if dice.count(dicemin) == 2 and dice.count(dicemax) == 3:
            return sum(dice)
        else:
            return 0
    else:
        return 0
