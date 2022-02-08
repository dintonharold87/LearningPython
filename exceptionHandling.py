""" Create a function called "sum_all" which takes a single parameter called "values" of type "list".

The main work of the function is to iterate all over the list(values parameter) and to return the sum of all numbers. 

Now, if a value inside the list given by the user is not of type "int" or "float" the function should return "Invalid value".

Expected Inputs/Outputs:

sum_all([1,2,3,4,5,6,7,8,9])                      =   Should return 45 as the sum of all the numbers in the list Is 45.

sum_all([1,"cat",21.64])                             =   Should return "Invalid value" as an output as "cat" is not an int or a float.

sum_all([4,15,21,16.345,78.51,-66])         = Should return 68.855 (round to 3 decimal places) as the sum of all the numbers in the list is 68.855

sum_all([[1,2]])                                          = Should return "Invalid value" as the given list contains another list of elements.

sum_all([-16,-21,-65,-2,{"a":"b"}])        = should return "Invalid value" as the list contains a dictionary data type.

Note: This function should not print anything it should return it!

Note: Solve the question only using the concepts of Exceptions and Error handling, DO NOT use if-else statements.

Note: Remember, don't run the function, simply provide the definition.

Note: take care of the casing in the "Invalid value" word. """

def sum_all(values):
    
        
    sum=0
    try:
        for i in values:
            sum+=i
    except TypeError:
        print("Invalid value")
            
    else:
            
        print(round(sum,3))
sum_all([4,15,21,16.345,78.51,-66])