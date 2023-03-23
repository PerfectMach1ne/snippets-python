# Python code to demonstrate working of
# global and non local

# global : This keyword is used to define a variable inside the function to be of a global scope.
#
# nonlocal : This keyword works similar to the global, but rather than global,
# this keyword declares a variable to point to variable of outside enclosing function,
# in case of nested functions.

# initializing a variable globally
a = 10

def read():
    print (a)

def modsmart(): # changing the value of globally defined variable
    global a
    a = 5

def modstupid(): # changing value of only local variable
    a = 5

read()
modstupid()
read()
modsmart()
read()

####################################

# demonstrating non local
# inner loop changing the value of outer a
# prints 10
print ("Value of a using nonlocal is : ", end = "")
def outer():
    a = 5
    def inner():
        nonlocal a
        a = 10
    inner()
    print (a)

outer()

print ("Value of a using nonlocal is : ", end = "")

def router():
    a = 5
    def inner():
        a = 10
    inner()
    print (a)

router()

print ("trying ", end = "")
print ("to ", end = "")
print ("understand end " + "keyword ", end = "")
print ("on")
print ("my")
print ("own")

print ("Well now I get it ", end = "")
print ("LULW")