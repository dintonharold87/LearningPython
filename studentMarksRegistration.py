print("=============================================")
print("Welcome to Makerere University Student Portal")
print("=============================================")
# An empty list to store the information entered
marks=[]
allDetails=[]
# Global variables 
name=studentNumber=registrationNumber=test1=test2=courseWork=examMark=''
# Function that prompts a student to enter their details
def register(name,studentNumber,registrationNumber,test1,test2,courseWork):
    name=input("Please enter your name: ")
    studentNumber=input("Please enter your student number:")
    registrationNumber=input("Please enter your registration number:")
    test1=int(input("Please enter your test one marks:"))
    test2=int(input("Please enter your test two marks:"))
    courseWork=int(input("Please enter your course work marks:"))
    
    marks.append(test1)
    marks.append(test2)
    marks.append(courseWork)
    allDetails.append(name)
    allDetails.append(studentNumber)
    allDetails.append(registrationNumber)

    
    
def marksCalculation():
    register(name,studentNumber,registrationNumber,test1,test2,courseWork)
    largest=max(marks)
    largestMark=str(largest)
    marks.remove(largest)
    secondLargest=max(marks)
    secondLargestMark=str(secondLargest)
    averageScore=str((largest+secondLargest)/2)
    scoreOutOfForty=int((((largest+secondLargest)/100)/2)*40)
    scoreOfCourseWork=str(scoreOutOfForty)
    examMark=int(input("Please enter your exam marks:"))
    exam=str(examMark)
    scoreOutOfSixty=((examMark/100)*60)
    scoreOfExam=str(scoreOutOfSixty)
    finalScore=scoreOutOfForty+scoreOutOfSixty
    realScore=str(finalScore)
    # A dictionary to store details for each student
    regDictionary={'Name':name, 'Student Number':studentNumber, 'Registration Number':registrationNumber, 'Test one marks':test1, 'Test two marks':test2, 'Course work marks':courseWork, 'Exam marks':examMark,'First best done':largest,'Second best done':secondLargest,'Average Score of the best two done':averageScore,"Final score out of forty":scoreOutOfForty,'Final score out of Sixty':scoreOutOfSixty,'Final Score for the course unit':finalScore}
    allDetails.append(exam)
    allDetails.append(largestMark)
    allDetails.append(secondLargestMark)
    allDetails.append(averageScore)
    allDetails.append(scoreOfCourseWork)
    allDetails.append(scoreOfExam)
    allDetails.append(realScore)
    
    
    print(allDetails)
def printDetailsToFile():
    f = open('studentResults.txt', 'w')
    for x in allDetails:
        f.write(x)
        f.write('\n')
marksCalculation()
printDetailsToFile()
    
    
    
