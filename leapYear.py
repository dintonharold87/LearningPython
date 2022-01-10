def isLeapYear(year):
    if ((year >= 1) and (year <= 9999)):
        if(year % 4) ==0:
            if(year % 100) == 0:
                if(year%400)==0:
                    print('leap year')
                else:
                    print('not leap year')
            else:
                print('leap year')
        else:
            print('not leap year')

    else:
        print('not in valid year range')
isLeapYear(-1600)