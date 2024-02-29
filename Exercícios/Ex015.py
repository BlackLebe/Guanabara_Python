dias = float(input('Quantos dias você passou com o carro? '))
pgtodias = dias*60
km = float(input('Quanto foi a distância percorrida? '))
pgtokm = km*0.15
pgtototal = pgtodias + pgtokm

print('você passou {} dias no com carro percorrendo {}km com ele, sendo assim o total a pagar foi R${}'.format(dias, km, pgtototal))