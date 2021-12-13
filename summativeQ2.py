# This is a funtion for rounding off grades
# Which takes the current grades as the input  
def grader (grades):
    # A new list is created to store the newly calculated grades 
    newlist = []
    # A this loop checks to see if grade is equal to or
    # less than 38 and adds it to the newlist.
    for i in range (len(grades)):
        if grades[i] < 39:
            newlist.append(grades[i])
             # Else it does a calculation of the next multiple of 5
             # by finding the previous multiple of 5 using the modulo
             # operator and subtracting, the remainder from the value and 
             # then adding a 5 .
        else:
            nextval =(grades[i] - (grades[i]%5))+5
            diff =  nextval - grades[i]   
            # next we check to see if the difference is <3 and add the differnce
            # to the value or leave the value as is if the differen is <=3.
            if diff > 3 :
                newlist.append(grades[i])
            else:
                val = grades[i] + diff 
                newlist.append(val)
    result= "Old score" + str(grades) + "\n" +"New score" +str(newlist)
    return result  
    

print(grader([73,67,38,33]))