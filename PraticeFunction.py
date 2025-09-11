# WAF to print the length of the list. 
fruits = ["Avocado","Blueberry","Coconut","Dragon fruit","Pineapple","Grapes","kiwi"]
cities = ["Kathamandu","Biratnagar","Gaighat","Dharan","Butwal","Pokhara"]

def Print_len(lst):
    print(len(lst))

# Pass the list itself, not its length
Print_len(fruits)
Print_len(cities)
# WAF print element of the list in a single line(list in the parameter)
def print_elements(lst):
    for item in lst:
        print(item, end=' ')  # print elements in the same line separated by space
    print()  # for newline at the end

# Example usage:
fruits = ["Avocado","Blueberry","Coconut","Dragon fruit","Pineapple","Grapes","Kiwi"]
print_elements(fruits)
#  write a program and find the factoe of the n. (n is parameter)
def Cal_fun(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

# Call the function
Cal_fun(5)

# WAF convert USD into Rupees.
def usd_to_npr(usd):
    exchange_rate = 133 
    npr = usd * exchange_rate
    print(f"{usd} USD = {npr} NPR")

# Example usage
usd_to_npr(10)


