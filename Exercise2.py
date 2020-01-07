list1 = [] 
							# we create a empty list l1
n = int(input("Enter the lenght of your list : ")) 

for i in range(0, n): 
    el = int(input("Enter the number: ")) 			# the users enter the number of the position i
    list1.append(el) 
				  			# We add this number in the list l1
print("The list is:",list1)

# our method is give at index i of list2 the rank of the value of the same index in l1. We begin with the maximum of list1. we put 1 at its indice corresponding in list2. After, we give at the maximum of list1, the value of minimum - 1. We repeat the same until the value of maximun is less or equal to the first minimum - 1 because the first minimun - 1 have a same indice that the first maximum.

list2 = [0]*len(list1) 					# we create a list2 which have a same lenght that list1 and list2[i]=0

i=1							# the rank begin at 1. So we initialize i at 1

r=min(list1)						# before enter to the loop while, we take the value of minimum of list1

while i<=(len(list1)) and list1[list1.index(max(list1))]>(r-1): 	#
	k=list1.count(max(list1))				#We find how many time the maximum of list1 coming in the list1
	while k>1:					#This loop give the same rank of element of the same values of list1
		list2[list1.index(max(list1))]=i
		list1[list1.index(max(list1))]=min(list1)-1	
		k-=1
	list2[list1.index(max(list1))]=i
	list1[list1.index(max(list1))]=min(list1)-1
	i+=1

print("The rank of element of the list is:",list2)

