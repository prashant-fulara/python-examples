"""Module - Convert 'Don't Panic' to 'on tap' using slice"""

PHRASE = "Don't Panic"

SUB_PHRASE_1 = PHRASE[1:3]
print(SUB_PHRASE_1)

SUB_PHRASE_2 = PHRASE[5:6]
print(SUB_PHRASE_2)

SUB_PHRASE_3 = PHRASE[4:5]
SUB_PHRASE_4 = PHRASE[7:5:-1]

print(SUB_PHRASE_1 + SUB_PHRASE_2 + SUB_PHRASE_3 + SUB_PHRASE_4)
