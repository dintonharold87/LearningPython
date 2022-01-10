def isOdd(number):
    #write your function here
    number=int(number)
    if number>0:
        if (number%2)==1:
            return True
        else:
            return False
    else:
        return False
    
    
    
    
def sumOdd(start, end):
    start=int(start)
    end=int(end)
    sum=0
    if (start>0)and(end>=start):
        for i in range(start, end+1):
            if isOdd(i)==True:
                sum+=i
        print(sum)
    else:
        return -1
sumOdd(100,100)