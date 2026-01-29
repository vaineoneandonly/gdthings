import inputType, gunfists, whiplance

def agnosticMain(): #Absolute trash, but some valuable lessons learned.
    #myClass = inputType.myWeapon(int(input("type 0 for gunfists, and 1 for whiplance:")))
    c = input("ddlkajslid: ")

    exec("myTransitionTable = " + c + "." + c + "TransitionTable")
    print(myTransitionTable)

    #for classy in inputType.myWeapon:
    #    print(classy)


    #print(myClass)

def currentMain(): #as non-generic as humanly possible. terrible, even.
    myClass = inputType.myWeapon.whiplance
    myInput = inputType.inputType.light

    if (myClass == inputType.myWeapon.whiplance):
        currentState = whiplance.whiplanceComboState.whipNeutral

        while True:
            myInput = inputType.inputType(int(input("0 for light, 1 for heavy, 2 for super: ")))
            currentState = whiplance.whiplanceTransitionTable[currentState.value][myInput.value]

            print(f"you are in {currentState.name} state.\nFrom here, you can go to:")

            for state in whiplance.whiplanceTransitionTable[currentState.value]:
                if state.name != "whipNeutral" and state.name != "lanceNeutral":
                    print(f"{state.name}")

            whiplance.whiplanceProcessState(currentState)

def classifiedClassesMain():
    myClassInput = int(input("0 for gunfists, 1 for whiplance: "))

    match myClassInput:
        case 0:
            player = gunfists.gunfistsClass()
        case 1:
            player = whiplance.whiplanceClass()

    while True:
        print("------------")
        player.showCurrentState()
        print()

        player.showPossibleStates()
        print()

        i = inputType.inputType(int(input("0 for light, 1 for heavy, 2 for super: ")))

        player.processState(i)

if __name__ == "__main__":
    #agnosticMain()
    classifiedClassesMain()   
