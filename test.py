import sys
def calculate():
    operation = input("Choose operation: addition (a), subtraction (s), multiplication (m), division (d), or terminate (t)")
    if operation == "a":
        adda = input("First number?")
        addb = input("Second number?")
        result = float(adda)+float(addb)
        print (result)
    elif operation == "s":
        adda = input("First number?")
        addb = input("Second number?")
        result = float(adda)-float(addb)
        print (result)
    elif operation == "m":
        adda = input("First number?")
        addb = input("Second number?")
        result = float(adda)*float(addb)
        print (result)
    elif operation == "d":
        adda = input("First number?")
        addb = input("Second number?")
        result = float(adda)/float(addb)
        print (result)
    elif operation == "t":
        sys.exit()
    else:
        print("Invalid operation")
        calculate()
calculate()