'''name = input("Enter your name: ")
print(f"Welcome {name} in python series beb")
age = 22
#print(f"are you{age} yrs old right")
print(f"Oh so you are turning{int(age)+1}")
# Taking input from users 
a = input("Enter first number:")
b = input("Enter second number:")
print(f"Sum of {a} and {b} is {int(a) + int(b)}")'''

 #Calculates the marks of student . 
student_name = input("Enter student name: ")
english = int(input("Enter English marks:")) 
python = int( input("Enter python marks :"))
java =  int(input("Enter java marks:"))
total = english + python + java
percentage = (total/300)*100
print("Total Marks =", total)
print("Percentage =", percentage)
