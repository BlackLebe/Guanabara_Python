from datetime import date
countmaio = 0
countmeno = 0
hoje = date.today().year
for c in range(1, 8):
    ano = int(input(f'Insira o ano que a {c}ª pessoa nasceu: '))
    if ano > hoje:
        idade = ano - hoje
    elif ano < hoje:
        idade = hoje - ano

    if idade >= 21:
        countmaio += 1
    elif idade < 21:
        countmeno += 1
print(f'Ao todo tivemos {countmaio} maiores de idade')
print(f'E também tivemos {countmeno} menores de idade')

