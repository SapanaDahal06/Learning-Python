#Concate Operation
'''
countries1 = ("Nepal","America","australia","Canda")
countries2 = ("itali","Portugal","Chinna","Dubai")
southEast = countries1 + countries2
print(southEast)

my_tuple = (1, 2, 4, 5, 4, 6,4, 7, 4)
#res = my_tuple.count(4)
#res = my_tuple.index(7)
res = my_tuple.index(2,4,6)
print('Count of 7 is:', res)
#Conver list into tuple. 
tuple1 = (1,2,3,4,)
print(type(tuple1))
print(tuple1)

list1 = [1,2,3,4]
new_tuple = tuple(list1)
print(new_tuple)
#Repetations
tuple3 = ("Hello",)*3
print(tuple3)
#Checking Item.
num = (10,20,30,40)
print(20 in num)'''

'''Using loop in Tuple 
fruits = ('Apple','Banana','Cherry')
for i in fruits:
    print(i)
#Using while lopp in Tuple 
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1   ''' 
    
'''#Method 
color = ('Red','Blue','green','White','Black','green','Pink')
#Count 
print(color.count('green'))   
#index
print(color.index('White'))'''

'''#Tuple Function
num = (1,2,3,4,5)
#len
print(len(num))
#sum
print(sum(num))
#Min
print(min(num))
#Max
print(max(num))
#Sort
print(sorted(num))#Tuple is list now 
'''

'''#Packing tuple is the process of puting multiple value into a single tuple . 
a = 'Adellise'
b = 22
c = 'Data Analyst'
pack_tuple = a,b,c
print(pack_tuple)
#Another example.
fruits = ('Apple', 'Banana', 'Cherry')
print(fruits)


#Unpacking Unpacking means taking out the values from a tuple and assigning them to individual variables.
name , age , profession = pack_tuple
print('Name is ',name)
print(age)
print(profession)

#Another example.
fruits = ('Apple', 'Banana', 'Cherry')
a, b, c = fruits
print(a)
print(b)
print(c)'''


#Modifying tuple  means once you create a tuple you can not add , remove , or change items. 
tuple_num = (10,20,30,40)
#tuple_num[0] = 100 #Error
# how  to modify tuple . 
list_num = list(tuple_num)
list_num[0] = 150
list_num[3] = 200
list_num.append(300)#Using append method.
list_num.remove(30)
print(list_num)



