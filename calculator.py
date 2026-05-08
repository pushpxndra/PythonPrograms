a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("choose operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input("enter choice (1/2/3/4): ")

if choice == '1':
    print("result =", a + b)

elif choice == '2':
    print("result =", a - b)

elif choice == '3':
    print("result =", a * b)

elif choice == '4':
    if b != 0:
        print("result =", a / b)
    else:
        print("division by zero not possible")

else:
    print("invalid choice")

