from modul import House, Building


house1 = House()
house2 = House()
print(house1 == house2)
House.setNewNumberOfFloors(house1, 12)


building1 = Building(4, "офис")
building2 = Building(4, "офис")
building3 = Building(8, "квартира")
building4 = building1

print(building1)

bhg = building1 == building2
print(building2 == building3)
print(building1 == building4)
print(bhg)

