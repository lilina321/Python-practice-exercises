with open('imionanazwiska.txt', encoding = 'UTF-8') as file:
    tab = []
    for line in file:
        x = tuple(line.split())
        tab.append(x)
        

with open('imiona.txt', 'w', encoding = 'UTF-8') as file2:
    for t in tab:
        file2.write(t[0])
        file2.write('\n')
        
            
with open('nazwiska.txt', 'w', encoding = 'UTF-8') as file3:
    for t in tab:
        file3.write(t[1])
        file3.write('\n')
        

    
