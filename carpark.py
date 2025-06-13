from bay import Bay

class Carpark:
    def __init__(self, name, capacity, bays):
        self.name = name
        self.capacity = capacity
        self.bays = bays
        self.license_plates = []

    @classmethod
    def from_config(cls, config):
        name = config["name"]
        capacity = config["capacity"]
        bays = [Bay(i, False) for i in range(capacity)]
        return cls(name, capacity, bays)

    def add_car(self, plate):
        for bay in self.bays:
            if not bay.is_occupied:
                bay.occupy(plate)
                self.license_plates.append(plate)
                return True
        return False

    def remove_car(self, plate):
        for bay in self.bays:
            if bay.plate == plate:
                bay.vacate()
                return True
        return False

    def available_bays(self):
        return [bay for bay in self.bays if not bay.is_occupied]
