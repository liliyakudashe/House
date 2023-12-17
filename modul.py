class House:

    numberOfFloors = 10

    def __init__(self):
        self.numberOfFloors = 10

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Текущий этаж равен", self.numberOfFloors)

    def printFloors(self):
        for floor in range(1, self.numberOfFloors + 1):
            print("Текущий этаж равен", floor)


class Building:

    total = 0

    def __init__(self, floors, building_type):
        self.numberOfFloors = floors
        self.buildingType = building_type
        Building.total += 1

    def __eq__(self, other):
        if isinstance(other, Building):
            return (self.numberOfFloors == other.numberOfFloors
                    and self.buildingType == other.buildingType)
        return False

    def __str__(self):
        return f'{self.buildingType}, {self.numberOfFloors}'


