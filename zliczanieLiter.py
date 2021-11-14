from collections import Counter


sentence = 'Ala ma kota'
words = len(sentence.split())
dict = {}

letters = len(sentence.replace(" ", ""))
for letter in sentence:
    if letter not in dict.keys():
        dict[letter] = 1
    else:
        dict[letter] += 1

tab = []
dict2 = {}
for i in sentence:
    if i not in tab:
        tab.append(i)
        dict2[i] = sentence.count(i)
print(dict2)
        
print(Counter(sentence))
print('Words:', words, 'Letters:', letters, 'Letter frequency:', dict)

