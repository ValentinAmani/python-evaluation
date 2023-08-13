"""
Afficher les nombres d'une liste qui sont divisibles par 5.
"""

def divisibleBy5(list):
    listLength = len(list)
    newList = []

    for i in range(listLength):
        number = list[i]

        if number % 5 == 0:
            newList.append(number)

    return newList

numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = divisibleBy5(numberList)
print(result)
