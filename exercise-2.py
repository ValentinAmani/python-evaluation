"""
Calculer la factorielle d'un nombre.
Coder un programme qui donne la factorielle d'un nombre.
Pour rappel, la factorielle est le résultat de la multiplication de tous les 
nombres inférieurs ou égaux à un nombre donné.
Par exemple pour 6 on a 1, 2, 3, 4, 5 et 6. Donc pour faire la factorielle de 
6 (!6) on multiple 1 x 2 x 3 x 4 x 5 x 6 = 720.
"""

def calculateFactorial(number):
    factorial = 1

    while number > 1:
        factorial *= number
        number -= 1

    return factorial

numberToCalculateFactorial = 6

result = calculateFactorial(numberToCalculateFactorial)
print(result)
