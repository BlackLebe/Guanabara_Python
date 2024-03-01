nome = str(input('Qual o seu nome?? ')).capitalize()
if nome == 'Calebe':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('a sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!!')
else:
    print('sua média não foi muito boa... Estude mais!!')
