a = [0]
b = [0]
c = [0]
i = 0
discs = [0]

ret = ""
digit = "10987654321"
while(ret == "" or not ret in digit):
    countDiscs = input("""Введите количество дисков (не больше 10), (11 дисков - уже ошибка,
не хватает глубины рекурсии): """)
    ret = countDiscs

countDiscs = int(countDiscs)

for i in range(countDiscs, 0, -1):
    a.append(i)

for i in range(countDiscs, 0, -1):
    discs.append(i)

flag = False

print(a, b, c)

if(countDiscs % 2 == 1):
    c.append(a[-1])
    a.pop(-1)

if(countDiscs % 2 == 0):
    b.append(a[-1])
    a.pop(-1)

def yyy():
    global flag, a, b, c, i

    if(countDiscs % 2 == 0):
        
        if(flag == True):
            
            if(a[-1] == 1):

                if(b[-1] % 2 == 0):
                    b.append(a[-1])
                    a.pop(-1)

            elif(b[-1] == 1):

                if(c[-1] % 2 == 0 and c[-1] != 0):
                    c.append(b[-1])
                    b.pop(-1)
                    
            elif(c[-1] == 1):

                if(a[-1] % 2 == 0 and a != 0):
                    a.append(c[-1])
                    c.pop(-1)

            i += 1
                
        print(a, b, c)

        flag = True
        
        if(a[-1] > b[-1] and a[-1] < c[-1] or c[-1] == 0):
            if(a[-1] != 1):
                if(c != discs):
                    c.append(a[-1])
                    a.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(a[-1] > c[-1] and a[-1] < b[-1] or b[-1] == 0):
            if(a[-1] != 1):
                if(c != discs):
                    b.append(a[-1])
                    a.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(c[-1] > a[-1] and c[-1] < b[-1] or b[-1] == 0):
            if(c[-1] != 1):
                if(c != discs):
                    b.append(c[-1])
                    c.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(c[-1] > b[-1] and c[-1] < a[-1] or a[-1] == 0):
            if(c[-1] != 1):
                if(c != discs):
                    a.append(c[-1])
                    c.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(b[-1] > c[-1] and b[-1] < a[-1] or a[-1] == 0):
            if(b[-1] != 1):
                if(c != discs):
                    a.append(b[-1])
                    b.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(b[-1] > a[-1] and b[-1] < c[-1] or c[-1] == 0):
            if(b[-1] != 1):
                if(c != discs):
                    c.append(b[-1])
                    b.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

    if(countDiscs % 2 == 1):
        
        if(flag == True):
            if(a[-1] == 1):
                if(b[-1] % 2 == 0 and b[-1] != 0):
                    b.append(a[-1])
                    a.pop(-1)
                                
                elif(c[-1] % 2 == 0):
                    c.append(a[-1])
                    a.pop(-1)

            elif(b[-1] == 1):
                if(a[-1] % 2 == 0 and b[-1] != 0):
                    a.append(b[-1])
                    b.pop(-1)
                                
                elif(c[-1] % 2 == 0):
                    c.append(b[-1])
                    b.pop(-1)

            elif(c[-1] == 1):
                if(a[-1] % 2 == 0):
                    a.append(c[-1])
                    c.pop(-1)
                                
                elif(b[-1] % 2 == 0):
                    b.append(c[-1])
                    c.pop(-1)
            i += 1
                
        print(a, b, c)

        flag = True
        
        if(a[-1] > c[-1] and a[-1] < b[-1] or b[-1] == 0):
            if(a[-1] != 1):
                if(c != discs):
                    b.append(a[-1])
                    a.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        elif(a[-1] > b[-1] and a[-1] < c[-1] or c[-1] == 0):
            if(a[-1] != 1):
                if(c != discs):
                    c.append(a[-1])
                    a.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(b[-1] > c[-1] and b[-1] < a[-1] or a[-1] == 0):
            if(b[-1] != 1):
                if(c != discs):
                    a.append(b[-1])
                    b.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        elif(b[-1] > a[-1] and b[-1] < c[-1] or c[-1] == 0):
            if(b[-1] != 1):
                if(c != discs):
                    c.append(b[-1])
                    b.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        if(c[-1] > b[-1] and c[-1] < a[-1] or a[-1] == 0):
            if(c[-1] != 1):
                if(c != discs):
                    a.append(c[-1])
                    c.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()

        elif(c[-1] > a[-1] and c[-1] < b[-1] or b[-1] == 0):
            if(c[-1] != 1):
                if(c != discs):
                    b.append(c[-1])
                    c.pop(-1)
                    print(a, b, c)
                    i += 1
                    yyy()
            
yyy()
print("Количество ходов =", i)
print(a, b, c)

input("...")

