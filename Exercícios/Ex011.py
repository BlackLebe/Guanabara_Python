altura = float(input('Digite a altura da parede: '))
comprimento = float(input('Digite o Comprimento da Parede: '))
area = altura * comprimento
litrosprecisa = area/2

print('Com as medidas informadas, e sabendo que 1 litro de tinta pinta 2m² de parede, será necessário {:.3f} litros de tinta para pintar a parede'.format(litrosprecisa))
