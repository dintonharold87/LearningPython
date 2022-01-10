""" Write a function named getEvenDigitSum
The method should return  the sum of all even digits  """
def getEvenDigitSum(number):
    #write your code here
    number=int(number)
    if number>=0:
        number=str(number)
        sum=0
        for i in number:
            i=int(i)
            if (i%2)==0:
                sum+=i
        return sum
        
    else:
        return -1
getEvenDigitSum(908)