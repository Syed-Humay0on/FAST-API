import numpy as np

my_list = [1,2,3,4]
my_list = my_list * 2

# The putput will duplicate the array
print(my_list) # output [1,2,3,4,1,2,3,4]

# a numpy array is superior tp python python list because it's faster
array = np.array([1,2,3,4])
array = array * 2
print(array)
print(type(array)) # output ndarray -> n-dimensional array

