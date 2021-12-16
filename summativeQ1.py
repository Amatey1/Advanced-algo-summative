# Defining the function for performing the summation
def summer(n):

#intializing the total variable 
 total = 0

# this loop goes through each value between 0 and the "n" adding the value of the index it is currently on to the "total" variable.
#The code stops once it reaches n and returns the sum.
 for x in range(n+1):
     total=total+x
 return total

print (summer(10))
print (summer(10000))
print (summer(1000000))
print (summer(100000000))
