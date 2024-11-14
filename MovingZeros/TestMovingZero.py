#Import unit test and function from necessary .py file
#Use class method to instantiate own function calling for testing.
#Running all valid test cases.

import unittest
from MovingZero import MoveZeros

class TestingMovingZeros(unittest.TestCase):
    def testing_cases(self):
        self.assertEqual(MoveZeros([0,1,0,3,12]),([1,3,12,0,0]))
        self.assertEqual(MoveZeros([0, 1, 0, 2, 0, 3, 0, 4]),([1,2,3,4,0,0,0,0]))
        self.assertEqual(MoveZeros([0, 0, 1, 2, 3]),([1,2,3,0,0]))
        self.assertEqual(MoveZeros([1, 2, 3, 4, 5]),([1,2,3,4,5]))
        self.assertEqual(MoveZeros([1, 0, 2, 0, 3, 0, 4, 5, 0, 6, 7, 0, 8]),([1,2,3,4,5,6,7,8,0,0,0,0,0]))
        self.assertEqual(MoveZeros([0, 1]),([1,0]))
        self.assertEqual(MoveZeros([0,0,0,0]),([0,0,0,0]))
        
if __name__ == '__main__':
    unittest.main()
