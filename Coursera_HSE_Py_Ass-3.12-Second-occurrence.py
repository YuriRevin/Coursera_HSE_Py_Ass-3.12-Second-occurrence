w = input()
i1 = w.find('f')
if i1 != -1:
    i2 = w.find('f', i1 + 1)
    if i2 != i1:
        print(i2)
    else:
        print('-1')
else:
    print('-2')
