import unittest

from flightpath import FlightPlath

class TestFlightPlath(unittest.TestCase):

    def setUp(self):
        self.indeces = ['Castle Black', 'Winterfell', 'Riverrun', 'Kings Landing']
        self.priceMatrix = [[0, 15, 80, 90], [0, 0, 40, 50], [0, 0, 0, 70], [0, 0, 0, 0]]
        self.fp = FlightPlath(self.priceMatrix, self.indeces)

    def test_findPathAndPrice(self):
        source = 'Castle Black'
        destination = 'Kings Landing'
        sourceIndex, destinationIndex = self.indeces.index(source), self.indeces.index(destination)

        paths = self.fp.findPathAndPrice(sourceIndex, destinationIndex)
        expected_paths = [[(0, 0), (1, 15), (2, 40), (3, 70)], 
         [(0, 0), (1, 15), (3, 50)], 
         [(0, 0), (2, 80), (3, 70)], 
         [(0, 0), (3, 90)]] 
        self.assertEqual(paths, expected_paths)

    def test_findPrice(self):
        source = 'Castle Black'
        destination = 'Kings Landing'
        sourceIndex, destinationIndex = self.indeces.index(source), self.indeces.index(destination)

        total_prices = self.fp.findPrice(sourceIndex, destinationIndex)
        expected_prices = [110, 65, 150, 90]

        self.assertEqual(total_prices, expected_prices)
    
if __name__ == '__main__':
    unittest.main()
