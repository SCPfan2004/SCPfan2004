from ctypes import *
import random
import time
import os

valuta = "монет"
money = 0
startMoney = 0
playGame = True
defaultMoney = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
        
def pobeda(result):
    color(14)
    print(f"    Поздравляю, Ты победил! Выигрыш составил: {result} {valuta}.")
    print(f"    Твой счёт составляет: {money} {valuta}.")

def lose(result):
    color(12)
    print(f"    К щастью для меня, ты проиграл: {result} {valuta}.")
    print(f"    Твой счёт составляет: {money} {valuta}.")
    print(f"    Тебе обязательно нужно отыграться!")

def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close
    except:
        print("Ошибка создания файла, наше Казино закрывается!")
        quit(0)

def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)

def colorLine(c, s):
    os.system("cls")
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))

def getInput(digit, message):
    color(7)
    ret= ""
    while(ret =="" or not ret in digit):
        ret = input(message)
    return ret
    
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while(ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print("    Введи целое число!")
    return ret

def getRuletka(visible):
    tickTime = random.randint(100, 120) / 10000
    mainTime = 0
    number = random.randint(0, 38)
    increaseTickTime = random.randint(100, 110) / 100
    col = 1

    while(mainTime < 0.7):
        col += 1
        if(col > 15):
            col = 1
        mainTime += tickTime
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if(number > 38):
            number = 0
            print()
            
        printNumber = number
        if(number == 37):
            printNumber = "00"
        elif(number == 38):
            printNumber = "000"

        print("Число >",
              printNumber,
              "*" * number,
              " " * (79 - number * 2),
              "*" * number)
        if(visible):
            time.sleep(mainTime)
            
    return number

def ruletka():
    global money
    playGame = True

    while(playGame > 0 and money > 0):
        colorLine(3, "Добро пожаловать на игру в рулетку!")
        color(14)
        print(f"У тебя на счету {money} {valuta}")
        color(11)
        print(" Cтавлю на...")
        print("    1. Чётное (выйгрыш 1:1)")
        print("    2. Нечётное (выйгрыш 1:1)")
        print("    3. Дюжина (выйгрыш 3:1)")
        print("    4. Число (выйгрыш 36:1)")
        print("    0. Возврат в предыдущее меню")

        x = getInput("01234", "    Твой выбор? ")

        playRuletka = True

        if(x == "3"):
            color(2)
            print()
            print(" Выбери числа:...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад")
            
            duzhina = getInput("0123", "    Твой выбор? ")

            if(duzhina == "1"):
                textDuzhina = "от 1 до 12"
            elif(duzhina == "2"):
                textDuzhina = "от 13 до 24"
            elif(duzhina == "3"):
                textDuzhina = "от 25 до 36"
            elif(duzhina == "0"):
                playRuletka = False
        elif(x == "4"):
            chislo = getIntInput(0, 36, f"    На какое число ставишь? (0...36):")

        color(7)
        if(x == "0"):
            return 0

        if(playRuletka):
            stavka = getIntInput(0, money, f"    Сколько поставишь? (не больше {money}):")
            if(stavka == 0):
                return 0

            number = getRuletka(True)

            print()
            color(11)

            if(number < 37):
                print(f"    Выпало число {number}! " + "*" * number)
            else:
                if(number == 37):
                    printNumber = "00"
                elif(number == 38):
                    printNumber = "000"
                print(f"    Выпало число {printNumber}!")

            if(x == "1"):
                print("    Ты ставил на ЧЁТНОЕ!")
                if(number < 37 and number % 2 == 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    lose(stavka)
                    
            elif(x == "2"):
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if(number < 37 and number % 2 != 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    lose(stavka)

            elif(x == "3"):
                print(f"    Ставка сделана на диапазон чисел {textDuzhina}.")
                winDuzhina = ""
                if(number > 0 and number < 13):
                    winDuzhina = "1"
                elif(number > 12 and number < 25):
                    winDuzhina = "2"
                elif(number > 24 and number < 37):
                    winDuzhina = "3"

                if(duzhina == winDuzhina):
                    money += stavka * 2
                    pobeda(stavka * 3)
                else:
                    money -= stavka
                    lose(stavka)
                    
            elif(x == "4"):
                print(f"    Ставка сделана на число {chislo}")
                if(number == chislo):
                    money += stavka * 35
                    pobeda(stavka * 36)
                else:
                    money -= stavka
                    lose(stavka)
            print()
            input(" Нажми Enter для продолжения...")
    

def getKosti():
    count = random.randint(3, 8)
    sleep = 0
    while(count > 0):
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, f"-----", f"  -----")
        print(" " * 10, f"| {y} |", f"  | {x} |")
        print(" " * 10, f"-----", f"  -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
        
    return x + y

def kosti():
    global money
    playGame = True
    while(playGame and money > 0):
        print()
        colorLine(3, "Добро пожаловать на игру в кости!")
        color(14)
        print(f"У тебя на счету {money} {valuta}")
        color(7)
        stavka = getIntInput(0, money, f"Сделай ставку в пределах {money} {valuta}: ")
        if(stavka == 0):
            return 0
        playRound = True
        control = stavka
        oldResult = getKosti()
        firstPlay = True
        while(playRound > 0 and stavka > 0 and money > 0):
            if(stavka > money):
                stavka = money
            color(11)
            print(f"В твоём распоряжении {stavka} {valuta}")
            color(12)
            print(f"Текущая сумма чисел на костях: {oldResult}")
            color(11)
            print("Сумма чисел на гранях будет больше, меньше, или равна предыдущей?")
            color(7)
            x = getInput("0123", "    Введи 1 - больше, 2 - меньше, 3 - равна, или 0 - выход: ")

            if(x != "0"):
                firstPlay = False
                if(stavka > money):
                    stavka = money
                money -= stavka
                kostiResult = getKosti()
                    
                win = False
                if(oldResult > kostiResult and x == "2"):
                    win = True
                if(oldResult < kostiResult and x == "1"):
                    win = True
                if(not x == "3"):
                    if(win):
                        money += stavka * 2
                        pobeda(stavka * 2)
                    else:
                        stavka = control
                        lose(stavka)
                elif(x == "3"):
                    if(oldResult == kostiResult):
                        money += stavka * 6
                        pobeda(stavka * 5)
                        stavka *= 3
                    else:
                        stavka = control
                        lose(stavka)
                oldResult = kostiResult
            elif(x == "0"):
                if(firstPlay):
                    money -= stavka
                playRound = False
    

def bandit():
    global money
    playGame = True
    while(playGame):
        colorLine(3, "Добро пожаловать на игру в однорукого бандита!")
        color(14)
        print(f"У тебя на счету {money} {valuta}")
        color(5)
        print("""Правила игры:
        1. При совпадении 2-х чисел ставка не списывается.
        2. При совпадении 3-х чисел выигрыш 2:1.
        3. При совпадении 4-х чисел выигрыш 5:1.
        4. При совпадении 5-ти чисел выигрыш 10:1.
        5. Ставка 0 для завершения игры""")
        stavka = getIntInput(0, money, f"Введи ставку в пределах {money} {valuta}: ")
        if(stavka == 0):
            return 0
        money -= stavka
        money += getBandRes(stavka)
        if(money <= 0):
            playGame = False
    
def getBandRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col = 10

    while(getD1 or getD2 or getD3 or getD4 or getD5):
        if(getD1):
            d1 += 1
        if(getD2):
            d2 -= 1
        if(getD3):
            d3 += 1
        if(getD4):
            d4 -= 1
        if(getD5):
            d5 += 1

        if(d1 > 9):
            d1 = 0
        if(d2 < 0):
            d2 = 9
        if(d3 > 9):
            d3 = 0
        if(d4 < 0):
            d4 = 9
        if(d5 > 9):
            d5 = 0

        if(random.randint(0, 20) == 1):
            getD1 = False
        if(random.randint(0, 20) == 1):
            getD2 = False
        if(random.randint(0, 20) == 1):
            getD3 = False
        if(random.randint(0, 20) == 1):
            getD4 = False
        if(random.randint(0, 20) == 1):
            getD5 = False

        time.sleep(0.1)
        color(col)
        col += 1
        if(col > 15):
            col = 10
        print("    " + "%" * 10)
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if(maxCount < getMaxCount(d2, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if(maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if(maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if(maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if(maxCount == 2):
        print(f"  Совпадение двух чисел! Ты ничего не потерял: {res}")
    elif(maxCount == 3):
        res *= 2
        print(f"  Совпадение трёх чисел! Твой выигрыш 2:1 {res}")
    elif(maxCount == 4):
        res *= 5
        print(f"  Совпадение ЧЕТЫРЁХ чисел! Твой выигрыш 5:1 {res}")
    elif(maxCount == 5):
        res *= 10
        print(f"  БИНГО!!! Совпадение ВСЕХ ЧИСЕЛ!!! Твой выигрыш 10:1 {res}")
    else:
        lose(res)
        res = 0
    color(11)
    print()
    input("Нажми Enter для продолжения...")

    return res

def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if(digit == v1):
        ret += 1
    if(digit == v2):
        ret += 1
    if(digit == v3):
        ret += 1
    if(digit == v4):
        ret += 1
    if(digit == v5):
        ret += 1
    return ret

def main():
    global money, playGame
    money = loadMoney()
    startMoney = money

    while(playGame > 0 and money > 0):
        colorLine(10, "Приветсвую тебя в нашем казино, дружище!")
        color(14)
        print(f"У тебя на счету: {money} {valuta}")
        color(6)
        print(" Ты можешь сыграть в:")
        print("    1. Рулетку")
        print("    2. Кости")
        print("    3. Однорукого бандита")
        print("    0. Выход. Ставка 0 в играх - выход.")
        color(7)

        x = getInput("0123", "    Твой выбор? ")

        if(x == "0"):
            playGame = 0
        elif(x == "1"):
            ruletka()
        elif(x == "2"):
            kosti()
        elif(x == "3"):
            bandit()
    
    color(11)
    if(money > startMoney):
        print("Ну что ж, поздравляю с прибылью!")
        print(f"На начало игры у тебя было: {startMoney} {valuta}.")
        print(f"Сейчас на твоём счету: {money} {valuta}! Приходи ещё!")
    elif(money < startMoney):
        print(f"Ты остался в минусе на: {startMoney - money} {valuta}.")
        print("В следующий раз всё обязательно получится!")
    elif(money == defaultMoney):
        print("По крайней мере, ты ничего не потерял.")
    elif(money <= 0):
        print("Мне жаль но у тебя закончились деньги.")
    input("Enter... ")

    saveMoney(money)

    color(7)
    
    quit(0)

main()



        
