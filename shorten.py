def shorten(words):
    tab = words.split()
    string = ''
    for word in tab:
        string += word[0].capitalize()
    return string
        


print(shorten('Dont repeat yourself!'))
