""" 
Bob is a wall Painter and he needs your Help!

You have to write a program that helps bob to calculate how many buckets of paint he needs to buy before going to work. Bob might also have some extra buckets at home. He also knows the area that he can cover with 1 bucket of paint.

1. Write a function called "getBucketCount" with 4 Parameters. The first parameter should be named "width", this parameter represents the width of the wall.

The second parameter should be named "height", which represents the height of the wall.

The third parameter should be named "areaPerBucket", which represents the area that can be covered with a single bucket of paint.

The fourth Parameter should be named "extraBuckets", which represents the number of extra buckets bob has which are stored at his home. 

The function needs to return an int that represents the number of buckets that Bob needs to buy before going to work.

To calculate the bucket count refer to the notes below: -

If one of the parameters width, height, or areaPerBucket is less or equal to 0 or if extraBuckets is less than 0, the function needs to return -1 to indicate an invalid value.

If the parameters are valid, the function needs to calculate the number of buckets bob has to buy and return it.

Expected Inputs/Outputs:

getBucketCount(-3.4, 2.1, 1.5, 2)  = should return -1 as the width parameter is invalid.

getBucketCount(3.4, 2.1, 1.5, 2)   = should return 3, as the wall area would be 7.14, a single bucket can cover an area of 1.5 and Bob has 2 extra buckets at home.

getBucketCount(2.75, 3.25, 2.5, 1)= should return 3 since the wall area is 8.9375 , a single bucket can cover an area of 2.5 and Bob has 1 extra bucket at home.

2. Bob does not like to enter 0 for the "extraBuckets" parameter so he needs another function.

Write another function called "countBuckets" with 3 parameters namely width, height, and areaPerBucket.

This function needs to return a value of type int that represents the number of buckets bob needs to buy before going to work. To calculate the bucket count refer to the notes below.

If any parameter width, height, or areaPerBucket is less than or equal to 0, the function needs to return -1 to indicate an invalid value.

If all the parameters are valid, the function needs to calculate the no. of buckets needed and return it.

Expected Inputs/Outputs:

countBuckets(-3.4, 2.1, 1.5)   = should return -1 as the width parameter is invalid.

countBuckets(3.4, 2.1, 1.5)   = should return 5 as the wall area is 7.14 and a single bucket can cover an area of 1.5.

countBuckets(7.25, 4.3, 2.35) = should return 14 since the wall area is 31.175, and a single bucket can cover an area of 2.35.

3. In some cases, Bob does not know the width and height of the wall, but he knows the area of a wall! He needs to write another function.

Write another method called "finalCount" which takes only 2 parameters namely, area and areaPerBucket.

The function needs to return a value of type int that represents the number of buckets that Bob needs to buy before going to work. To calculate the bucket count refer to the notes below.

If any of the parameter area or areaPerBucket is less or equal to 0, the function needs to return -1, indicating an invalid value.

If all the parameters are valid, the method needs to calculate the number of buckets needed and return it.

Expected Inputs/Outputs:

finalCount(3.4, 1.5)   = should return 3 as the area of the wall is 3.4 and a single bucket can cover an area of 1.5.

finalCount(6.26, 2.2) = should return 3 as the area of the wall is 6.26 and a single bucket can cover an area of 2.2.

finalCount(3.26, 0.75) = should return 5 as the area of the wall is 3.26 and a single bucket can cover an area of 0.75.

Do your best to help Bob!

Note: You have to create three functions in this exercise.

Note: All functions have to return a number of type int.

Note: You can round a number using the inbuilt round() method, to know more about round() click here!

Note: Do not call the function anywhere in your main block of code, you just need to provide the definition of the fucntion.

 """

def getBucketCount(width,height,areaPerBucket,extraBuckets):
    if (width<=0)|(height<=0)|(areaPerBucket<=0)|(extraBuckets<=0):
        print('wrong value')
    else:
        wallArea=width*height
        bucketsToBuy=round(wallArea/areaPerBucket)-extraBuckets
        print(bucketsToBuy)
# getBucketCount(2.75, 3.25, 2.5, 1)
def countBuckets(width,height,areaPerBucket):
    if (width<=0)|(height<=0)|(areaPerBucket<=0):
        print('wrong value')
    else:
        wallArea=width*height
        bucketsToBuy=round(wallArea/areaPerBucket)
        print(bucketsToBuy)
countBuckets(3.4,2.1, 1.5)
countBuckets(7.25,4.3, 2.35)
def finalCount(area,areaPerBucket):
    if (area<=0)|(areaPerBucket<=0):
        print('wrong value')
    else:
        
        bucketsToBuy=round(area/areaPerBucket)
        print(bucketsToBuy)
# finalCount(3.26, 0.75)