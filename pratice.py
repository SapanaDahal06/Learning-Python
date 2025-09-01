# name = input("Enter your name:")
# print("Good Morning,"+ name)
# print("Good Afternoon,"+name)
# print("Good Evening,"+name)

# Create a python program capable of greeting you with a Good morning , Good Afternoone , Good night. Your program should use time module to get the current time. 
import time
current_time = time.localtime().tm_hour
name = input("Enter your name:")
if current_time < 12:
    print("Good Morning!" + name)
elif current_time < 18:
    print("Good afternoon!"+name)
else:
    print("Good night!"+name)

