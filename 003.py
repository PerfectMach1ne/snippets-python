name = input("Enter your name: ") # the return type of input is string

print("HELOOO",name)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ",num3)

num4 = float(input("Enter any number (num4): "))

if (num4 > 21.5):
    print("num4 > 21.5")
elif (num4 < 21.5):
    print("num4 < 21.5")
else:
    print("num4 = 21.5")