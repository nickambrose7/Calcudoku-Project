import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
      
   # ADD MORE TESTS!!!! 

   def test_check_row1(self):
      row = [1, 2, 3, 4, 5]
      self.assertTrue(check_row(row), True)

   def test_check_row2(self):
      row = [1, 2, 1, 4, 5]
      self.assertFalse(check_row(row), False)

   def test_check_row3(self):
      row = [1, 0, 0, 0, 0]
      self.assertTrue(check_row(row), True)

   def test_check_row4(self):
      row = [1, 1, 1, 1, 0]
      self.assertFalse(check_row(row), False)

   def test_check_row5(self):
      row = [1, 2, 6, 4, 5]
      self.assertFalse(check_row(row), False)

   

   def test_check_rows0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle), True)

   def test_check_rows1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 5, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_rows_valid(puzzle), False)


   def test_check_rows2(self):
      puzzle = []
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle), True)

   def test_check_rows3(self):
      puzzle = []
      puzzle.append([5, 1, 2, 5, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 3, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_rows_valid(puzzle), False)



'''  
   def test_check_columns0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_columns_valid(puzzle))
      
   def test_check_cages0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_cages_valid(puzzle, cages))
      
   def test_check_valid0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_valid(puzzle, cages))
'''
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

