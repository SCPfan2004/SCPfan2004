function raschet() {
	allVoinAttack = voinAttack * voinCount;
	drakHp -= allVoinAttack;
	allVoinHp -= drakAttack;

	if(allVoinHp % voinHp != 0) {
		voinCount = Math.trunc(allVoinHp / voinHp) + 1;
	} else {
		voinCount = Math.trunc(allVoinHp / voinHp);
	}

	voinHp1Mech = allVoinHp % voinHp;

}

function podbor(allMechAttack, drakonHp, allMechHp, mechHp, mechCount) {

	allMechHp = mechHp * mechCount;

	while(drakonHp > 0 && mechCount > 0) {
		allMechAttack = voinAttack * mechCount;
		drakonHp -= allMechAttack;
		allMechHp -= drakAttack;

		if(allMechHp % mechHp != 0) {
			mechCount = Math.trunc(allMechHp / mechHp) + 1;
		} else {
			mechCount = Math.trunc(allMechHp / mechHp);
		}

		var hp1Voin = allMechHp % mechHp;

		if(drakonHp <= 0) {
			a = false;
			break;
		}
    }
}

var drakHp = prompt("Введите количество жизней дракона: ");
var drakAttack = prompt("Введите урон дракона: ");
var voinHp = prompt("Введите количество жизней мечника: ");
var voinAttack = prompt("Введите урон мечника: ");
var voinCount = 1;
var allVoinAttack = 0;
var allVoinHp = voinCount * voinHp;
var voinHp1Mech = null;

a = true;

while(a) {
	podbor(allVoinAttack, drakHp, allVoinHp, voinHp, voinCount);
	if(a == false) {
		break;
	}
	voinCount++;
}

allVoinHp = voinCount * voinHp;

console.log(drakHp + " - здоровье дракона, " + drakAttack + " - атака дракона. " +
voinCount + " - количество мечников, " + voinHp + " - здоровье мечника, " + voinAttack + " - атака мечника.");

while(drakHp > 0 && voinCount > 0) {

    raschet();

    if(drakHp > 0) {
        console.log("Мечники атакуют (" + allVoinAttack + " урона), у дракона осталось " + drakHp + " здоровья.");
    } else if(drakHp <= 0) {
        console.log("Мечники атакуют (" + allVoinAttack + " урона), дракон убит.");                  
		console.log("Победа!!!")
		break;
    }
        
    if(voinHp1Mech != 0) {
        console.log("Дракон атакует (" + drakAttack + " урона), мечников осталось " + voinCount + ", из которых один раненый (" + voinHp1Mech + " здоровья).")
    } else { 
    	console.log("Дракон атакует (" + drakAttack + " урона), мечников осталось " + voinCount + ".")
    }

}