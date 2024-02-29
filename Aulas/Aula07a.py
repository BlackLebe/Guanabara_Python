nome = input('Qual o seu nome ? ')
print('Prazer em te conhecer {:=^20}.'.format(nome))

n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma dos dois é {}\no produto é {}\na divisão é {:.3f}\na divisão inteira é {}\ne a potenciação é {}.'.format(s, m, d, di, e))

