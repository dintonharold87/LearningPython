""" Create a function "args_1" which takes 3 parameters "num1" and "num2", it also takes a parameter of type *args called "num3".

If the type of parameters "num1" and "num2" is not int, the function should return -1, indicating an invalid value.

The function should multiply the sum of parameters "num1" and "num2" with the sum of all the values in "num3". The parameter "num3" will contain more than one values as its variable type is *args. Thus in mathematical notation, the function needs to perform the following calculation:- 

(num1+num2)*(sum of all values in num3)

After performing the calculation the function should return the answer obtained.

Expected Inputs/Outputs:

args_1(2,4,6,8,9,10,21): The function should return 324 as (2+4)*(6+8+9+10+21) = 324.

args_1(-16,34,81,-22,-91,-64,5,15,20) : the function should return -1008 as (-16+34)*(81+(-22)+(-91)+(-64)+5+15+20) = -1008

args_1(2.1,16,21,84,66): should return -1 as parameter "num1" has an invalud value.

args_1(4,8,10): should return 120 as (4+8)*10 = 120.

args_1(6,"cat",2,4,6,1): should return -1 as parameter "num2" has an invalid value.

args_1(1,2,3,4,5,6,7,8,9): should return 126 as (1+2)*(3+4+5+6+7+8+9)= 126.

Note: As we have been doing in our previous coding exercises, Do not call the function in your main block of code, you just need to provide the definition of the function. """
def args_1(num1,num2,*num3):
    #write your code here
    if (num1 != int(num1)) | (num2 != (num2)):
        return -1
    else:
        sumOfAandB=sum((num1,num2))
        sumOfArgs=sum(num3)
        productOfTheTwo=sumOfAandB * sumOfArgs
        return productOfTheTwo
args_1('dinton',45.4,6,6)