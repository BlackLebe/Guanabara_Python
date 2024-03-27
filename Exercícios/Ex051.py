pt = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a sua razão: '))
t = int(input('Até qual termo você quer que seja realizada a PA: '))
enesimotermo = pt + (t - 1) * razao
for c in range(pt, enesimotermo + razao, razao):
    print(c, end=(' -> '))
print('FIM')
