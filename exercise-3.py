"""
Lire un fichier texte dans une variable et remplacer toutes les nouvelles lignes 
par des espaces.
En supposant que vous ayez un fichier avec le contenu suivant:
line1
line2
line3
line4
line5
Le résultat attendu doit être line1 line2 line3 line4 line5 .
"""

def replaceBackLinesBySpaces(filePath):
    with open(filePath, "r") as file:
        content = file.read().replace("\n", " ")

    return content

fileToModifyPath = "file.txt"

result = replaceBackLinesBySpaces(fileToModifyPath)
print(result)
