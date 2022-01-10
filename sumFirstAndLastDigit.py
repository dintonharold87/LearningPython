def sumFirstAndLastDigit(number):
    number =int(number)
    if number>0:
        number=str(number)
        firstDigit=int(number[0:1])
        lastDigit=int(number[-1])
        sum=firstDigit+lastDigit
        print(sum)
        
    else:
        return -1
sumFirstAndLastDigit(1364647474747474747474744737474744)