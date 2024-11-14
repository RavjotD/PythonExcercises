#Import unit test and functin from neccesary .py file
#Use class method to instantiate own fucntion calling for testing.
#Running all valid test cases.
import unittest
from SelectionSort import SelectionSort

class TestSelectionSort(unittest.TestCase):
    def testing_cases(self):
        self.assertEqual(SelectionSort([0,1,0,3,12]),([0,0,1,3,12]))
        self.assertEqual(SelectionSort([]),([]))
        self.assertEqual(SelectionSort([]),([]))
        self.assertEqual(SelectionSort([]),([]))
        self.assertEqual(SelectionSort([]),([]))
        self.assertEqual(SelectionSort([]),([]))
        self.assertEqual(SelectionSort([]),([]))
        
if __name__ == '__main__':
    unittest.main()