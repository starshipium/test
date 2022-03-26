# calculator.py
# Nora Mellik, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
number_1=int(input('Enter your first value: '))      # Input for the first number
operator_1=(input('Enter your first operator: '))    # Input for the first operator
number_2=int(input('Enter your second value: '))     # Input for the second number
operator_2=(input('Enter your second operator: '))   # Input for the second operator
number_3=int(input('Enter your third value: '))      # Input for the third number

print('Entered expression:', end =" ")         # Outputs the expression entered by the user
print(number_1, operator_1, number_2, operator_2, number_3) # Outputs the expression entered by the user

if operator_1 == '*' or operator_1 == '/':             #Initially checks whether operator_1 is multiplication or division
    if operator_1 == '*':                              # Proceeds here if it is multiplication
        new_number = number_1*number_2
    else:                                              # Other option is to divide if not multiplication
        new_number = number_1 // number_2
    if operator_2 == '*' or operator_2 == '/':         # Then checks if operator_2 is multiplication or division
        if operator_2 == '*':                          # Multiplies with new number if multiplication
            final_value = new_number * number_3        # Assigns final_value if this branch executes
        else:
            final_value = new_number // number_3       # Divides if not multiplication
    if operator_2 == '+' or operator_2 == '-':         # If operator_2 is neither multiplication nor division, it will go to addition or subtraction
        if operator_2 == '+':                          # Checks for addition to new value
            final_value = new_number + number_3        # Assigns final_value
        else:
            final_value = new_number - number_3        # If false, it will subtract, then assign final_value

if operator_1 == '+' or operator_1 == '-':             # If the first branch does not execute, that means operator_1 has to be addition or subtraction
    if operator_2 == '*' or operator_2 == '/':         # First checks if operator_2 is multiplication or division, in which case it has to perform operator_2 before operator_1
        if operator_2 == '*':                          # Checks if operator_2 is multiplication
            new_number = number_2 * number_3
        else:                                          # Divides if not multiplication
            new_number = number_2 // number_3
        if operator_1 == '+':                          # Checks if operator_1 is addition
            final_value = number_1 + new_number
        else:                                          # Subtracts if not addition
            final_value = number_1 - new_number        # Assigns final_value
    elif operator_2 == '+' or operator_2 == '-':       # If previous nested branch did not execute, it will go to final scenario, where operator_2 is also addition or subtraction 
            if operator_1 == '+':                      # Checks if operator_1 is addition
                new_number = number_1 + number_2
            else:                                      # Subtracts if not addition
                new_number = number_1 - number_2
            if operator_2 == '+':                      # Adds number_3 to new number if operator_2 is addition, then assigns final_value
                final_value = new_number + number_3
            else:                                      # Subtracts if not addition, then assigns final_value
                final_value = new_number - number_3


print('Your final answer =', end =" ") # Outputs the answer to the expression entered by the user
print(final_value)                      # Outputs the answer to the expression entered by the user 