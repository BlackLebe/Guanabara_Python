n = int(input('Digite um número: '))
div = 0
count = 0
for c in range(1, n + 1):
    if n % c ==0:
        print('\033[32m', end=' ')
        count += 1

    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {count} vezes')
if count == 2:
    print(f'\033[32m O que prova que {n} é primo')
else:
    print(f'\033[31m O que prova que o número {n} não é primo')

