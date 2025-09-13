# def SumNbr(a,b,c):
#     result = a+b+c
#     print("The sum is:",result)
# SumNbr(a=20 , b = 30,c = 10)  

# Return Statement
def addnum(a, b):
    return a + b
SumNbr = addnum(10,20)
print(SumNbr)

# Another options
def sumnbr(a,b):
    return a + b
result = sumnbr(10,15)
print(result)



# Convert celsius to fahrenheit - with retun
def Celsius_to_fahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit

temp_f1 = Celsius_to_fahrenheit(25)
print(temp_f1)
print("with return:",type(temp_f1))


# Convert celsius to fahrenheit-without return 
def Celsius_to_fahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    print( Fahrenheit)

temp_f2 = Celsius_to_fahrenheit(25)
print("Without return:",type(temp_f2))