class House:

    def __init__(self):
        self.numberOfFloors = 10

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Текущий этаж равен", self.numberOfFloors)

