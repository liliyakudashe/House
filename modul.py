class House:

    numberOfFloors = 10

    def print_floors(self):
        for floors in range(1, self.numberOfFloors+1):
            print("Текущий этаж равен", floors)

