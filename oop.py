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
# The first attribute in the method should be self(which is similar to this  in JavaScript),followed by other properties{parameters in the init method}.
#Self is used to identify the properties of an object
#so name, price and color are properties while name1, price1 and color1 are parameters going to be parsed to the properties
class Phone:
    # A constant attribute that never changes/predefined attribute
    status="Classy"
    # def method is only used when when we are defining the attributes/properties/characteristics of a class.
    def __init__(self,name1,price1,color1):
        
        # self.attribute name=argument(parsed in the __init__ method)
        #User defined attributes
        self.name=name1
        self.price=price1
        self.color=color1
    def termsAndConditions(self,term):
        print(f"This {self.name} costs UGX {self.price} and is non refundable after two years of purchase.\n I hope you {term} the terms and conditions ")

#creating objects of the class Phone
iphone=Phone('iphone12',6500000,'space gray')
samsung=Phone('samsung galaxy s6',700000,'gold')
print(iphone.name)
print(samsung.status)
iphone.termsAndConditions('accept')