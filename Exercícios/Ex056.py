soma = 0
homemaior = 0
nomemaior = ''
countf = 0
for c in range (1, 5):
    print(f'----- {c}ª Pessoa ----')
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    soma += idade
    if sexo == 'M':
        if c == 1:
            homemaior = idade
            nomemaior = nome
        else:
            if idade > homemaior:
                homemaior = idade
                nomemaior = nome
    else:
        if idade < 20:
            countf += 1
media = float(soma / c)
print(f'A média de idade do grupo é de {media} anos')
print(f'O Homem mais velho possui {homemaior} anos e se chama {nomemaior}')
print(f'Ao todo existem {countf} com menos de 20 anos')
