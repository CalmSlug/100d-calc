# Importing art assets:
import calc_art


# Calculator operations:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary with all operations:
calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Variable linking up intro and cont blocks:
answer = 0

# Introduction block that runs at the start of the program:
def intro():
    # Increasing scope:
    global answer
    
    # Introduction art:
    print(calc_art.logo)

    # User input block:
    # 1. get the 1st number from user
    # 2. print available operations from the dictionary
    # 3. get the desired operation from user
    # 4. get the 2nd number from user
    num1 = float(input("What's the 1st number?: "))
    for key in calc_operations:
        print(key)
    operation_key = input("Pick an operation from the line above: ")
    num2 = float(input("What's the 2nd number?: "))

    # Calc block:
    # 1. look up requested operation in the dictionary
    # 2. calculate an answer using that operation
    calc = calc_operations[operation_key]
    answer = calc(num1, num2)

    # Final statement:
    print(f"{num1} {operation_key} {num2} = {answer}")

# Continue block that runs if user requested more operations;
# Uses last answer as 1st number in calculations:
def cont():
    # Increasing scope:
    global answer

    # User input block:
    # 1. get the desired operation from user
    # 2. get the 2nd number from user
    operation_key = input("Pick another operation: ")
    num2 = float(input("What's the next number?: "))

    # Calc block:
    # 1. look up requested operation in the dictionary
    # 2. calculate an answer using that operation
    calc = calc_operations[operation_key]
    new_answer = calc(answer, num2)

    # Final statement:
    print(f"{answer} {operation_key} {num2} = {new_answer}")

    # Re-writing global variable to chain cont blocks:
    answer = new_answer
    

# Main logic:
# 1. Intro block as a starting point
# 2. Cont block in an infinite loop for more calculations
intro()
while True:
    on_or_off = input(f"Continue working with {answer}? Type Y or N: ").lower()
    if on_or_off == "y":
        cont()
    else:
        break
