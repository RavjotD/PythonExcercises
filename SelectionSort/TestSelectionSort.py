#Import unit test and functin from neccesary .py file
#Use class method to instantiate own fucntion calling for testing.
#Running all valid test cases.
import unittest
from SelectionSort import SelectionSort

class TestSelectionSort(unittest.TestCase):
    def testing_cases(self):
        self.assertEqual(SelectionSort([0,1,0,3,12]),([0,0,1,3,12]))
        self.assertEqual(SelectionSort([3,1,5,2,11]),([1,2,3,5,11]))
        self.assertEqual(SelectionSort([4,3,1,2]),([1,2,3,4]))
        self.assertEqual(SelectionSort([3,2,4]),([2,3,4]))
        self.assertEqual(SelectionSort([1,0,3,5,4]),([0,1,3,4,5]))
      
        
if __name__ == '__main__':
    unittest.main()