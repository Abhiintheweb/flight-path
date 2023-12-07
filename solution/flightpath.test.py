import unittest

from flightpath import FlightPlath

class TestFlightPlath(unittest.TestCase):

    def setUp(self):
        self.indeces = ['Castle Black', 'Winterfell', 'Riverrun', 'Kings Landing']
        self.priceMatrix = [[0, 15, 80, 90], [0, 0, 40, 50], [0, 0, 0, 70], [0, 0, 0, 0]]
        self.fp = FlightPlath(self.priceMatrix, self.indeces)

    def test_flight_path(self):
        source = 'Castle Black'
        destination = 'Kings Landing'
        sourceIndex, destinationIndex = self.indeces.index(source), self.indeces.index(destination)

        paths = self.fp.flightPath(sourceIndex, destinationIndex)
        expected_paths =  [([0, 3], 90), ([0, 2, 3], 150), ([0, 1, 3], 65), ([0, 1, 2, 3], 125)]
        self.assertEqual(paths, expected_paths)
    def test_flightPath_with_same_source_destination(self):
        source = 'Castle Black'
        destination = 'Kings Landing'
        sourceIndex, destinationIndex = self.indeces.index(source), self.indeces.index(destination)
        try:
            paths = self.fp.flightPath(sourceIndex, sourceIndex)
        except Exception:
            self.assertRaises(Exception)
    
    def test_flightPath_with_out_of_boundery_source_destination(self):
        source = 'Castle Black'
        destination = 'Kings Landing'
        # sourceIndex, destinationIndex = self.indeces.index(source), self.indeces.index(destination)
        try:
            paths = self.fp.flightPath(99, -11)
        except Exception:
            self.assertRaises(Exception)
        
        


    
    
if __name__ == '__main__':
    unittest.main()
