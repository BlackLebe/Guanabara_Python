n1 = int(input('Digite o primeiro número para eu ordenar: '))
n2 = int(input('Digite o segundo número para eu ordenar: '))
n3 = int(input('Digite o terceiro número para eu ordenar: '))
menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('Dos número digitados, o maior é {} e o menor é {}'.format(maior,menor))
