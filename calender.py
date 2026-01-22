import calendar

year = int(input("Enter the year: "))
month_name = input("Enter the month name (e.g. March): ").strip().capitalize()

# Convert name to number
month_number = list(calendar.month_name).index(month_name)

# Display calendar
print("\n", calendar.month(year, month_number))
