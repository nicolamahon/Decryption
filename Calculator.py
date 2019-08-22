"""
This is a simple calculator, made in Python, using tkinter for GUI programming.

Date: 2018-09-18
Author: Nicola Mahon C15755031

"""

# Library Imports
import tkinter as tk
from tkinter import *
from tkinter import Entry
from tkinter import StringVar


# Begin Function Prototypes

# when a button is pressed i.e. 0-9 or decimal point
def on_click(number):
    # access the global variables
    global input_value, firstValue, secondValue, operator
    # checks if this is the first value being entered
    if not secondFlag:
        # checks that the input_value is not empty
        if input_value != '':
            # if not empty, then concatenate the current value to the user's input i.e. more than 1 digit
            input_value = input_value + str(number)
        else:
            # otherwise, assign the user's input to the global variable
            input_value = str(number)
        # set the textbox to this new value
        user_input.set(input_value)
    # otherwise this is the second value
    else:
        # concatenate the second value to current value i.e. more than 1 digit
        input_value = input_value + str(number)
        # update the textbox to show the user their values
        user_input.set(str(firstValue) + operator + input_value)
        # update the global variable for the second value
        secondValue = input_value


# get the user's selected operator i.e. +, -, *, /
def get_operator(value):
    # access global variables
    global operator, secondFlag, firstValue, input_value
    # set the value for the first variable
    firstValue = input_value
    # printing for testing
    print("firstValue: " + firstValue)
    print("operator: " + value)
    # reset the input value once an operator has been chosen
    input_value = ''
    # update the global operator value
    operator = value
    # update the textbox with the operator value
    user_input.set(str(firstValue) + value)
    # set flag to indicate we are on the second value
    secondFlag = True


# button to clear the textbox
def clear():
    # access global variables
    global operator, firstValue, secondValue, input_value, secondFlag
    # reset the global variables
    clear_values()
    # update the textbox to be empty
    user_input.set('')


# to clear the global variables
def clear_values():
    # access global variables
    global operator, firstValue, secondValue, input_value, secondFlag
    # reset their values
    operator = ''
    firstValue = 0
    secondValue = 0
    input_value = ''
    # set flag to false, to indicate that we are back to the first value
    secondFlag = False


# called to perform the calculations
def equals():
    # access global variables
    global operator, firstValue, secondValue
    # printing for testing
    print("secondValue: " + secondValue)
    try:
        # IF_ELSE block to perform calculations
        if operator == '+':
            result = add(firstValue, secondValue)
        elif operator == '-':
            result = subtract(firstValue, secondValue)
        elif operator == '*':
            result = multiply(firstValue, secondValue)
        else:
            result = divide(firstValue, secondValue)
        # update the textbox to the result of the calculation
        user_input.set(str(result))
        # printing for testing
        print("result: " + str(result))
    except SyntaxError:
        user_input.set("ERROR")
        raise
    # reset the global variables as the calculation is done or else erroneous
    clear_values()  # reset the values


"""
CALCULATION FUNCTIONS
"""


def add(a, b):
    result = float(a) + float(b)
    return result


def subtract(a, b):
    result = float(a) - float(b)
    return result


def multiply(a, b):
    result = float(a) * float(b)
    return result


def divide(a, b):
    result = float(a) / float(b)
    return result


# main function
if __name__ == "__main__":

    # initialise root window
    root = tk.Tk()
    # set title for root window
    root.title("Calculator")

    # for capturing user input
    user_input = StringVar()

    # global variables
    operator = ""
    firstValue = 0
    secondValue = 0
    secondFlag = False
    input_value = ''

    # add an input box for user input
    inputBox = Entry(root, bd=25, insertwidth=1, font=30, justify='right',
                     textvariable=user_input, ).grid(columnspan=4)

    """
    Add rows of buttons for the keypad and +, -, *, /, =, C to clear input
    lambda is used in each button to control the function calls only when clicked, not at startup
    """

    # GRID, ROWS and COLS
    # 7, 8, 9, +
    # 4, 5, 6, -
    # 1, 2, 3, *
    # C, 0, =, /

    # ROW0 = 7, 8, 9, + (add)
    button7 = Button(root, padx=20, pady=16, bd=8, text="7", fg="black",
                     command=lambda: on_click(7)).grid(row=1, column=0)
    button8 = Button(root, padx=20, pady=16, bd=8, text="8", fg="black",
                     command=lambda: on_click(8)).grid(row=1, column=1)
    button9 = Button(root, padx=20, pady=16, bd=8, text="9", fg="black",
                     command=lambda: on_click(9)).grid(row=1, column=2)
    Add = Button(root, padx=21, pady=16, bd=8, text="+", fg="black",
                 command=lambda: get_operator('+')).grid(row=1, column=3)

    # ROW1 = 4, 5, 6, - (minus)
    button4 = Button(root, padx=20, pady=16, bd=8, text="4", fg="black",
                     command=lambda: on_click(4)).grid(row=2, column=0)
    button5 = Button(root, padx=20, pady=16, bd=8, text="5", fg="black",
                     command=lambda: on_click(5)).grid(row=2, column=1)
    button6 = Button(root, padx=20, pady=16, bd=8, text="6", fg="black",
                     command=lambda: on_click(6)).grid(row=2, column=2)
    Sub = Button(root, padx=20, pady=16, bd=8, text=" - ", fg="black",
                 command=lambda: get_operator('-')).grid(row=2, column=3)

    # ROW2 = 1, 2, 3, * (multiply)
    button1 = Button(root, padx=20, pady=16, bd=8, text="1", fg="black",
                     command=lambda: on_click(1)).grid(row=3, column=0)
    button2 = Button(root, padx=20, pady=16, bd=8, text="2", fg="black",
                     command=lambda: on_click(2)).grid(row=3, column=1)
    button3 = Button(root, padx=20, pady=16, bd=8, text="3", fg="black",
                     command=lambda: on_click(3)).grid(row=3, column=2)
    Mul = Button(root, padx=20, pady=16, bd=8, text=" * ", fg="black",
                 command=lambda: get_operator('*')).grid(row=3, column=3)

    # ROW3 = C (clear), 0 (zero), . (decimal), ÷ (divide)
    buttonClear = Button(root, padx=20, pady=16, bd=8, text="C", fg="black",
                         command=clear).grid(row=4, column=0)
    button0 = Button(root, padx=20, pady=16, bd=8, text="0", fg="black",
                     command=lambda: on_click(0)).grid(row=4, column=1)
    btnDecimal = Button(root, padx=20, pady=16, bd=8, text=".", fg="black",
                        command=lambda: on_click('.')).grid(row=4, column=2)
    Div = Button(root, padx=21, pady=16, bd=8, text="÷", fg="black",
                 command=lambda: get_operator('/')).grid(row=4, column=3)

    # ROW4 = EQUALS
    btnEquals = Button(root, padx=20, pady=16, bd=8, text="=", fg="black",
                       command=equals).grid(column=0, row=5, columnspan=4, sticky=tk.W+tk.E)

    # run program
    root.mainloop()
