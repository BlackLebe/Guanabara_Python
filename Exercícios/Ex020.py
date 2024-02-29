from random import shuffle

n1 = input('Digite o nome do primeiro aluno \n ')
n2 = input('digite o nome do segundo aluno \n ')
n3 = input('digite o nome do terceiro aluno \n ')
n4 = input('digite o nome do quarto aluno \n ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:\n {}'.format(lista))

