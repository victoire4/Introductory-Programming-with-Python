# Question 1
def f(p,n):

	f = 0

	while n != 0:
		f += (n%10)**p 								# The first value of n%10 is a last digit of n. We put the power p in this digit.
		n = n - (n%10) 								# We remove this last digit of n
		n = n //10  
	return f								# We remove the order of this last digit of n. We do the same until n=0 and we find f(p,n)

# Question 2

def g(p):
	l1=[]
	r=p+5
	for i in range(0,r):
		el=(i/(10**(i-1)))
		l1.append(el)
	return l1

#Question 3

def h(p,L):
	h=[]
	for i in range(len(L)):
		el=L[i]<(1/(9**p))
		h.append(el)
	return h

print("For the comment, we take L=g(p)")
#comment : we take L = g(p)
p=int(input("Enter p: "))
h1=[]
c = g(p)
for i in range(len(c)):
	el=c[i]<(1/(9**p))
	h1.append(el)
print("h(p,L)=",h1)

# Conclusion: for i>0, We observe that h1[i] is true for i >= p+2    
      
#Question 4
l2=[]
for i in range(0,20):
	el=i*(9**3)
	l2.append(el)
print("L(i*9**3)=",l2)

#Question 5

#For example
n=123
p=3
L=[0.0,2.0]
print("f(p,n)=",f(p,n))
print("g(p)=",g(p))
print("h(p,L)=",h(p,L))
