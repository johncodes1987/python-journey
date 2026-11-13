me = {
    "name": "John",
    "age": 39,
    "city": "Lubbock"
}

print(f"My name is {me['name']}.")
print(f"I am {me['age']} years old.")
print(f"I live in {me['city']}.")

me["hobby"] = "coding"

print("\nDictionary Items:")
for key, value in me.items():
    print(f"{key}: {value}")