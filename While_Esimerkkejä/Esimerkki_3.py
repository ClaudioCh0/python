age = int(input("Enter your age: "))

while age < 1:
    print("You didn't type your age. \ntry again")
    age = int(input("Enter your age: "))
else:
    print(f"you are {age} years old")