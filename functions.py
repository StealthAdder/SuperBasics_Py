# function is collection of code
# they together work to do a task
# they are called using a function call.
# to create a function we use a keyword called "def"
# --------------------------------------------------

# create a function.
def greetings():
    print("Hello Dude!")

greetings() #calling the function 
# OUTPUT: Hello Dude!

# ---------------------------------------------------------------------------------------
# passing a parameter

 def greetings(name): #here we are telling the function to use the argument "name" while calling the function.
     print("Hello " + name)

 greetings("StealthAdder") #calling the function with a parameter.
# OUTPUT: Hello StealthAdder
# --------------------------------------------------------------------------------------

# passing multiple parameters

def func1(para1, para2):
     print("Going to print the first parameter here " + para1 + " the next over here " + para2)

func1("parameter1", "parameter2")
# OUTPUT: Going to print the first parameter here parameter1 the next over here parameter2
# ----------------------------------------------------------------------------------------------

# useful example printing name of that persons with dob

def greets(name, dob):
    print("Hey " + name + ", You Birthday is " + dob)

greets("StealthAdder", "07Aug")
# OUTPUT:Hey StealthAdder, You Birthday is 07Aug
# ----------------------------------------------------------------------------------------------

# Return function in function
# Using return we return some imformation back from the function
# Nothing after return function inside a function will be execute, it just breaks the code.

def cube(num):
    return num * num * num
    print("Hey")    #this is not going to be printed (code is out of reach)

result = cube(3) #value returned from cube() is saved to variable result.
print(result)   #prints the value
print(str(result))  #can print even in string format.
# OUTPUT: 27
# ------------------------------------------------------------------------------------------------
