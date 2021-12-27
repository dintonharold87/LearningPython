""" object oriented programming in Python
An object is an instance of a class
A class is a collection of objects
A class is identified with the phrase 'IS A' eg A car IS A vehicle
meaning Vehicle is a class and Car is an object that
We create a class using the keyword Class followed by the class name.
The class name should start with Uppercase letter"""
class Car:
    pass
#instaces of class car/objects
nissan=Car()
ford=Car()
subaru=Car()
toyota=Car()
#Defining a class with properties, attributes or characteristics of objects, we use init method def __init__()
# The first attribute in the method should be self(which is similar to self in JavaScript),followed by other properties{parameters in the init method}.
#Self is used to identify the properties of an object
#so name, price and color are properties while name1, price1 and color1 are parameters going to be parsed to the properties
class Phone:
    def __init__(self,name1,price1,color1):
        self.name=name1
        self.price=price1
        self.color=color1
#creating objects of the class Phone
iphone=Phone('iphone12',6500000,'space gray')
samsung=Phone('samsung galaxy s6',700000,'gold')
print(iphone.name)