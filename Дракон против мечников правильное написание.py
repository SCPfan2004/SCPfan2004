def raschet():
    global drakHp, drakAttack, voinCount, voinHp, voinAttack, voinHp1Mech, allVoinHp, allVoinAttack

    allVoinAttack = voinAttack * voinCount
    drakHp -= allVoinAttack
    allVoinHp -= drakAttack
    if(allVoinHp % voinHp != 0):
        voinCount = (allVoinHp // voinHp) + 1
    else:
        voinCount = allVoinHp // voinHp
    voinHp1Mech = allVoinHp % voinHp

def podbor(allMechAttack, drakonHp, allMechHp, mechHp, mechCount):
    global a
    
    allMechHp = mechHp * mechCount
    while(drakonHp > 0 and mechCount > 0):
        allMechAttack = voinAttack * mechCount
        drakonHp -= allMechAttack
        allMechHp -= drakAttack
        if(allMechHp % mechHp != 0):
            mechCount = (allMechHp // mechHp) + 1
        else:
            mechCount = allMechHp // mechHp
        hp1Voin = allMechHp % mechHp
        if(drakonHp <= 0):
            a = False
            break

drakHp = int(input("Введите количество здоровья дракона: "))
drakAttack = int(input("Введите атаку дракона: "))
voinCount = 1
voinHp = int(input("Введите количество здоровья мечника: "))
allVoinHp = voinCount * voinHp
voinAttack = int(input("Введите атаку мечника: "))
allVoinAttack = 0

a = True
while(a):
    podbor(allVoinAttack, drakHp, allVoinHp, voinHp, voinCount)
    if(a == False):
        break
    voinCount += 1

allVoinHp = voinHp * voinCount

print(f"""{drakHp} - здоровье дракона, {drakAttack} - атака дракона.
{voinCount} - количество мечников, {voinHp} - здоровье мечника, {voinAttack} - атака мечника.""" + "\n")

while(drakHp > 0 and voinCount > 0):

    raschet()

    if(drakHp > 0):
        print(f"Мечники атакуют ({allVoinAttack} урона), у дракона осталось {drakHp} здоровья.")
    elif(drakHp <= 0):
        print(f"""Мечники атакуют ({allVoinAttack} урона), дракон убит.
Победа!!!""")
        break
        
    if(voinHp1Mech != 0):
        print(f"Дракон атакует ({drakAttack} урона), мечников осталось {voinCount}, из которых один раненый ({voinHp1Mech} здоровья)." + "\n")
    else: 
        print(f"Дракон атакует ({drakAttack} урона), мечников осталось {voinCount}." + "\n")
