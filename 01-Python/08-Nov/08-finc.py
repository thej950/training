x = 10  # global variable

def modify():
    global x
    x = 20  # modify global variable

modify()
print("Updated x:", x)
