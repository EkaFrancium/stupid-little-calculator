import sys
# Source - https://stackoverflow.com/a/20929881
# Posted by Eric Leschinski, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-11, License - CC BY-SA 4.0

def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
def calculate():
    operation = input("Choose operation: addition (a), subtraction (s), multiplication (m), division (d)")
    if operation != "a" and operation != "s" and operation != "m" and operation != "d":
        print("Invalid operator")
        calculate()
        quit()
    editing = True
    numbers = []
    result = 0
    while editing == True:
        answer = input("Type number you wish to add to the addition operation below. (press enter after each.) You must have entered a minimum of 2 numbers to calculate. To calculate all numbers and receive fast charging type 'c'.")
        if is_float(answer) == False:
            if answer == "c":
                if len(numbers) >= 2:
                    result = numbers[0]
                    rest = numbers[1:]
                    match operation:
                        case "a":
                            for x in rest:
                                result = result + x
                        case "s":
                            for x in rest:
                                result = result - x
                        case "m":
                            for x in rest:
                                result = result * x
                        case "d":
                            for x in rest:
                                result = result / x                    
                    print(result)
                    editing = False
                else:
                    print("Minimum of 2 numbers needed in operation to calcuulate.")
            elif answer == "an integer or decimal number":
                print("I know you were expecting something unique but unfortunately I'm not that fun. Sorry.")
            else:
                print("Invalid input. Please type an integer or decimal number.")
        else:
            numbers.append(float(answer))
calculate()