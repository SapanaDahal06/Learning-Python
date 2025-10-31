def my_function ():
    print("Welcome to the python course")
    
#Use function using (use function)
#my_function()
#def addnumber(a,b):
    #result = a + b
    #print("Sum of the :",result)
    
#addnumber(10,15)
#default argument
#def average(a=3, b=4):
#    print("The average is", (a + b) / 2)

# Function calls
#average()        # uses default values: a=3, b=4
#average(b=10)    # overrides b

#Required argument
'''def gretting(name):
    print("Hello", name,"!")
gretting("Sapana")'''


'''def intro(course_name ,export_name):
    print("Welcome to ",course_name, "course by",export_name)
intro("Python","Sapana")'''
    
    
#Default Argument

def gretting(name="World"):
    print("Hello" ,name , "!")
gretting()
gretting("Adellise")

