import inputType

class g2ComboState(inputType.Enum):
    neutral = 0
    reload = 1
    jab1 = 2
    jab2 = 3
    jab3 = 4
    uppercut = 5
    hook = 6
    tripleAce = 7
    flush = 8
    deadMansHand = 9
    lastManStanding = 10
    discharge = 11

g2TransitionTable = [
    #         light               heavy                    super
    [g2ComboState.jab1,     g2ComboState.uppercut,  g2ComboState.neutral],          #neutral
    [g2ComboState.neutral,  g2ComboState.uppercut,  g2ComboState.reload],           #reload
    [g2ComboState.jab2,     g2ComboState.neutral,   g2ComboState.neutral],          #jab1
    [g2ComboState.jab3,     g2ComboState.uppercut,  g2ComboState.neutral],          #jab2
    [g2ComboState.neutral,  g2ComboState.neutral,   g2ComboState.reload],           #jab3
    [g2ComboState.neutral,  g2ComboState.discharge, g2ComboState.tripleAce],        #uppercut
    [g2ComboState.jab1,     g2ComboState.discharge, g2ComboState.tripleAce],        #hook
    [g2ComboState.neutral,  g2ComboState.hook,      g2ComboState.flush],            #tripleAce
    [g2ComboState.jab2,     g2ComboState.neutral,   g2ComboState.lastManStanding],  #flush
    [g2ComboState.neutral,  g2ComboState.neutral,   g2ComboState.neutral],          #deadMansHand
    [g2ComboState.neutral,  g2ComboState.neutral,   g2ComboState.neutral],          #lastManStanding
    [g2ComboState.neutral,  g2ComboState.neutral,   g2ComboState.deadMansHand]      #discharge
]
class gunfistsClass(inputType.baseWeaponClass):
    def __init__(self):
        self.comboState = g2ComboState.neutral
        self.transitionTable = g2TransitionTable

        self.bullets = 0
        self.bulletReloadCount = 3
        self.maxBulletCount = 6
        self.tripleAceCount = 3
        self.flushCount = 2

    def showCurrentState(self):
        super().showCurrentState()
        print(f"{self.bullets} bullets in the chamber.")

    def processState(self, i):
        super().processState(i)

        match self.comboState:
            case g2ComboState.reload:
                if (self.bullets >= self.maxBulletCount):
                    print("locked and loaded. But a turn wasted.")
                else:
                    print("reloading...")
                    self.bullets += self.bulletReloadCount

                    if (self.bullets > self.maxBulletCount): 
                        self.bullets = self.maxBulletCount 

            case g2ComboState.tripleAce:
                if (self.bullets < self.tripleAceCount):
                    print("a whiff is a whiff.")
                else:
                    print("bang, bang, bang, cowboy.")
                    self.bullets -= self.tripleAceCount
            
            case g2ComboState.flush:
                if (self.bullets < self.flushCount):
                    print("whomp whomp.")
                else:
                    print("fwoosh.")
                    self.bullets -= self.flush

            case g2ComboState.deadMansHand:
                if (self.bullets != 0):
                    print("nope!")
                else:
                    print("it's high noon. What the hell are we doing with this state btw")

            case g2ComboState.lastManStanding:
                if (self.bullets != 1):
                    print("there can only be one.")
                else:
                    print("one shot to raelly hurt.")

            case g2ComboState.discharge:
                if (self.bullets == 0):
                    print("no bullets left in your chamber, cowboy.")
                else:
                    print("bang!" * self.bullets, end = " ")
                    print()

                self.bullets = 0