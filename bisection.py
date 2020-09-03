#to solve 2nd year CS-04 
#no2 question : x**4 -x -3
#no3 question : x**2 -2*x -2
#substitute those on line 13
print("Finding the nth approximation to the solution of the equation using BISECTION method : \n")
print("Function : f(x)=x**4 -x -3\n")

#equation=equation.subs(x,x)
left_value = float(input("Enter start point of interval : "))
right_value = float(input("Enter end point of interval   : "))
approximation = int(input("Approximation : "))
def function(x):
	return x**2 -2*x -2

print(f"\nLeft value  : {function(left_value)}")
print(f"Right value : {function(right_value)}")

if (function(left_value)*function(right_value) > 0.0):
	print("Function has the same signs.")
	exit()

count=0
print("\nApproximation	|  	a  	 	|	b 	   	|  	Function(mid)")
print("-"*90)


mid=(left_value+right_value)/2.0

while(count+1 <= approximation):
	mid=(left_value+right_value)/2.0

	count=count+1

	print(count,left_value,right_value,function(mid),sep="		|	",end="\n")
	if(function(left_value)*function(mid) < 0.0):
		right_value=mid
	else:
		left_value=mid

print(f"\nf(x)={function(mid)}\n")
print("#"*30)	
