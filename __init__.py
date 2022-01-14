from PyDictionary import PyDictionary

words = str(input("Enter the Word: "))
dictionary=PyDictionary(words)

print(dictionary.getMeanings())
