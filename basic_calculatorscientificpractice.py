# modules imported
import time

# choose which calculator you wish to use
calc_type = str(input("which calculator do you wish to use? (standard, trig or scientific)")).lower()

# if you choose one of the options above then you will be brought to this if statement which will execute one of either of the options standard or scientific 
if calc_type == "standard":
        num1 = float(input('Enter your first number: '))
        operator = input(('Enter operator: '))
        num2 = float(input('Enter your second number: '))
    # this code will operate the output sum once it has determined with mathematical operator you have chosen
        # addition
        if operator == '+':
            print("You have selected addition")
            time.sleep(1)
            print(num1 + num2)
        # subtraction
        elif operator == '-':
            print("You have selected subtraction")
            time.sleep(1)
            print(num1 - num2)
        # division
        elif operator == '/':
            print("You have selected divison")
            time.sleep(1)
            print(num1 / num2)
        # multiplication
        elif operator == "*":
            print("You have selected multiplication")
            time.sleep(1)
            print(num1 * num2)
    # if the user didn't put an operator
        else:
            pass

# if the user did not select the standard calculator then this code will be executed accordingly 
if calc_type == "trig":
    # give user selection of scientific calculations they can perform
    trig_calc_option = str(input("Please select a function? (sine, cosine, tangent, cosecant, secant, cotangent)")).lower()
    # sine is selected
    if trig_calc_option == "sine":
        print("You selected sine... please follow the onscreen instructions")
        time.sleep(1)
        opposite = float(input("Please input the opposite side figure?"))
        hypotenuse = float(input("Please input the hypotenuse?"))
        time.sleep(1)
        print(opposite / hypotenuse)
    # cosine is selected
    elif trig_calc_option == "cosine":
        print("You selected cosine... please follow the onscreen instructions")
        time.sleep(1)
        adjacent = float(input("Please enter the adjacent figure?"))
        hypotenuse =  float(input("Please enter the hypotenuse?"))
        time.sleep(1)
        print(adjacent / hypotenuse)
    # tangent is selected
    elif trig_calc_option == "tangent":
        print("You selected tangent... please follow the onscreen instructions")
        time.sleep(1)
        opposite = float(input("Please enter the opposite side figure?"))
        adjacent = float(input("Please enter the adjacent figure?"))
        time.sleep(1)
        print(opposite / adjacent)
    # cosecant is selected
    elif trig_calc_option == "cosecant":
        print("You selected cosecant... please follow the onscreen instructions")
        time.sleep(1)
        hypotenuse = float(input("Please enter the hypotenuse?"))
        opposite = float(input("Please enter the opposite side?"))
        time.sleep(1)
        print(hypotenuse / opposite)
    # secant is selected
    elif trig_calc_option == "secant":
        print("You selected secant... please follow the onscreen instructions")
        time.sleep(1)
        hypotenuse = float(input("Please enter the hypotenuse?"))
        adjacent = float(input("Please enter the adjacent figure?"))
        time.sleep(1)
        print(hypotenuse / adjacent)
    # cotangent is selected    
    elif trig_calc_option == "cotangent":
        print("You selected cotangent... please follow the onscreen instructions")
        time.sleep(1)
        adjacent = float(input("Please enter the adjacent side figure?"))
        opposite = float(input("Please enter the opposide side figure?"))
        time.sleep(1)
        print(adjacent / opposite)
    else:
        pass

