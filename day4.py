""" Data structures in Python
1.List- represented by[]
2.Dictionary- represented by {}
3.Tuple - identified with ()
4.Set - identified with () only has unique values. No duplicates/ nothing is repeated.

LIST
this is used to store elements of different datatypes"""
num=["dinton", 23,24,25,3.8]
# This is used to store all the elements in num list in num2 variable 
num2=num[:]
print(num2)
# num3 contains indeces up to 4-1 if num3=num2[n:m] this means num2 contains all elements from index n to index m-1
num3=num2[:4]
print(num3)
# A list is mutable meaning it be changed or we can add anything to it using append method. This method adds one item at a time in a list

# We are adding a list with 3 items into num3 list  
num3.append([20,30,40])
print(num3)

""" we use sort function to sort elements in a list and use sort(reverse=true) to sort in reverse order  """

# A set ommits repeated values in a list 
guests =["dinton", "dinton","Harold","Ainemukama"]
print(set(guests))

#pop function removes the last item  while remove function removes a specific item
guests.remove("Ainemukama")
print(guests)
#del deletes a specific range of items from the list
del num2[2:3]
print(num2)


#TUPLES- are identified using a pair of parentheses
""" A tuple is immutable ie it can't be changed 
it can't be manipulated, it can only be read """
myTuple = (1,4,5,3,88,7,5,455)
myList=[]
myList.append(myTuple,)
myList.append([1,2,3,4])
print(myList)
myList.insert(0,5)
myList.extend([3])
print(myList)



""" A DICTIONARY- this is identified using a pair of braces
syntax-{key:value} """
personX={"name":"Dinton","DOB":1997}
print(personX["name"])

my_box={}
for x in range(7):
    my_box[x]= x*x
print(my_box)
#this checks if the key 1 is in the dictionary called my_box(the answer is a boolen value either true or false)
print(1 in my_box)

#this is to print all value in dictionary
for i in my_box:
    print(my_box[i])
# this is to print all the keys in the dictionary
for i in my_box:
    print(i)
# this is to print the entire dictionary with keys and their values
for i in my_box:
    print(i,my_box[i])
#this is to print values of a dictionary that are even
for i in my_box:
    if my_box[i] % 2 == 0:
        print(i,my_box[i])