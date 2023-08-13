"""
Modifier l'élément d'une liste imbriquée dans la liste suivante.
Changer les occurrences de 58 en 5800.
La liste est la suivante -> list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
Le résultat attendu est le suivant: [5, [10, 15, [20, 25, [30, 5800], 40], 45], 50]
"""

def modifyItemsInList(itemsList, element, replace):
    for i, item in enumerate(itemsList):
        if isinstance(item, list):
            modifyItemsInList(item, element, replace)
        elif item == element:
            itemsList[i] = replace

    return itemsList

listToModify = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
itemToModify = 58
modification = 5800

result = modifyItemsInList(listToModify, itemToModify, modification)
print(result)
