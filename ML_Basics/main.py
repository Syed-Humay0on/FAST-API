import numpy as np

my_list = [1,2,3,4]
my_list = my_list * 2

# The putput will duplicate the array
print(my_list) # output [1,2,3,4,1,2,3,4]

# a numpy array is superior tp python python list because it's faster
array = np.array([1,2,3,4]) * 2
# array = array * 2
print(array)
print(type(array)) # output ndarray -> n-dimensional array

# 0,1,2 and 3 Dimensional array
arrayx = np.array('A') # output 0

arrayY = np.array(['A', 'B', 'C']) # output 1

arrayZ = np.array([
    ['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']
]) # output 2 because it's a two dimensional array ie Rows and Column

array3 = np.array([
    [['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],
    [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],
    [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', ' ']]
    
]) # output 3 because it's a three dimensional array ie Rows and Column


print(array3.ndim)
