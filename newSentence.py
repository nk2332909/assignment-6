sentence = input("Enter a english sentence: ")

words = sentence.split()
words.sort()

newSentence = ""
for x in words:
    newSentence += x + " "
    
print(newSentence)
