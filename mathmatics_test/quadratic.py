
import math

# x equals negative b plus or minus the square root of b squared 
# minus 4ac devided by 2a 
# @return: returns two values for x
def quadratic(a, b, c):
    print("This program will find the root of a quadratic equation")
    x1 = (-b + math.sqrt(math.pow(b, 2)-(4*a*c))) /(2*a)
    x2 = (-b - math.sqrt(math.pow(b, 2)-(4*a*c))) /(2*a)
    return x1, x2
    
x1, x2 = quadratic(2, -8, 5)
print(x1)
print(x2)