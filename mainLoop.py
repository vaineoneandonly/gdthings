import inputType, gunfists, whiplance

if __name__ == "__main__":
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

    