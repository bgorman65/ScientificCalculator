# Importing needed libraries and files

import customtkinter as ctk
from buttons import Button, NumberButton
from settings import *
import math

# Creating Calculator Class for logic

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Basic CustomTKinter Options
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.geometry(f'{MAIN_SIZE[0]}x{MAIN_SIZE[1]}')
        self.resizable(False, False)
        self.title("Scientific Calculator")
        # Row and Col setup
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform="a")
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform="a")
        # Data
        self.result_string = ctk.StringVar(value="0")
        self.firstNum = ctk.StringVar(value="")
        self.numDisplay = []
        self.operation = []
        # Widgets
        self.createWidget()
        self.mainloop()

    # Function to create the needed widgets in the window

    def createWidget(self):
        # Fonts

        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        reduced_font = ctk.CTkFont(family=FONT, size=REDUCED_FONT_SIZE)

        # Results Label

        ResultsLabel(self, 0, main_font, self.result_string)

        # Clear Button

        Button(parent=self, text=OPERATORS["clear"]["text"], func=self.clear, col=OPERATORS["clear"]["col"], row=OPERATORS["clear"]["row"], font=main_font)

        # Operator Buttons

        Button(parent=self, text=MATH_POSITIONS["%"]["character"], func=self.remainder, col=MATH_POSITIONS["%"]["col"], row=MATH_POSITIONS["%"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["+"]["character"], func=self.addition, col=MATH_POSITIONS["+"]["col"], row=MATH_POSITIONS["+"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["-"]["character"], func=self.subtraction, col=MATH_POSITIONS["-"]["col"], row=MATH_POSITIONS["-"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["="]["character"], func=self.equals, col=MATH_POSITIONS["="]["col"], row=MATH_POSITIONS["="]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["*"]["character"], func=self.multiplication, col=MATH_POSITIONS["*"]["col"], row=MATH_POSITIONS["*"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["/"]["character"], func=self.division, col=MATH_POSITIONS["/"]["col"], row=MATH_POSITIONS["/"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["x^y"]["character"], func=self.givenPower, col=MATH_POSITIONS["x^y"]["col"], row=MATH_POSITIONS["x^y"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["x^2"]["character"], func=self.square, col=MATH_POSITIONS["x^2"]["col"], row=MATH_POSITIONS["x^2"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["x!"]["character"], func=self.factorial, col=MATH_POSITIONS["x!"]["col"], row=MATH_POSITIONS["x!"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["e^x"]["character"], func=self.givenExpontenial, col=MATH_POSITIONS["e^x"]["col"], row=MATH_POSITIONS["e^x"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["√"]["character"], func=self.root, col=MATH_POSITIONS["√"]["col"], row=MATH_POSITIONS["√"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["x√y"]["character"], func=self.givenRoot, col=MATH_POSITIONS["x√y"]["col"], row=MATH_POSITIONS["x√y"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["sin"]["character"], func=self.sin, col=MATH_POSITIONS["sin"]["col"], row=MATH_POSITIONS["sin"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["arcsin"]["character"], func=self.arcSin, col=MATH_POSITIONS["arcsin"]["col"], row=MATH_POSITIONS["arcsin"]["row"], font=reduced_font)
        Button(parent=self, text=MATH_POSITIONS["cos"]["character"], func=self.cos, col=MATH_POSITIONS["cos"]["col"], row=MATH_POSITIONS["cos"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["arccos"]["character"], func=self.arcCos, col=MATH_POSITIONS["arccos"]["col"], row=MATH_POSITIONS["arccos"]["row"], font=reduced_font)
        Button(parent=self, text=MATH_POSITIONS["tan"]["character"], func=self.tan, col=MATH_POSITIONS["tan"]["col"], row=MATH_POSITIONS["tan"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["arctan"]["character"], func=self.arcTan, col=MATH_POSITIONS["arctan"]["col"], row=MATH_POSITIONS["arctan"]["row"], font=reduced_font)
        Button(parent=self, text=MATH_POSITIONS["log"]["character"], func=self.log, col=MATH_POSITIONS["log"]["col"], row=MATH_POSITIONS["log"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["ln"]["character"], func=self.ln, col=MATH_POSITIONS["ln"]["col"], row=MATH_POSITIONS["ln"]["row"], font=main_font)
        Button(parent=self, text=MATH_POSITIONS["."]["character"], func=self.decimal, col=MATH_POSITIONS["."]["col"], row=MATH_POSITIONS["."]["row"], font=main_font)

        # Constant Buttons

        Button(parent=self, text=CONSTANTS["pi"]["character"], func=self.pi, col=CONSTANTS["pi"]["col"], row=CONSTANTS["pi"]["row"], font=main_font)
        Button(parent=self, text=CONSTANTS["e"]["character"], func=self.exponential, col=CONSTANTS["e"]["col"], row=CONSTANTS["e"]["row"], font=main_font)

        # Number Buttons

        NumberButton(parent=self, text="1", func=self.one, col=NUM_POSITIONS[1]["col"], row=NUM_POSITIONS[1]["row"], font=main_font, span=NUM_POSITIONS[1]["span"])
        NumberButton(parent=self, text="2", func=self.two, col=NUM_POSITIONS[2]["col"], row=NUM_POSITIONS[2]["row"], font=main_font, span=NUM_POSITIONS[2]["span"])
        NumberButton(parent=self, text="3", func=self.three, col=NUM_POSITIONS[3]["col"], row=NUM_POSITIONS[3]["row"], font=main_font, span=NUM_POSITIONS[3]["span"])
        NumberButton(parent=self, text="4", func=self.four, col=NUM_POSITIONS[4]["col"], row=NUM_POSITIONS[4]["row"], font=main_font, span=NUM_POSITIONS[4]["span"])
        NumberButton(parent=self, text="5", func=self.five, col=NUM_POSITIONS[5]["col"], row=NUM_POSITIONS[5]["row"], font=main_font, span=NUM_POSITIONS[5]["span"])
        NumberButton(parent=self, text="6", func=self.six, col=NUM_POSITIONS[6]["col"], row=NUM_POSITIONS[6]["row"], font=main_font, span=NUM_POSITIONS[6]["span"])
        NumberButton(parent=self, text="7", func=self.seven, col=NUM_POSITIONS[7]["col"], row=NUM_POSITIONS[7]["row"], font=main_font, span=NUM_POSITIONS[7]["span"])
        NumberButton(parent=self, text="8", func=self.eight, col=NUM_POSITIONS[8]["col"], row=NUM_POSITIONS[8]["row"], font=main_font, span=NUM_POSITIONS[8]["span"])
        NumberButton(parent=self, text="9", func=self.nine, col=NUM_POSITIONS[9]["col"], row=NUM_POSITIONS[9]["row"], font=main_font, span=NUM_POSITIONS[9]["span"])
        NumberButton(parent=self, text="0", func=self.zero, col=NUM_POSITIONS[0]["col"], row=NUM_POSITIONS[0]["row"], font=main_font, span=NUM_POSITIONS[0]["span"])

    # Functions for logic

    # Function to evaluate the expression given
    # First gathers last data entry and appends it to list
    # Second creates a formula string from the list and then evaluates the operation
    # Lastly updates needed variables to continue calculation

    def equals(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        formula = " ".join(self.operation)
        result = eval(formula)
        self.operation.clear()
        self.numDisplay = [str(result)]
        self.result_string.set(result)

    # Function to reset the calculator
    # Done by clearing the output and data

    def clear(self):
        self.result_string.set(0)
        self.firstNum.set("")
        self.numDisplay.clear()
        self.operation.clear()

    # Function for operations that can be done with the python syntax
    # easily Checks if a number exists then adds that number and
    # specified operation to a list to be evaluated

    def remainder(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("%")
            self.numDisplay.clear()

    def addition(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("+")
            self.numDisplay.clear()

    def subtraction(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("-")
            self.numDisplay.clear()

    def multiplication(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("*")
            self.numDisplay.clear()

    def division(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("/")
            self.numDisplay.clear()

    def square(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("**")
            self.operation.append("2")
            self.numDisplay.clear()

    def root(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("**")
            self.operation.append(".5")
            self.numDisplay.clear()

    def givenRoot(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("**")
            self.operation.append("1/")
            self.numDisplay.clear()

    def givenPower(self):
        current = "".join(self.numDisplay)
        if current:
            self.operation.append(current)
            self.operation.append("**")
            self.numDisplay.clear()

    # Functions for constants

    def pi(self):
        self.numDisplay.append(str(math.pi))
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def exponential(self):
        self.numDisplay.append(str(math.exp(1)))
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    # Various operations not able ot be done in python easily
    # These functions will have to evaluate a number and then
    # Similarly to equals reset the operation list and add it
    # to it for proper functionality

    def givenExpontenial(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = int(self.operation[0])
        x = math.exp(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def factorial(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = int(self.operation[0])
        fact = 1
        for i in range(1, cur + 1):
            fact = fact * i
        self.operation.clear()
        self.numDisplay = [str(fact)]
        self.result_string.set(fact)

    def sin(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.sin(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def arcSin(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.asin(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def cos(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.cos(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def arcCos(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.acos(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def tan(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.tan(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def arcTan(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.atan(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def log(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.log(cur, 10)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    def ln(self):
        current = "".join(self.numDisplay)
        self.operation.append(current)
        cur = float(self.operation[0])
        x = math.log(cur)
        self.operation.clear()
        self.numDisplay = [str(x)]
        self.result_string.set(x)

    # Functions for number button functionality
    # Adds specified character to a list, then joins
    # list into a string and displays that string in the window

    def decimal(self):
        self.numDisplay.append(".")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def one(self):
        self.numDisplay.append("1")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def two(self):
        self.numDisplay.append("2")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def three(self):
        self.numDisplay.append("3")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def four(self):
        self.numDisplay.append("4")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def five(self):
        self.numDisplay.append("5")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def six(self):
        self.numDisplay.append("6")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def seven(self):
        self.numDisplay.append("7")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def eight(self):
        self.numDisplay.append("8")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def nine(self):
        self.numDisplay.append("9")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

    def zero(self):
        self.numDisplay.append("0")
        full_number = ''.join(self.numDisplay)
        self.result_string.set(full_number)

# Class to make results window

class ResultsLabel(ctk.CTkLabel):
    def __init__(self, parent, row, font, res):
        super().__init__(master=parent, anchor="e", font=font, textvariable=res)
        self.grid(column=0, columnspan=7, row=row, padx=10)

# Running an instance of the calculator object

if __name__ == "__main__":
    Calculator()