# Задание 2:
# Определите, сколько раз встречается каждое из слов в неком тексте.

Text = '''Один два три 4 три три
4 4 два 4 успокоение аллегория
тропики Питон Питон Питон'''
print(Text, '\n')
D = {}

Array_of_words = Text.split()
for word in Array_of_words:
    if word not in D:
        D[word] = 1
    else:
        D[word] += 1

Words = D.keys()
for word in Words:
    print('Слово', word, 'встречается', D[word], 'раз')
