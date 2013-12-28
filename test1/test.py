import csv
import unittest

class TestSharePrice(unittest.TestCase):

    def setUp(self):
        self.datafile = open('datagen.csv', 'r')
        self.read = csv.reader(self.datafile)
        self.name = next(self.read)[:]
        for row in self.read:
            self.year, self.month = row[:2]
            break
             
    def test_yearmonthshareprice(self):
        year, month = 1990, 'jan'
        self.assertEqual(self.year, str(year))
        self.assertEqual(self.month, month)
        
if __name__ == '__main__':
    unittest.main()
    
