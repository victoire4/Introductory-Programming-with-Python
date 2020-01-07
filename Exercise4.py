l1 = [] 						# we create a empty list l1

n = int(input("Enter the lenght of your list : ")) 

for i in range(0, n): 				# for i, the index of the element in l1
    el = int(input("Enter the number")) 		# the users enter the number of the position i
    l1.append(el)   				# We add this number in the list l1. So we form the list l1

print("The list is:",l1) 				# display l1

from functools import reduce # We have two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.

def l2(l1):  					# We define our function 
    l2 = []  					# we create a empty list l2
    for i in range(0, n):	
        l2.append(reduce(lambda x, y: x*y, l1[:i] + l1[i+1:])) #l1[:i] + l1[i+1:] give the list of elements before and after the element of index i  
 						# the function "reduce" associated at "lambda" give the product of all element of the list l1[:i] + l1[i+1:]
			
    return l2

print("The product of all integers of the list except list[i] is:",l2(l1))

