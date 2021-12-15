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
