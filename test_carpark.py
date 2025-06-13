import unittest
from carpark import Carpark
from bay import Bay

class TestCarpark(unittest.TestCase):
    def setUp(self):
        bays = [Bay(i, False) for i in range(3)]
        self.cp = Carpark("Test Lot", 3, bays)

    def test_add_car(self):
        result = self.cp.add_car("XYZ123")
        self.assertTrue(result)

    def test_remove_car(self):
        self.cp.add_car("XYZ123")
        result = self.cp.remove_car("XYZ123")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
