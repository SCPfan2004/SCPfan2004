def factorial():
    global i, b
    
    i += 1
    b *= i
    
    if(i == a):
        print(f"Факториал числа {a} = {b}")
    else:
        factorial()

a = int(input("Введите число для факториала: "))
i = 0
b = 1

factorial()
print(b)
