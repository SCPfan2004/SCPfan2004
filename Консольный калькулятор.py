spisok = ["**", "//", "*", "/", "%", "-", "+",]
primer = []
i = -1

def opredilenie(massage):
    global i
    a = ""
    flag = True

    while(flag and i != len(massage) - 1):
        i += 1
        a += massage[i]
        
        for g in range(len(spisok)):
            if (i == len(massage) - 1 or massage[i + 1] == spisok[g] or massage[i] == spisok[g] or
                massage[i + 1] == " " or massage[i] == " "):
                flag = False
                
    return a


def schet():
    global primer
    massage = input("Введите пример: ")
    
    while(i != len(massage) - 1):
        b = opredilenie(massage)
        if (b != " "):
            if (b == "*"):
                if(primer[-1] == b):
                    b = "**"
                    primer.pop(-1)
                    primer.append(b)
                    continue
                
            elif(b == "/"):

                if(primer[-1] == b):
                    b = "//"
                    primer.pop(-1)
                    primer.append(b)
                    continue

            primer.append(b)
        
schet()


#print(primer)

b = len(primer)
while(len(primer) != 1):
    for i in range(b - 1):
        while ("**" in primer):
            for i in range(b - 1, 0, -1):
                #print(i)
                if (primer[i] == "**"):
                    summa = float(primer[i - 1]) ** float(primer[i + 1])
                    primer.pop(i + 1)
                    primer.pop(i)
                    primer.pop(i - 1)
                    primer.insert(i - 1, summa)
                    a = len(primer)
                    #print(primer)
                    b = len(primer)
                    break
            if (len(primer) == 1):
                break

        if(len(primer) == 1):
            break
        
        if ("*" in primer or "/" in primer or "//" in primer or "%" in primer):
            if (primer[i] == "*"):
                summa = float(primer[i - 1]) * float(primer[i + 1])
                primer.pop(i + 1)
                primer.pop(i)
                primer.pop(i - 1)
                primer.insert(i - 1, summa)
                a = len(primer)
                #print(primer)
                break

            if (primer[i] == "/"):
                summa = float(primer[i - 1]) / float(primer[i + 1])
                primer.pop(i + 1)
                primer.pop(i)
                primer.pop(i - 1)
                primer.insert(i - 1, summa)
                a = len(primer)
                #print(primer)
                break

            if (primer[i] == "//"):
                summa = float(primer[i - 1]) // float(primer[i + 1])
                primer.pop(i + 1)
                primer.pop(i)
                primer.pop(i - 1)
                primer.insert(i - 1, summa)
                a = len(primer)
                #print(primer)
                break

            if (primer[i] == "%"):
                summa = float(primer[i - 1]) % float(primer[i + 1])
                primer.pop(i + 1)
                primer.pop(i)
                primer.pop(i - 1)
                primer.insert(i - 1, summa)
                a = len(primer)
                #print(primer)
                break

        
        elif (primer[i] == "+"):
            summa = float(primer[i - 1]) + float(primer[i + 1])
            primer.pop(i + 1)
            primer.pop(i)
            primer.pop(i - 1)
            primer.insert(i - 1, summa)
            a = len(primer)
            #print(primer)
            break

        
        elif (primer[i] == "-"):
            summa = float(primer[i - 1]) - float(primer[i + 1])
            primer.pop(i + 1)
            primer.pop(i)
            primer.pop(i - 1)
            primer.insert(i - 1, summa)
            a = len(primer)
            #print(primer)
            break   


if (primer[i - 1] - int(primer[i - 1]) > 0):
    print(primer[i - 1])

else:
    print(int(primer[i - 1]))
