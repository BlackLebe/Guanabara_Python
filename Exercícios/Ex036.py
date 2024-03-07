casa: float = float(input('Insira o valor da Casa que você irá comprar: '))
salario: float = float(input('Insira também o seu salário '))
parcela: float = float(input('Insira também em quantos anos você planeja parcelar o valor. '))
valormensal: float = (casa/parcela)/12

if valormensal <= ((30/100)*salario):
    print(f'\033[32mCRÉDITO APROVADO\nDado o valor da casa ser {casa:.2f} e o seu salário, parcelando em {parcela:.0f} anos, o valor mensal de cada parcela será R${valormensal:.2f}')
elif valormensal > ((30/100)*salario):
    print('\033[31mCRÉDITO NEGADO\n')
else:
    print('Falta informações para o cálculo')

