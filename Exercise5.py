import math as m

S=2117519.73

xo=2000

EV=m.sqrt(S)

Xn=1/2*(xo+(S/xo))

n=0

print("S=",S)

print("The exact answer to square root of S is",EV)

print("When we use Hero's method, we have:")

while EV!=Xn :
	Xn=1/2*(Xn+(S/Xn))
	n+=1
	print("X",n,"=",Xn)


print("For the number S, the answer is the same that the exact answer after",n,"compute by the Hero's method.")
