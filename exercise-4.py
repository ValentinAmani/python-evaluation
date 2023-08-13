"""
Afficher un mot en alternant entre majuscule et minuscule.
"""

def uppercaseLowercase(word):
    word = word.lower()
    wordLength = len(word)
    newWord = ""

    for i in range(wordLength):
        if i % 2 == 0:
            newWord += word[i].upper()
        else:
            newWord += word[i]

    return newWord

wordToUppercaseLowercase = "abcdefghijklmnopqrstuvwyz"

result = uppercaseLowercase(wordToUppercaseLowercase)
print(result)
