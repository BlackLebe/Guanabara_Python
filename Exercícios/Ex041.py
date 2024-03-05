from datetime import date

nascimento = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('Você é da categoria mirim')
elif 9 > idade <= 14:
    print('Você é da categoria Infantil')
elif 14 > idade <= 19:
    print('Você é Junior')
elif 19 > idade == 20:
    print('Você é Sênior')
elif idade > 20:
    print('você é master')
