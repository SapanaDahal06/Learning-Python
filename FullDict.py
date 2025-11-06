
Syntax = my_dict = {"Key1":"value1","Key2":"value2","Key3":"value3"}
Student = {
    1:"Class-VII",
    "name": "Adellise",
    "age": 20
  #print(Student)
    
}
 #Create dictionary using curly braket{}
cohort = {
  "Course":  "Python",
  "Instructor": "Adellise",
  "Level" : "Beginner",
  
  }
print(cohort)
#Using Dict() Constructor
person = dict(Name="Adellise",age = "22",address = "Udayapur")
print(person)


#Using a List of Tuples.
Student = ([("name","Adellise"),("age",22),("Level","Bachelor Running")])
print(Student)

# Acess Dictionary Value.
Student = {
    "name": "Adellise",
    "Grade":"A",
    "City":"Gaighat",
    "Year":"Last year of bachelor"
}
print(Student)
print(type(Student))
print(Student['name'])
print(Student["Grade"])

#Key of the Dictionary.
Student = {
    "name": "Adellise",
    "Grade":"A",
    "City":"Gaighat",
    "Year":"Last year of bachelor"
}
#Keys 
print(Student.keys())
#Values
print(Student.values())
#Item()
print(Student.items())
#Get()
print(Student.get("City"))

#For More Knowledge
#print(Student['Email'])# Its print Error. 
print(Student.get('Email'))# Its print None . Email is not in the dictionary.

#Add & Modify items in the dictionary.
#Add item -assign items
Student['Email']= 'Adellise123@d.com'
Student['age'] = 22
print(Student)

#Modifying items 
Student ['Grade'] = 'A+'
Student['Year'] = '4th '
print(Student)
#Del to item from dict
del Student['Grade']
print(Student)
#POP Method
var1 = Student.pop('City')
print(var1)
print(Student)

#Dictionary Iterations.
Student = {
    "name": "Adellise",
    "Grade":"A",
    "City":"Gaighat",
    "Year":"Last year of bachelor"
}
#Loop through keys.
#for x in Student:
  #print(x)
  
# Loop Through for value
for value in Student:
  print(Student[value])
#LOOp through values Using values()
for value in Student.values():
  print(value)  
# LOOp through both keys and values.
for keys, value in Student.items():
  print(keys,value)
  
  
#Nested Dictionary
Main_Students = {
    "Student1": {
        "name": "Sapana",
        "Grade": "A",
        "City": "Gaighat",
        "Year": "Last year of bachelor"
    },
    "Student2": {
        "name": "Adellise",
        "Grade": "A",
        "City": "Gaighat",
        "Year": "Last year of bachelor"
    }
}

print(Main_Students["Student1"]["name"])
#Dictionary Comprehension.

#Syntax:-
# {key_expression: value_expression for item in iterable if condition}

my_dict = {x:x*x for x in range(1,6)}
print(my_dict)

names = ["Sapana", "Asha", "Bipin"]
lengths = {name: len(name) for name in names}
print(lengths)

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)
