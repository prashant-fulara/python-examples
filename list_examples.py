"""Module providing examples of List"""

SENTENCE = "Earth supports Life"

sentenceList = list(SENTENCE)

print(sentenceList)
print(sentenceList[0:3])
print("".join(sentenceList[0:3]))
print(sentenceList[-4:])

sentenceListInReverse = sentenceList[::-1]
print("".join(sentenceListInReverse))

every_other = sentenceList[::2]
print(every_other)
