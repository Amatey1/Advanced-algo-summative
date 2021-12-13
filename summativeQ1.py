# Defining the function for performing the summation
def summer(n):

#intializing the total variable 
 total = 0

# loop through each value and add the value to the variable "total".
 for x in range(n+1):
     total=total+x
 print(total)

summer(10)
summer(10000)
summer(1000000)
summer(100000000)
