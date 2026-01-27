from enum import Enum

#unload discharges the bullets loaded, which you do when standing by pressing the super button.
#Drum discharge (eventually, maybe) lunges you forward like a bullet.

class gunfistsComboState(Enum):
    neutral = 0 #standing.
    reload = 1 #relaoding. 
    jab1 = 2 #light attack1.
    jab2 = 3
    jab3 = 4
    uppercut = 5 #heavy attack1.
    downslam = 6
    straight = 7 #lunges the character forward, consuming three bullets.
    tripleAce = 8 #adds 3 pistol bursts to an attack, consuming three bullets.
    straightFlush = 9 #discharges the barrell, consuming all six bullets.

class inputType(Enum):
    light = 0
    heavy = 1
    super = 2
    empty = 3
                   
transitionTable =   [       #light                          heavy                           super
                        [gunfistsComboState.jab1,    gunfistsComboState.downslam,  gunfistsComboState.straight],      #neutral
                        [gunfistsComboState.jab2,    gunfistsComboState.neutral,   gunfistsComboState.reload],        #reload
                        [gunfistsComboState.jab2,    gunfistsComboState.uppercut,  gunfistsComboState.tripleAce],     #jab1
                        [gunfistsComboState.jab3,    gunfistsComboState.neutral,   gunfistsComboState.tripleAce],     #jab2
                        [gunfistsComboState.neutral, gunfistsComboState.neutral,   gunfistsComboState.reload],        #jab3
                        [gunfistsComboState.jab1,    gunfistsComboState.downslam,  gunfistsComboState.reload],        #uppercut
                        [gunfistsComboState.jab1,    gunfistsComboState.neutral,   gunfistsComboState.straightFlush], #downslam
                        [gunfistsComboState.neutral, gunfistsComboState.neutral,   gunfistsComboState.neutral],       #straight
                        [gunfistsComboState.jab2,    gunfistsComboState.uppercut,  gunfistsComboState.neutral],       #tripleAce
                        [gunfistsComboState.neutral, gunfistsComboState.neutral,   gunfistsComboState.neutral]        #straightFlush
                    ]

if __name__ == "__main__":
    currentState = gunfistsComboState.neutral

    myInput = inputType.heavy
    bullets = 0

    bulletReloadCount = 3
    maxBulletCount = 6
    
    tripleAceCount = 3
    straightCount = 2
    straightFlushCount = 6

    while True:
        match (currentState.name):
            case "reload":
                if (bullets >= maxBulletCount):
                    print("locked and loaded. But a turn wasted.")
                else:
                    print("reloading...")
                    bullets += bulletReloadCount

                    if (bullets > maxBulletCount): 
                        bullets = maxBulletCount

            case "tripleAce":
                if (bullets < tripleAceCount):
                    print("a whiff is a whiff.")
                else:
                    print("bang, bang, bang, cowboy.")
                    bullets -= tripleAceCount

            case "straight":
                if (bullets < straightCount):
                    print("whomp whomp.")
                else:
                    print("fwoosh.")
                    bullets -= straightCount

            case "straightFlush":
                if (bullets < straightFlushCount):
                    print("big heckling whomp.")
                else:
                    print("fwoosh, with a lotta damage.")
                    bullets -= straightFlushCount

        print(f"you are in {currentState.name} state, with {bullets} bullets.\nFrom here, you can go to:")

        for state in transitionTable[currentState.value]:
            if state.name != "neutral":
                print(f"{state.name}")

        myInput = inputType(int((input("0 for light, 1 for heavy, 2 for special: "))))
        currentState = transitionTable[currentState.value][myInput.value]

        print()

        