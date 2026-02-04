try:
    a = int(input("Enter the number: "))
    print(f"Multiplication table of {a} is:")
    
    for i in range(1, 11):
        print(f"{a} X {i} = {a * i}")

except ValueError:
    print("Please enter a valid number!")

except Exception as e:
    print(f"Sorry, an unexpected error occurred: {e}")

finally:
    print("Some line of code")
    print("End of the code.")
