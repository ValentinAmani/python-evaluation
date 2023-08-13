"""
Renverser l'ordre des éléments d'une liste.
Créer un programme qui change l'ordre des éléments d'une liste en les 
renversant.
[1, 2, 3, 4] devient [4, 3, 2, 1].
"""

def listReverse(list):
    listLength = len(list)
    newList = []

    for i in range(1, listLength + 1):
        decrement = listLength - i
        newList.append(list[decrement])
    
    return newList

listToReverse = [1, 2, 3, 4]

result = listReverse(listToReverse)
print(result)
