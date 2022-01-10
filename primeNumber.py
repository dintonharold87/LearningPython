def FindPrime(number):
    number=int(number)
    if number>1 or number<1:
        for i in range(2,number):
            if(number%i) == 0:
                print('Not Prime')
                break  
        else:
            print('Prime')
                
    else:
        print('not in range')
    
FindPrime(-13) 
