class vehicles:
    count = 0
    def __init__(self, value):
        self.value = value
        vehicles.count += 1

    def getval(self):
        return self.value

    def getcount(cls):
        return vehicles.count

    counter = classmethod(getcount)

type1 = vehicles("Car")
type2 = vehicles("Bus")
type3 = vehicles("Bikes")

print(type1.getval(), type2.getval(), vehicles.counter(), type2.getcount())
