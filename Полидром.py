a = 100000

for i in range(a):
    c = str(i)

    b = True
    for i in range(len(c) // 2):
        b = (c[i] == c[len(c) - 1 - i] and b)
        if(b == False):
            break
    if(b == True):
        print(c)
