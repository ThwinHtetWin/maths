from sympy import *

#to solve 2nd year CS-04 

print("Finding the nth approximation to the solution of the equation using BISECTION method : \n")
print("Function : f(x)=x^4 -x -3\n")

left_value = float(input("Enter start point of interval : "))
right_value = float(input("Enter end point of interval   : "))

def function(x):
	return x**4-x-3

print(f"\nLeft value  : {function(left_value)}")
print(f"Right value : {function(right_value)}")

if (function(left_value)*function(right_value) > 0.0):
	print("Function has the same signs.")
	exit()

count=0
print("\nApproximation	|  	a  	 	|	b 	   	|  	Function(mid)")
print("-"*90)


mid=(left_value+right_value)/2.0

while(count+1 <= 5):
	mid=(left_value+right_value)/2.0

	count=count+1

	print(count,left_value,right_value,function(mid),sep="		|	",end="\n")
	if(function(left_value)*function(mid) < 0.0):
		right_value=mid
	else:
		left_value=mid

print(f"\nRoot : {mid}\nf(x)={function(mid)}\n")
print("#"*30)	