# Super_basics
# using and, or, if else, elif statements all in one program.
# Output is knowing: if the devices are on, off, both running or one of them is running.

# Playing with the boolean input's

Fan = False
Bulb = False

if Fan == True and Bulb == True:
    print("Fan & Bulb are ON")
    print("Both are consuming Energy to work")
elif Fan == True or Bulb == True:
    print("Energy is being consumed because")
    if Fan == True:
        print("Fan is ON")
    else:
        print("Bulb is ON")
else:
    print("Both the Devices are OFF")
