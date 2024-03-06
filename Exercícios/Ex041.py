from datetime import date

nascimento = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('Você é da categoria mirim')
elif idade <= 14:
    print('Você é da categoria Infantil')
elif idade <= 19:
    print('Você é Junior')
elif idade == 20:
    print('Você é Sênior')
elif idade > 20:
    print('você é master')
