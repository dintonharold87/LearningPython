""" Create a function called "final" that takes the following arguments:

arg1, arg2, *arg3, **arg4

The function should return the values of the given variables in the following manner:

(arg1, arg2, [arg3 #arg3 in the form of a list], [#arg4.values() in the form of a list])

Give default values of arg1 and arg2 as "one" and "two" respectively.

Expected Inputs/Outputs:

final() : should return ("one", "two", [], [])

final("val")  : should return ("val", "two", [], [])

final("arg1","arg2",1,2,3,4,5,6,7,8,9,a="first",b="second",c="third")  : should return ('arg1', 'arg2', [1, 2, 3, 4, 5, 6, 7, 8, 9], ['first', 'second', 'third'])

final("arg1","arg2",a="first",b="second",c="third") : should return ('arg1', 'arg2', [], ['first', 'second', 'third'])

Note: As we have been doing in our previous coding exercises, Do not call the function in your main block of code, you just need to provide the definition of the function. """
# 

def final(arg1='one',arg2='two',*arg3,**arg4):
    arg3=list(arg3)
    arg4=list(arg4.values())
    
    return((arg1,arg2,arg3,arg4))
def wordex(word):
    ans=''
    for i in range (0,len(word)+1):
        ans=ans+word[0:i]
        return ans