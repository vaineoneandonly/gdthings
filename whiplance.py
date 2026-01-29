import inputType

class whiplanceComboState(inputType.Enum):
    whipNeutral = 0
    lanceNeutral = 1

    morphToLance = 2
    morphToWhip = 3

    whipcrack1 = 4
    whipcrack2 = 5
    whipcrack3 = 6

    poke1 = 7
    poke2 = 8
    poke3 = 9

    empowerLance = 10
    empowerWhip = 11

    whipLasso = 12
    lanceThrust = 13

    backswing = 14
    constrict = 15

    whipCarousel = 16
    lanceTornado = 17

whiplanceTransitionTable = [
    #        light                               heavy                                 super
    [whiplanceComboState.whipcrack1,    whiplanceComboState.whipLasso,      whiplanceComboState.whipNeutral],   #whipNeutral  
    [whiplanceComboState.poke1,         whiplanceComboState.lanceThrust,    whiplanceComboState.lanceNeutral],  #lanceNeutral
    [whiplanceComboState.poke1,         whiplanceComboState.lanceThrust,    whiplanceComboState.empowerWhip],   #morphToLance
    [whiplanceComboState.whipcrack1,    whiplanceComboState.whipLasso,      whiplanceComboState.empowerLance],  #morphToWhip
    [whiplanceComboState.whipcrack2,    whiplanceComboState.whipNeutral,    whiplanceComboState.whipNeutral],   #whipcrack1
    [whiplanceComboState.whipcrack3,    whiplanceComboState.whipLasso,      whiplanceComboState.whipNeutral],   #whipcrack2
    [whiplanceComboState.whipNeutral,   whiplanceComboState.whipNeutral,    whiplanceComboState.morphToLance],  #whipcrack3
    [whiplanceComboState.poke2,         whiplanceComboState.lanceNeutral,   whiplanceComboState.lanceNeutral],  #poke1
    [whiplanceComboState.poke3,         whiplanceComboState.lanceThrust,    whiplanceComboState.lanceNeutral],  #poke2
    [whiplanceComboState.lanceNeutral,  whiplanceComboState.lanceThrust,    whiplanceComboState.morphToWhip],   #poke3
    [whiplanceComboState.whipcrack1,    whiplanceComboState.whipLasso,      whiplanceComboState.whipNeutral],   #empowerLance
    [whiplanceComboState.poke1,         whiplanceComboState.lanceThrust,    whiplanceComboState.lanceNeutral],  #empowerWhip
    [whiplanceComboState.whipNeutral,   whiplanceComboState.constrict,      whiplanceComboState.whipCarousel],  #whipLasso
    [whiplanceComboState.lanceNeutral,  whiplanceComboState.backswing,      whiplanceComboState.lanceTornado],  #lanceThrust
    [whiplanceComboState.lanceNeutral,  whiplanceComboState.lanceNeutral,   whiplanceComboState.morphToWhip],   #backswing
    [whiplanceComboState.whipNeutral,   whiplanceComboState.whipNeutral,    whiplanceComboState.morphToLance],  #constrict
    [whiplanceComboState.lanceNeutral,  whiplanceComboState.lanceNeutral,   whiplanceComboState.lanceNeutral],  #whipCarousel
    [whiplanceComboState.lanceNeutral,  whiplanceComboState.lanceNeutral,   whiplanceComboState.lanceNeutral]   #lanceTornado
]

whipEmpowered = False
lanceEmpowered = False

def whiplanceProcessState(state):
    global whipEmpowered, lanceEmpowered

    match state.name:
        case "empowerLance":
            print("lance powered up and ready to go.")
            lanceEmpowered = True

        case "empowerWhip":
            print("whip powered up and ready to go.")
            whipEmpowered = True

        case "backswing":
            print("you toss your lance backwards, creating a wavy motion.")

        case "constrict":
            print("you squeeze the last bit of breath out of your enemy.")
        
        case "whipCarousel":
            if (whipEmpowered and lanceEmpowered):
                print("absolutely menacing double squandering with your whip.")
                lanceEmpowered = False
            elif (whipEmpowered):
                print("wahooooooooooie. We're going on a field trip, Jex!")
            else:
                print("Jex?")

            whipEmpowered = False

        case "lanceTornado":
            if (whipEmpowered and lanceEmpowered):
                print("thruuuuuust like Katrina!")
                whipEmpowered = False
            elif (lanceEmpowered):
                print("the storm approaches.")
            else:
                print("it's a rainy summer day in the summer of Rio Grande.")

            lanceEmpowered = False

hue = "bjkhdsk"

class whiplanceClass(inputType.baseWeaponClass):
    def __init__(self):
        self.comboState = whiplanceComboState.whipNeutral
        self.transitionTable = whiplanceTransitionTable

        self.whipEmpowered = False
        self.lanceEmpowered = False

    def showCurrentState(self):
        super().showCurrentState()
        if self.whipEmpowered and self.lanceEmpowered:
            print("with both tools charged and ready for a big boom!")
        elif self.whipEmpowered:
            print("charged whip in hand.")
        elif self.lanceEmpowered:
            print("charged lance in hand.")
        else:
            print("with both tools uncharged. Tough luck.")

    def processState(self, i):
        super().processState(i)

        match self.comboState:
            case whiplanceComboState.empowerLance:
                print("lance powered up and ready to go.")
                self.lanceEmpowered = True

            case whiplanceComboState.empowerWhip:
                print("whip powered up and ready to go.")
                self.whipEmpowered = True

            case whiplanceComboState.backswing:
                print("you toss your lance backwards, creating a wavy motion.")

            case whiplanceComboState.constrict:
                print("you squeeze the last bit of breath out of your enemy.")

            case whiplanceComboState.whipCarousel:
                if (self.whipEmpowered and self.lanceEmpowered):
                    print("absolutely menacing double squandering with your whip.")
                    self.lanceEmpowered = False
                elif (self.whipEmpowered):
                    print("wahooooooooooie. We're going on a field trip, Jex!")
                else:
                    print("Jex?")

                self.whipEmpowered = False

            case whiplanceComboState.lanceTornado:
                if (self.whipEmpowered and self.lanceEmpowered):
                    print("thruuuuuust like Katrina!")
                    self.whipEmpowered = False
                elif (self.lanceEmpowered):
                    print("the storm approaches.")
                else:
                    print("it's a rainy summer day in the summer of Rio Grande.")

                self.lanceEmpowered = False
