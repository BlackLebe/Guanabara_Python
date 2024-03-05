from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
sealistou = input('Você já se alistou??\n1 - sim\n2 - não\n')
anosistema = date.today().year
idade = anosistema - ano

if sealistou == '2':
    if idade < 18:
        print('Ainda falta algum tempo para você se alistar no exército precisamente faltam {} ano(s)'.format(18 - idade))
    elif idade == 18:
        print('JÁ ESTÁ NA HORA DE SE ALISTAR SEU VAGABUNDO!!')
    elif idade > 18:
        print('MEU DEUS JÁ PASSOU {} ANO(S) DESDE A ÉPOCA DE VOCÊ SE ALISTAR'.format(idade - 18))
else:
    print('Ok tenha um bom dia')
