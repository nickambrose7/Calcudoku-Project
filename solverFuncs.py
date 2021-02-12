# These are the required functions for this project.
#
# I highly recommend adding functions to check a single
# row, check a single column, and check a single cage.

def check_rows_valid(puzzle):

	for i in range(len(puzzle)):
		
		if check_row(puzzle[i]) == False: #loops through 'i' arguemnet so that every row is checked.
			
			return False #We return false here because the function has done its job if it finds a row is false
		
		else:
			
			func_works = True #We do not return true here becuase we want the funciton to keep running

	return func_works

		 
def check_row(row):
	
	for i in range(len(row)):
		
		for j in range(len(row)):
			
			if row[i] == row[j] and i != j and row[i] != 0 and row[j] != 0 or row[i] > 5 and row[j] > 5: #compares every number in the list and ensures there are no duplicates AT DIFFERENT INDEXES. Excludes 0. returns False if value in row is greater than 5
				
				return False

	return True


def check_columns_valid(puzzle):

	for i in range(len(puzzle)):
		
		if check_column(puzzle, i) == False: #loops through 'i' arguemnet so that every column is checked.
			
			return False #We return false here because the function has done its job if it finds a column is false
		
		else:
			
			func_works = True #We do not return true here becuase we want the funciton to keep running

	return func_works
	



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
	
	for i in range(len(cages)):

		if check_cage(puzzle, cages[i]):

			return True

		else:

			return False
		



def check_cage(puzzle, cage):
	
	s = 0  #keeps track of the sum of the cage

	desired_sum = cage[0] #pulls desired sum out of cage list

	full = True #we will assume the cage is full until proven otherwise

	if s < desired_sum: # This might be redundant but I will keep in in anyways

		for i in range(2, len(cage)): #We start at index 2 in the cage list because that is where the square numbers are listed

			square = cage[i] #We must get the value of the square so that we can convert to row and col

			row = square_to_row(square) # must call this function first becuase we need the row for the next function (square_to_col)

			col = square_to_col(square, row)

			value = puzzle[row][col] #Now that we have converted square # to row and col, we can access the value in the puzzle list

			s += value # we add the value in the puzzle to the total sum of the cage

			if value == 0: # A zero value indicates the cage is not yet full

				full = False

		if full == False and s >= desired_sum: #If we have exceed the desired sum while the cage is not full, the cage is not valid
			
			return False

		elif full == True and s == desired_sum: #If the cage is full and the desired sum has been reached, the cage is valid
			
			return True

		elif full == False and s < desired_sum: #As long as the cage is not full and the sum is less than the desired sum, the cage is still valid

			return True

		elif full == True and s != desired_sum: #Cage is full but not equal to the desired sum.

			return False

			
		

def square_to_row(square):

	if square <= 4:

		row = 0

	elif square > 4 and square <= 9:

		row = 1

	elif square > 9 and square <= 14:

		row = 2

	elif square > 14 and square <= 19:

		row = 3

	else:
		row = 4

	return row


def square_to_col(square, row):

	col = square - (row * 5) #This is the only equation I could come up with to get the column

	return col



		 
def check_valid(puzzle, cages):
	return check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle)

def get_cages():
	pass
