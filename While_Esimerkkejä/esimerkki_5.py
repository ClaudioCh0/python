num = int(input("Enter a number # 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number # 1 - 10: "))

print(f"your number is {num}")