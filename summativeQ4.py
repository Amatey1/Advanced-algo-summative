# this algorithm takes a number and adds all the indivual values within the string to form a sum 
# the number of times the number should be concatenated is represented by K
# the goal is to add the concatnated values till you have just 1 digit .

def megadigit(n,k):

    p = k*n
    #This multiplies the number of string by the number of times k create a duplication k number of times    
    while len(p) >= 2 :       
        # since super digit aims to get to the point where the sum of the concatnated values(P) is 1 digit 
        #  we use a while loop to keep checking the number of digits in P.
        sum = 0
        # the for loop , loops through all the values of P and converts them to integer as they are added up.
        for g in range(len(p)):
            sum = sum + int(p[g])
        p = str(sum)
    return p


print(megadigit("23",2))
print (megadigit("54",3))
print (megadigit("6234",4))




