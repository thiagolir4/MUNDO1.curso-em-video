f = str(input('Degite aqui uma frase: ')).upper().strip()
a = f.count('A')
p = f.find('A')+1
print('Sua frase utilizou a letra A {} vezes'.format(a))
print('A primeira vez que ela apareceu foi na {} posição'.format(p))
print('A ultima vez que ela apareceu foi na {} posição'.format(f.rfind('A')+1))
