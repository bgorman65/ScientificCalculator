# Sizing Settings

MAIN_SIZE = (605, 520)
MAIN_ROWS = 6
MAIN_COLUMNS = 7

# Text Settings

FONT = "Helvetica"
NORMAL_FONT_SIZE = 30
REDUCED_FONT_SIZE = 18

# Dictionaries for Number and Operation Button Settings

NUM_POSITIONS = {
    0: {"col": 3, "row": 5, "span": 2},
    1: {"col": 3, "row": 4, "span": 1},
    2: {"col": 4, "row": 4, "span": 1},
    3: {"col": 5, "row": 4, "span": 1},
    4: {"col": 3, "row": 3, "span": 1},
    5: {"col": 4, "row": 3, "span": 1},
    6: {"col": 5, "row": 3, "span": 1},
    7: {"col": 3, "row": 2, "span": 1},
    8: {"col": 4, "row": 2, "span": 1},
    9: {"col": 5, "row": 2, "span": 1}
}

CONSTANTS = {
    "e": {"col": 0, "row": 1, "character": "e"},
    "pi": {"col": 0, "row": 2, "character": "\u03C0"}
}

MATH_POSITIONS = {
    "+": {"col": 6, "row": 3, "character": "+"},
    "-": {"col": 6, "row": 4, "character": "-"},
    "*": {"col": 6, "row": 2, "character": "×"},
    "/": {"col": 5, "row": 1, "character": "÷"},
    "%": {"col": 4, "row": 1, "character": "%"},
    "x^y": {"col": 3, "row": 1, "character": "x^y"},
    "x^2": {"col": 2, "row": 1, "character": "x^2"},
    "x!": {"col": 1, "row": 1, "character": "!"},
    "e^x": {"col": 1, "row": 2, "character": "e^x"},
    "√": {"col": 2, "row": 2, "character": "√"},
    "x√y": {"col": 2, "row": 3, "character": "x√y"},
    "sin": {"col": 0, "row": 3, "character": "sin"},
    "arcsin": {"col": 1, "row": 3, "character": "arcsin"},
    "cos": {"col": 0, "row": 4, "character": "cos"},
    "arccos": {"col": 1, "row": 4, "character": "arccos"},
    "tan": {"col": 0, "row": 5, "character": "tan"},
    "arctan": {"col": 1, "row": 5, "character": "arctan"},
    "log": {"col": 2, "row": 4, "character": "log"},
    "ln": {"col": 2, "row": 5, "character": "ln"},
    "=": {"col": 6, "row": 5, "character": "="},
    ".": {"col": 5, "row": 5, "character": "."}
}

OPERATORS = {
    "clear": {"col": 6, "row": 1, "text": "AC"}
}
