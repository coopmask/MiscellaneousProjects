# Ask the user for noun, verbs, plural noun and
# print out a story with their libs.

singular_noun = input('What would you like to name a character? ').title()

plural_noun = input('What would you like to name a group of characters? ').lower()

verb1 = input('What action should a character take that is in the past tense? ').lower()

verb2 = input('What is an action that a character should take in the present tense? ').lower()

verb3 = input('What is an action that a character should take in the past tense? ').lower()

print()

print(f'{singular_noun} took a stroll to the park the other day and noticed that an old man {verb1} next to the bench. \
He appeared to be friendly, so {singular_noun} approached him and asked him if he wanted to {verb2}. As {singular_noun} \
finished the question, a group of {plural_noun} interrupted their conversation. The old man surprisingly {verb3}, \
and {singular_noun} laughed.')