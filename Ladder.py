class Ladder:
    existingInstances = 0

    def __init__(self, brand="unknown", maxLength=0, maxWeight=0, material="unknown", isFoldable="unknown",
                 color="unknown", amountOfSteps=0):
        self.brand = brand
        self.maxLength = maxLength
        self.maxWeight = maxWeight
        self.material = material
        self.isFoldable = isFoldable
        self.color = color
        self.amountOfSteps = amountOfSteps
        Ladder.existingInstances += 1

    def __str__(self):
        return f"Brand: {self.brand} Max length: {self.maxLength} Max weight: {self.maxWeight} " \
               f"Material: {self.material} Is foldable: {self.isFoldable} Color: {self.color} " \
               f"Steps: {self.amountOfSteps}"

    def __del__(self):
        Ladder.existingInstances -= 1

    @staticmethod
    def getAmountOfInstances():
        return Ladder.existingInstances


if __name__ == '__main__':
    ladderEqual = Ladder("EQUAL", 200, 210, "Steel", True, "red", 6)
    ladderDefault = Ladder()
    ladderLittleGiant = Ladder("Little Giant", 250, 175)

    print(ladderEqual.__str__())
    print(ladderDefault.__str__())
    print(ladderLittleGiant.__str__())
    print(Ladder.getAmountOfInstances())
