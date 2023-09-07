# Importing needed libraries and files

from customtkinter import CTkButton

# Creating a class for buttons

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span=1):
        super().__init__(master=parent, text=text, command=func, height=75, font=font)
        self.grid(row=row, columnspan=span, column=col, padx=5, pady=5)

class NumberButton(Button):
    def __init__(self, parent, text, func, col, row, font, span):
        super().__init__(parent=parent, text=text, func=func, row=row, col=col, font=font, span=span)
