def allFactors(number):
    
    #write your function here
    allFactorList = []
    number=int(number)
    if number>1:
        for i in range(1,number+1):
            if(number%i)==0:
                allFactorList.append(i)
                continue
        else:
                
            return(allFactorList)
    else:
        return -1
# allFactors(300)  

def primeFactors(number):
    #write your function here
    factorlist=allFactors(number)
    
    primeList=[]
    for i in factorlist:
        if i==1:continue
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
        if flag==True:
            primeList.append(i)
    return primeList
    
primeFactors(300)
    