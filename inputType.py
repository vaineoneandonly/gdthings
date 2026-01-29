from enum import Enum

class inputType(Enum):
    light = 0
    heavy = 1
    super = 2

class baseWeaponClass():
    def __init__(self):
        self.comboState = None
        self.transitionTable = None

    def showCurrentState(self):
        print(f"you are on {self.comboState.name}, ", end = "")

    def processState(self, i):
        self.comboState = self.transitionTable[self.comboState.value][i.value]

    def showPossibleStates(self):
        for state in self.transitionTable[self.comboState.value]:
            if state.name != "whipNeutral" and state.name != "lanceNeutral" and state.name != "neutral":
                print(f"{state.name}")
    