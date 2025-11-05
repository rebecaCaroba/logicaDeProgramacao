num = int(input('Digite um número: '))

for i in range(0, num - 1, 1):
    if i == 0:
        a=0
        b=0

    if i == 1:
        a = 0
        b = 1

    # a = 0, 0, 1, 1, 2, 3
    # b = 0, 1, 1, 2, 3, 5
    # c = 0, 1, 2, 3, 5, 8

    c = a + b
    a = b
    b = c

    print(c, " ")