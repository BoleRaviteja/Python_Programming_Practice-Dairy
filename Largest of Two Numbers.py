first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print(f"Largest: {first_number}")
elif second_number > first_number:
    print(f"Largest: {second_number}")
else:
    print("Both numbers are equal.")