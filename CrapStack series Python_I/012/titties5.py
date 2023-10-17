i = 1
while i <= 13:
    print(i * '*')
    i += 1

i = 13
while i > 0:
    print(i * '*')
    i -= 1

names = ["Jeff", "Jeffuel", "Jeffery", "Jef", "Jhuss"]
print(names)
print(names[0])
print(names[4] + " Chillen")
print(names[4] == names[-1])
print(names[3] == names[-2])
print(names[0] == names[-5])
names[0] = "Jeffeff"
print(names[0])

print(names[0:3])
print(names[3:5])
print(names[3:4])
print(names[4:5])
print(names[0:(2+1)])

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(0, 0)
print(numbers)
numbers.pop(-1)
print(numbers)
numbers.remove(3)
print(numbers)

print(11 in numbers)
print(len(numbers))

for i in numbers:
    print(i)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
numbers.pop(-6)
print(numbers)
numbers.insert(0, 1)
print(numbers)
numbers.pop(-5)
print(numbers)