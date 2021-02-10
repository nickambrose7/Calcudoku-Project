# These are the required functions for this project.
#
# I highly recommend adding functions to check a single
# row, check a single column, and check a single cage.

def check_rows_valid(puzzle):

	for i in range(len(puzzle)):
		
		if check_row(puzzle[i]):
			
			return True
		
		else:
			
			return False

       
def check_row(row):
	
	for i in range(len(row)):
		
		for j in range(len(row)):
			
			if row[i] == row[j] and i != j and row[i] != 0 and row[j] != 0 or row[i] > 5 and row[j] > 5: #compares every number in the list and ensures there are no duplicates AT DIFFERENT INDEXES. Excludes 0. returns False if value in row is greater than 5
				
				return False

	return True


def check_columns_valid(puzzle):
   pass

def check_column(puzzle, col_num):

	col_list = []

	for i in range(len(puzzle)): #goes through each row
		
		item = puzzle[i][col_num] #pulls out the number in the specified column for each row
		
		col_list.append(item) #poplulates list with all numbers from specified column

	for j in range(len(col_list)): #Same logic as check row except it uses the list of a column now.

		for k in range(len(col_list)):

			if col_list[j] == col_list[k] and j != k and col_list[j] != 0 and col_list[k] != 0 or col_list[j] > 5 and col_list[k] > 5:

				return False

	return True
	
	


def check_cages_valid(puzzle, cages):
   pass

def check_cage(puzzle, cage):
	pass

       
def check_valid(puzzle, cages):
   pass

def get_cages():
   pass
