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



# Convert celsisus to fohrenheit. 
def Celsisus_to_fohrenheit(Celsisu):
    Forenheit = (Celsius *9/5)+32
    return Forenheit
temp_f = Celsisus_to_fohrenheit(25)
print(temp_f)
    