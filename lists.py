# lists functions

names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

# extend function.
# allow a list to append onto a list
names.extend(no)
print(names)

# OUTPUT: ['rob', 'bob', 'shaw', 'newton', 'jack', 'bill', 5, 16, 8, 12, 4, 32, 1]
# ----------------------------------------------------------------------------------------
# add individual element onto a list
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names.append("noah")
print(names)
# OUTPUT:['rob', 'bob', 'shaw', 'newton', 'jack', 'bill', 'noah']
# --------------------------------------------------------------------------------------

# insert at a index point
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names.insert(2,"shaun")
print(names)
# OUTPUT:['rob', 'bob', 'shaun', 'shaw', 'newton', 'jack', 'bill']
# -------------------------------------------------------------------------------------------

# remove elements
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names.remove("jack")
print(names)
# OUTPUT:['rob', 'bob', 'shaw', 'newton', 'bill']

# remove all the elements in the list
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names.clear()
print(names)
# OUTPUT: []

# pop element
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names.pop() #removes the last element.
print(names)
# OUTPUT:['rob', 'bob', 'shaw', 'newton', 'jack']
# ---------------------------------------------------------------------------------------------

# index function
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

print(names.index("bob"))
# returns the index value.
# OUTPUT:1
# ---------------------------------------------------------------------------------------------
# count function to check if duplicate element is present'
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names = ["rob", "bob", "bob", "shaw", "newton", "jack", "bill"]
print(names.count("bob")) #counts how many times bob as repeated in the list
# OUTPUT:2
# ----------------------------------------------------------------------------------------------

# sort in alphabetical order

names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

names.sort()
print(names)

no.sort()
print(no)
# OUTPUT: ['bill', 'bob', 'jack', 'newton', 'rob', 'shaw']
# OUTPUT: [1, 4, 5, 8, 12, 16, 32]
# ------------------------------------------------------------------------------------------------
# copy function
names = ["rob", "bob", "shaw", "newton", "jack", "bill"]
no = [5, 16, 8, 12, 4, 32, 1]

newnames = names.copy()
print(newnames)

newno = no.copy()
print(newno)
# OUTPUT: ['rob', 'bob', 'shaw', 'newton', 'jack', 'bill']
# [5, 16, 8, 12, 4, 32, 1]
# ------------------------------------------------------------------------------------------------------------