""" numbers= [1,2,3,4,5,5,6]
sum=0
for i in numbers:
    if i%2 ==0:
        # print(i)
        sum+= i
print(sum) """
numbers=[23,2,3,45,6,7,98,7,4,4,1,1,2,0]
sum=0
index=0
total=0
while index< len(numbers):
    num=numbers[index]
    if num>0:
        total+=numbers[index]
    index+=1
print(total) 
