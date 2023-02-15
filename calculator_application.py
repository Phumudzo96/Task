txt_sum = open("number_sum.txt","r+")                # open the text file

while True:
    try:
        number1 = int(input("Enter a number: "))     # ask the useer to enter a number
        break
    except:
        print("Invalid selection. Try again")        # if the user inputs anything thats not a number. this must be printed

while True:
    try:
        number2 = int(input("Enter a second number: "))
        break
    except:
        print("Invalid selection. Try again")

operation = input("Enter an operation: ")              # user must enter one of the following operations.[+, -, *, /]

if operation == "+":
    sum = (number1 + number2)
    txt_sum.write(f"{number1} + {number2} = {sum} \n")
    txt_sum.read()
    print(sum)
elif operation == "-":
    sum = (number1 - number2)
    txt_sum.write(f"{number1} - {number2} = {sum} \n")
    txt_sum.read()
    print(sum)
elif operation == "*":
    sum = (number1 * number2)
    txt_sum.write(f"{number1} * {number2} = {sum} \n")
    txt_sum.read()
    print(sum)
elif operation == "/":
    sum = (number1 / number2)
    txt_sum.write(f"{number1} / {number2} = {sum} \n")
    txt_sum.read()
    print(sum)
else:
    print("Invalid operation entered")

txt_sum.close()                        # close the text file

print_file = input("[1]Enter numbers again or [2]print out equations... 1 or 2? ")  # ask user to continue entering numbers or print out text file

if print_file == "1":
    while True:
        try:
            number1 = int(input("Enter a number: "))     # ask the useer to enter a number
            break
        except:
            print("Invalid selection. Try again")        # if the user inputs anything thats not a number. this must be printed

    while True:
        try:
            number2 = int(input("Enter a second number: "))
            break
        except:
            print("Invalid selection. Try again")

    operation = input("Enter an operation: ")              # user must enter one of the following operations.[+, -, *, /]

    if operation == "+":
        sum = (number1 + number2)
        txt_sum.write(f"{number1} + {number2} = {sum} \n")
        txt_sum.read()
        print(sum)
    elif operation == "-":
        sum = (number1 - number2)
        txt_sum.write(f"{number1} - {number2} = {sum} \n")
        txt_sum.read()
        print(sum)
    elif operation == "*":
        sum = (number1 * number2)
        txt_sum.write(f"{number1} * {number2} = {sum} \n")
        txt_sum.read()
        print(sum)
    elif operation == "/":
        sum = (number1 / number2)
        txt_sum.write(f"{number1} / {number2} = {sum} \n")
        txt_sum.read()
        print(sum)
    else:
        print("Invalid operation entered")
elif print_file == "2":
    file = input("Enter the name of file: ")   # ask the user for name of the file they want printed out
    file = None
    try:
        file = open("number_sum.txt","r+")
        file1 = file.read()                    # the file must read 
        print(file1)                           # the file must be printed

    except FileNotFoundError:
        print("file name entered is not available") # if the file is not found this must printed out

    finally:
        if file is not None:
            file.close()                         # when everything is done the file must be closed





