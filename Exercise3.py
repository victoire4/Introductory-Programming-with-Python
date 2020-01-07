# We want to calculate "pi" of the Madhava series. pi = A*B; A=square root of 12 and B= sum(((-1)/3)**k + (1/(2*k+1)))

import math as m 				# We import math for do the square root

A=m.sqrt(12)

B=1 					# The first values of the sum B for k=0

k=1 					# So, we begin with k=1

for k in range(1,20): 			# range(1,20) because we calculates for the first 20 terms
	B+=(((-1)/3)**k * (1/(2*k+1)))	#at B, we add the sum obtain of the Madhava series

print("From the Madhava series, pi=",A*B)	# We display the result of "pi"
