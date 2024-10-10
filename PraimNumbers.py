boluvchi = 0
i = 2
j = 2
while i < 20:
    j = 2
    boluvchi = 0

    while j < i:
        if i % j == 0: boluvchi += 1
        j += 1

    if boluvchi == 0: print(i)

    i += 1
