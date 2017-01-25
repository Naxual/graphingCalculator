# ProcessFun.py

# Algorithm:
# 1. Take user-input function as input
# 2. Convert input into python-processable function


class ProcessFun:
    def __init__(self, function):
        self.__function = function

    def process(self):
        processFunc = ""
        mathConstants = ["π", "e"]
        char = 0
        while char < len(self.__function):
            # Operations requiring no checks
            if self.__function[char] in ["+", "-", "/", "*", ")", "."]:
                processFunc += self.__function[char]
            elif self.__function[char] == "f":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                            self.__function[char-1] == "X" or
                            self.__function[char-1] in mathConstants):
                        processFunc += "*"
                processFunc += "math.factorial"
                char += 8
            elif self.__function[char] == "d":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                            self.__function[char-1] == "X" or
                            self.__function[char-1] in mathConstants):
                        processFunc += "*"
                processFunc += "misc.derivative(lambda X:"
                char += 4
            elif self.__function[char] == "i":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                            self.__function[char-1] == "X" or
                            self.__function[char-1] in mathConstants):
                        processFunc += "*"
                if self.__function[char:char+8] == "integral":
                    processFunc += "integrate.quad(lambda X:"
                    char += 8
            elif self.__function[char] == "L":
                if char > 0:
                    if (self.__function[char-1].isdigit() or 
                            self.__function[char-1] == "X" or
                            self.__function[char-1] in mathConstants):
                        processFunc += "*"
                if self.__function[char:char+3] == "LOG":
                    processFunc += "np.log10"
                    char += 2
                else:
                    processFunc += "np.log"
                    char += 1

            # Special case; (^) -> (**)
            elif self.__function[char] == "^":
                processFunc += "**"
            # Trig self.__functions
            elif self.__function[char] == "S":
                if self.__function[char-1] != "O":
                    if char > 0:
                        if (self.__function[char-1].isdigit() or 
                                self.__function[char-1] == "X" or 
                                self.__function[char-1] in mathConstants):
                            processFunc += "*"
                    if self.__function[char:char+6] == "SIN^-1":
                        processFunc += "np.arcsin"
                        char += 5
                    else:
                        processFunc += "np.sin"
                        char += 2
            elif self.__function[char] == "C":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                            self.__function[char-1] == "X" or
                            self.__function[char-1] in mathConstants):
                        processFunc += "*"
                if self.__function[char:char+6] == "COS^-1":
                    processFunc += "np.arccos"
                    char += 5
                else:
                    processFunc += "np.cos"
                    char += 2
            elif self.__function[char] == "T":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                        self.__function[char-1] == "X" or
                        self.__function[char-1] in mathConstants):
                        processFunc += "*"
                if self.__function[char:char+6] == "TAN^-1":
                    processFunc += "np.arctan"
                    char += 5
                else:
                    processFunc += "np.tan"
                    char += 2
            elif self.__function[char] == "X":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                            self.__function[char-1] in
                            mathConstants or self.__function[char-1] == ")"):
                        processFunc += "*"
                processFunc += "X"
    
            elif self.__function[char] == "(":
                if char > 0:
                    if (self.__function[char-1].isdigit() or
                            self.__function[char-1] == "X" or
                            self.__function[char-1] in mathConstants or 
                            self.__function[char-1] == ")"):
                        if (self.__function[char-6:char] != "SIN^-1" and 
                                self.__function[char-6:char] != "COS^-1" and
                                self.__function[char-6:char] != "TAN^-1"):
                            processFunc += "*"
                processFunc += self.__function[char]
    
            elif self.__function[char].isdigit():
                if char > 0:
                    if (self.__function[char-1] == "X" or
                            self.__function[char-1] == ")" or
                            self.__function[char-1] in mathConstants):
                        processFunc += "*"
                processFunc += self.__function[char]
    
            elif self.__function[char] in mathConstants:
                if char > 0:
                    if (self.__function[char-1] == "X" or
                            self.__function[char-1] == ")" or
                            self.__function[char-1] in mathConstants or
                            self.__function[char-1].isdigit()):
                        processFunc += "*"
                if self.__function[char] == "e":
                    processFunc += "np.e"
                if self.__function[char] == "π":
                    processFunc += "np.pi"

            else:
                processFunc += self.__function[char]

            char += 1

        return processFunc

    def __str__(self):
        return self.__function
