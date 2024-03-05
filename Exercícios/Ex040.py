nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2)/2
if media < 5:
    print('REPROVADO')
elif 6.9 >= media <= 5:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')