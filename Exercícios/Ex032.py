from datetime import date

ano = int(input('Diga-me um ano e lhe direi se és bissexto(se quiser o ano atual só colocar 0):  '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ANO É BISSEXTO!!')
else:
    print('Ano não é bissexto...')