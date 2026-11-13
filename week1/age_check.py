name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
age = current_year - birth_year

if age < 13:
    category = "Child"
elif age <= 17:
    category = "Teenager"
elif age <= 64:
    category = "Adult"
else:
    category = "Senior"

print(f"Hello, {name}! You are approximately {age} years old. ({category})")