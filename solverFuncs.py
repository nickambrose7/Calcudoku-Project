# These are the required functions for this project.
#
# I highly recommend adding functions to check a single
# row, check a single column, and check a single cage.

def check_rows_valid(puzzle):


   pass
       
def check_row(row):
	
	for i in range(len(row)):
		for j in range(len(row)):
			if row[i] == row[j] and i != j and row[i] != 0 and row[j] != 0 or row[i] > 5 and row[j] > 5: #compares every number in the list and ensures there are no duplicates AT DIFFERENT INDEXES. Excludes 0. returns False if value in row is greater than 5
				return False

	return True


def check_columns_valid(puzzle):
   pass

def check_column(puzzle, col_num):
	pass


def check_cages_valid(puzzle, cages):
   pass

def check_cage(puzzle, cage):
	pass

       
def check_valid(puzzle, cages):
   pass

def get_cages():
   pass
