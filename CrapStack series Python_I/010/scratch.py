# in : This keyword is used to check if a container contains a value.
# This keyword is also used to loop through the container.

if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else: print("s is not part of geeksforgeeks")

if '2' and 'u' in '1345678902098765431':
    print("2 is yes")
else: print("2 is nononoo")

for i in 'geeksforgeeks':
    print(i, end = " ")

print("\r")

# is : This keyword is used to test object identity, i.e
# to check if both the objects take same memory location or not.

print(' ' is ' ') # indian dudes wrote me a code that shits out a warning (try running this)

# using is to check object identity
# string is immutable( cannot be changed once alloted)
# hence occupy same memory location

print({} is {})

# using is to check object identity
# dictionary is mutable( can be changed once alloted)
# hence occupy different memory location