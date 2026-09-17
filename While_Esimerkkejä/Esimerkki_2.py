name = input("Enter your name: ")

while name == "":
    print("You did not enter your name. \ntry again.")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}")