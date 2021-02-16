from solverFuncs import *

def main():
   
   row = 0

   col = 0 

   cages = get_cages()

   puzzle = []

   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])


   checks = 0

   backtracks = 0

   
   while row < 5:

   	#print(puzzle)
   	
   	puzzle[row][col] += 1 #increase current value

   	checks += 1 #inc checks

   	if check_valid(puzzle, cages): #if puzzle and cages are valid

   		if col < 4: # move over a col if less than four

   			col += 1

   		else: #move down a row if at the last column

   			row += 1

   			col = 0

   	if check_valid(puzzle, cages) == False and puzzle[row][col] >= 5: 

   		puzzle[row][col] = 0

   		if col == 0:

   			row -= 1

   			col = 4

   			backtracks += 1

   		else:

   			col -= 1

   			backtracks += 1

  

   print('\n--Solution--\n')

   for i in range(len(puzzle)): #Turns list of numbers into line of strings
   	
   	for j in range(5):

   		puzzle[i][j] = str(puzzle[i][j])

   	print(' '.join(puzzle[i]))
 

   print('\nchecks:', checks, 'backtracks:', backtracks)




if __name__ == '__main__':
   main()
