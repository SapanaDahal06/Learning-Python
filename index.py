print('hello, world')
# The input() function
my_name = input('Enter your name:')
print('Its good to see you,'+ my_name)
# The len() function
# Checking length of the name
print('The length of your name is:')
print(len(my_name))
#  Working with age
my_age = int(input("What is your age? > "))
print(f"You will be {my_age + 1} in a year.")

# Using type() function
# The type() function
# type(object)

print(type(10))        # int (integer)
print(type(10.5))      # float (decimal number)
print(type("Hello"))   # str (string)
print(type(True))      # bool (boolean)
# Using round() function
#  Syntax :- round(number,ndigits)
print(round(4.5))
print(round(4.4))
print(round(3.14159,1))
print(round(3.14159,2))
#  Using the abs() function
# abs(number)
print(abs(5))      # 5
print(abs(5.5))    # 5.5
print(abs(-3.7))   # 3.7
print(abs(0))      # 0
