class Bay:
    def __init__(self, bay_id, is_occupied, plate=""):
        self.bay_id = bay_id
        self.is_occupied = is_occupied
        self.plate = plate

    def occupy(self, plate):
        self.is_occupied = True
        self.plate = plate

    def vacate(self):
        self.is_occupied = False
        self.plate = ""

    def __str__(self):
        return f"Bay {self.bay_id} - {'Occupied' if self.is_occupied else 'Free'} ({self.plate})"
