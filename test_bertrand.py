import math
import unittest
from bertrand import get_random_point

class TestBertrand(unittest.TestCase):

    def test_getRandomPoint(self):
        point = get_random_point()
        point = math.sqrt(math.pow(point[0],2) + math.pow(point[1], 2))
        self.assertEqual(point, 1) 

    

unittest.main()