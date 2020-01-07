n=int(input ("Enter your integer's number that you want to know the fibonacci sequence: "))	# The user enter his number for the compute of its fibonacci sequence 

def fibonacci(n):									# We defined a function fibonacci(n)
										
    if n==0: 									# First Fibonacci number is 0 
        return 0
    
    elif n==1: 									# Second Fibonacci number is 1 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 						# all integer's number greater than 1 
r=0

while r<n :
	print("F",r,"=",fibonacci(r))
	r+=1
print("F",n,"=",fibonacci(n))
