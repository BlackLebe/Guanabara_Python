preco = float(input('Digite o preço do produto: '))
desconto = (5/100)*preco
novopreco = preco - desconto

print('Com o desconto aplicado o produto passará a valer {:.2f}'.format(novopreco))