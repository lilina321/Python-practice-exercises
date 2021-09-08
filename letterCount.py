word = 'abzkfhiohfnlaanfnffnkkdamd'

tab = []
for letter in sorted(word):
    if letter not in tab:
        tab.append(letter)
        print(letter, ':', word.count(letter))
