import sys

# ========== Functions ==========

def Initialize():   # This function creates an empty list
    Name = []
    return Name

def SetParameter(name, arg):    # If there are arguments, this function extends the list whith the arguments
    name.extend(arg)
    return name

def Print(name):
    if len(name) == 1:    # If there are no arguments, the length of "Name" list will be 1 (the filename)
        print("Hello World!")
    else: print("Hello" + " " + name[1] + "!")

# ========== Main ==========

Initialize()
Print(SetParameter(Initialize(), sys.argv))
'''
The Initialize function gives its parameter to the SetParameter,
then the SetParameter gives its parameter to the Print function
'''