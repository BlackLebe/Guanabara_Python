frase = str(input('Digite um nome ou uma frase: ')).strip().upper().split()
juntar = ''.join(frase)
inv = ''
for letra in range(len(juntar) - 1, -1, -1):
    inv += juntar[letra]
print(f'A Palavra digitada {juntar} invertida fica {inv}')
if juntar == inv:
    print('Portanto se trata de um palíndromo')
else:
    print('Não se trata de um palíndromo')
