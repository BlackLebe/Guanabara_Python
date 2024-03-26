m = 0
n = int(input('digite um número: '))
print('{:=^20}\n{:^20}'.format('','TABUADA'))
for c in range(0, 11):
    m = n * c
    print(f'{n} X {c} = {m:2}')
print('{:=^20}'.format(''))