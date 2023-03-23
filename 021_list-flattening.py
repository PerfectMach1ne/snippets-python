# exec(open('D:/Programming/Python/python-snippets/021_list-flattening.py').read())
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists[1])

# Naive/'brute force' list flattening
flat_list = list()

for sub_list in list_of_lists:
    flat_list += sub_list

print(flat_list)

# List comprehension for list flattening
# any list comprehension can actually be expressed as a for-loop (though the
# reverse isn’t necessarily true)
# Advantages:
#  1. You don’t need to instantiate a new empty list
#  2. You can write it over one line
#
# [x ** 2 for x in [1, 2, 3, 4, 5]]
# an expression FOR an item IN an iterable list
#
flat_list = [item for sublist in list_of_lists for item in sublist]
# my smoothbrained "brain translation" attempt
# "the number as item FOR its sublist IN list_of_lists, but OH, i just realized
# that the item is a senseless word u n t i l we reach the `FOR item IN sublist
# ` line of code, which uses the entire thing before it as the expression, item
# IN a sublist as the item IN an iterable list (that is the sublist). i get it
# now. it makes sense to me now."

print(flat_list)

# How to make it NOT work:
# flat_list = [(item for sublist in list_of_lists) for item in sublist]
# flat_list = [item for sublist in list_of_lists for item2 in sublist]
# flat_list = [item for sublist in list_of_lists]
# flat_list = [item for sublist in list_of_lists for item ** 2 in sublist]
#
# Going to W3Schools for extra lore because they didn't bother to explain list comprehension properly
# in the 'mid-iocre' tutorial
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = list()

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)
newlist = list()
print(newlist)
newlist = [x for x in fruits if 'a' in x]
print(newlist)
# newlist = [expression for item in iterable if condition == True]
# 
# Itertools chain()
from itertools import chain
# chain() returns itertools.chain object
print(type(chain(*list_of_lists)))

flat_list = list(chain(*list_of_lists))
# the * operator is variable unpacking
s = [*'abcdefg']
print(s)
print(*list_of_lists)  # Prints out 3 unconnected lists
print(flat_list)  # Prints out the chained 3 lists as 1 list thanks to chain()

# Flattening multi-level lists of lists
list_of_lists = [1, [2, 3], [4, [5, 6]], [7, 8], 9]
# this pleases my set theory braincells.
# when the set L is equal to {1,{2,3},{4,{5,6}},{7,8},9} by the axiom of extensionality-
# WHEN THE IMPOSTER IS S-
print(list_of_lists)
print(*list_of_lists)
first, *unused, last = [1, 2, 3, 5, 7]
print(str(first) + ' and ' + str(unused) + ' and ' + str(last))
def flatten_list(list_of_lists: list, flat_list=[]):  # doesnt mtter if you do fl: list = [] or fl=[], it'll still be fucky-wucky
    if not list_of_lists:
        return flat_list
    else:
        for item in list_of_lists:
            if type(item) == list:
                flatten_list(item, flat_list)
            else:
                flat_list.append(item)

    return flat_list

flat_list = flatten_list(list_of_lists)
print(flat_list)
enmpty = list()
print("enmpty" + str(flatten_list(enmpty))) # WHAT THE FUCK?
# OH, I GET IT. THE IMPLEMENTATION IS CURSED 2 BEGIN WITH
print("enmpty" + str(flatten_list(enmpty, [])))

def flatten_listv2(list_of_lists: list, flat_list: list = []):
#    unpack = list()
#    for item in *list_of_lists,:
#        unpack.append(item)
#    print(unpack)
    # Okay, so the , is there because of weird PEP specification thing.
    # It's about making sure a tuple is coupled with this unpacked thing... I think?
    # like, try *ass = 'donky', it will break. but *ass, = "donky" will work just fine.
    # similarly, *numbers, = range(5) will give you a neat list of 5 first natural numbers
    # And, ** is for unpacking dictionaries specifically. I've used it before anyway
    # https://geekflare.com/python-unpacking-operators/
    if list_of_lists == []:
        return flat_list
    else:
        unpack = list()
        for item in *list_of_lists,:
            unpack.append(item)
        for item in unpack:
            if type(item) == list:
                flatten_list(item, unpack)
            else:
                flat_list.append(item)

    return flat_list

print(flatten_listv2(list_of_lists))
# Okay, my poorly thought out version  is a little broken LMAO what is that
# [1, 9, 2, 3, 4, 5, 6, 7, 8] :Skull:
