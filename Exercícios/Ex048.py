s = 0
for c in range(1, 500, 2):
    print(c)
    if c % 3 == 0:
        n = c
        s += n
print(s)
