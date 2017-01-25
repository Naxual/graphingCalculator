# Gui.py

# Algorithm:
# 1. Start Tk window
# 2. Initiate frames, buttons, entry boxes
# 3. Place widgets onto respective locations
# 4. Handle basic events caused by button presses

from tkinter import *
import matplotlib.pyplot as pyplot
import numpy as np
import math
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("qt4agg")
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from scipy import integrate, misc
from RiemannSums import *
from ProcessFun import *


class Gui:
    def __init__(self):
        self.__mainProgram = Tk()

        # defining string variables
        self.__userInputLog = StringVar()
        self.__userOutputLog = StringVar()
        self.__inputVar = StringVar()
        self.__outputVar = StringVar()
        self.__inputFuncVar = StringVar()
        self.__tableText = StringVar()
        self.__riemannAns = StringVar()

        # defining variables
        self.__enteringFunction = False
        self.__enteringRiemann = False
        
        # answer variable
        self.__ans = '0'

        # mainframe
        self.__mainFrame = Frame(self.__mainProgram)

        # setting up frames
        self.__numbersF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                                bg="white")
        self.__rightF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                              bg="white")
        self.__topMiddleF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                                  bg="white")
        self.__leftF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                            bg="white")
        self.__displayF = Frame(self.__mainFrame, bd=3, relief=SUNKEN,
                                bg="white")
        self.__topLeftF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                                bg="white")
        self.__topRightF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                                 bg="white")
        self.__graphF = Frame(self.__mainFrame, bd=2, relief=RIDGE,
                              bg="white")
        self.__riemannF = Frame(self.__mainFrame, bd=3, relief=SUNKEN,
                                bg="white")
        self.__enterFuncF = Frame(self.__mainFrame, bd=3, relief=SUNKEN,
                                  bg="white")

        # name labels
        self.__nameJaLabel = Label(self.__mainFrame, text="James Yao")
        self.__nameRiLabel = Label(self.__mainFrame, text="Richard Zheng")
        self.__nameThLabel = Label(self.__mainFrame, text="Theodore Bauer")
        self.__nameJoLabel = Label(self.__mainFrame, text="John Rocco")

        self.__funcLabel = Label(self.__enterFuncF, text="Y = ", font=18,
                                 bg="white")
        self.__funcDynLabel = Label(self.__enterFuncF, font=18, bg="white",
                                    textvariable=self.__inputFuncVar)
        self.__riemannFuncLabel = Label(self.__riemannF, font=18, bg="white",
                                        textvariable=self.__inputFuncVar)
        self.__tableLabel = Label(self.__enterFuncF, font=12, bg="white",
                                  textvariable=self.__tableText)
        self.__riemannResultL = Label(self.__riemannF, font=12, bg="white",
                                      textvariable=self.__riemannAns, )
        self.__numRectanglesL = Label(self.__riemannF, font=12, bg="white",
                                      text="Number of Rectangles")
        self.__typeL = Label(self.__riemannF, font=12, bg="white",
                             text="Type of Riemann Sum")
        self.__riemannYLabel = Label(self.__riemannF, text="Y=", font=12,
                                     bg="white")

        # creating entry boxes
        self.__leftBoundE = Entry(self.__enterFuncF, bg="gray93")
        self.__leftBoundE.insert(0, "-2")
        self.__intervalE = Entry(self.__enterFuncF, bg="gray93")
        self.__intervalE.insert(0, "1")
        self.__rightBoundE = Entry(self.__enterFuncF, bg="gray93")
        self.__rightBoundE.insert(0, "2")
        self.__numRectanglesE = Entry(self.__riemannF, bg="gray93")
        self.__numRectanglesE.insert(0, "1")
        self.__typeE = Entry(self.__riemannF, bg="gray93")
        self.__typeE.insert(0, "midpoint")

        # buttons on numbers frame
        self.__oneB = Button(self.__numbersF, text="1",
                             command=lambda:self.__update("1"))
        self.__twoB = Button(self.__numbersF, text="2",
                             command=lambda:self.__update("2"))
        self.__threeB = Button(self.__numbersF, text="3",
                               command=lambda:self.__update("3"))
        self.__fourB = Button(self.__numbersF, text="4",
                              command=lambda:self.__update("4"))
        self.__fiveB = Button(self.__numbersF, text="5",
                              command=lambda:self.__update("5"))
        self.__sixB = Button(self.__numbersF, text="6",
                             command=lambda:self.__update("6"))
        self.__sevenB = Button(self.__numbersF, text="7",
                               command=lambda:self.__update("7"))
        self.__eightB = Button(self.__numbersF, text="8",
                               command=lambda:self.__update("8"))
        self.__nineB = Button(self.__numbersF, text="9",
                              command=lambda:self.__update("9"))
        self.__zeroB = Button(self.__numbersF, text="0",
                              command=lambda:self.__update("0"))
        self.__decimalB = Button(self.__numbersF, text=".",
                                 command=lambda:self.__update("."))
        self.__minusB = Button(self.__numbersF, text="( - )",
                               command=lambda:self.__update("-"))

        # buttons on right frame
        self.__enterB = Button(self.__rightF, text="ENTER",
            command=lambda:self.__calculate(self.__inputVar.get()))
        self.__addB = Button(self.__rightF, text="+",
                             command=lambda:self.__update("+"))
        self.__subtractB = Button(self.__rightF, text="-",
                                  command=lambda:self.__update("-"))
        self.__multiplyB = Button(self.__rightF, text="*",
                                  command=lambda:self.__update("*"))
        self.__divideB = Button(self.__rightF, text="/",
                                command=lambda:self.__update("/"))
        self.__powerB = Button(self.__rightF, text="^",
                               command=lambda:self.__update("^"))

        # top right clear button
        self.__clearB = Button(self.__topRightF, text="CLEAR",
                               command=self.__clear)

        # buttons on top left frame
        self.__quitB = Button(self.__topLeftF, text="QUIT",
                              command=self.__quit)
        self.__delB = Button(self.__topLeftF, text="DEL",
                             command=self.__del)
        self.__ansB = Button(self.__topLeftF, text="ANS",
                             command=self.__answer)

        # buttons on graph frame
        self.__graphB = Button(self.__graphF, text="GRAPH",
            command=lambda:self.__graph(self.__inputFuncVar.get()))
        self.__tableB = Button(self.__graphF, text="TABLE",
            command=lambda:self.__table(self.__inputFuncVar.get()))
        self.__riemannB = Button(self.__graphF, text="RIEMANN",
            command=self.__userEnterRiemann)
        self.__xB = Button(self.__graphF, text="X",
                           command=lambda:self.__update("X"))
        self.__yB = Button(self.__graphF, text="Y=",
                           command=self.__userEnterFunction)

        # buttons in left frame
        self.__sinB = Button(self.__leftF, text="SIN",
                             command=lambda:self.__update("SIN("))
        self.__cosB = Button(self.__leftF, text="COS",
                             command=lambda:self.__update("COS("))
        self.__tanB = Button(self.__leftF, text="TAN",
                             command=lambda:self.__update("TAN("))
        self.__logB = Button(self.__leftF, text="LOG",
                             command=lambda:self.__update("LOG("))
        self.__lnB = Button(self.__leftF, text="LN",
                            command=lambda:self.__update("LN("))
        self.__arcSinB = Button(self.__leftF, text="SIN^-1",
                                command=lambda:self.__update("SIN^-1("))
        self.__arcCosB = Button(self.__leftF, text="COS^-1",
                                command=lambda:self.__update("COS^-1("))
        self.__arcTanB = Button(self.__leftF, text="TAN^-1",
                                command=lambda:self.__update("TAN^-1("))
        self.__sqrtB = Button(self.__leftF, text="X^1/2",
                              command=lambda:self.__update("^(1/2)"))
        self.__sqB = Button(self.__leftF, text="X^2",
                            command=lambda:self.__update("^2"))
        self.__eB = Button(self.__leftF, text="e^X",
                           command=lambda:self.__update("e^("))
        self.__base10B = Button(self.__leftF, text="10^X",
                                command=lambda:self.__update("10^("))

        # buttons on top middle frame
        self.__leftParenthesis = Button(self.__topMiddleF, text="(",
                                        command=lambda:self.__update("("))
        self.__rightParenthesis = Button(self.__topMiddleF, text=")",
                                         command=lambda:self.__update(")"))
        self.__commaB = Button(self.__topMiddleF, text=",",
                               command=lambda:self.__update(","))
        self.__derivative = Button(self.__topMiddleF, text="d/dX",
                                   command=lambda:self.__update("d/dX("))
        self.__integral = Button(self.__topMiddleF, text="integral",
                                 command=lambda:self.__update("integral("))
        self.__inverse = Button(self.__topMiddleF, text="x^-1",
                                command=lambda:self.__update("^(-1)"))
        self.__factorial = Button(self.__topMiddleF, text="!",
                                  command=lambda:self.__update("factorial("))
        self.__i = Button(self.__topMiddleF, text="EE",
                          command=lambda:self.__update("*10^"))
        self.__e = Button(self.__topMiddleF, text="e",
                          command=lambda:self.__update("e"))
        self.__pi = Button(self.__topMiddleF, text="π",
                           command=lambda:self.__update("π"))
        
        # Riemann enter button
        self.__riemannEnterB = Button(self.__riemannF, text="ENTER",
            command=lambda:self.__riemann(self.__inputFuncVar.get()))

        # input display
        self.__inputDisplay = Label(self.__displayF, bg="white", font=14,
                                    textvariable=self.__inputVar)
        self.__outputDisplay = Label(self.__displayF, bg="white", font=14,
                                     textvariable=self.__outputVar)
        self.__leftBoundL = Label(self.__enterFuncF, bg="white",
                                  text="Left Bound", font=14)
        self.__intervalL = Label(self.__enterFuncF, bg="white",
                                     text="Interval", font=14)
        self.__rightBoundL = Label(self.__enterFuncF, bg="white",
                                     text="Right Bound", font=14)

        # user log display
        self.__userLogInputDisplay = Label(self.__displayF, bg="white",
            font=12, textvariable=self.__userInputLog)
        self.__userLogOutputDisplay = Label(self.__displayF, bg="white",
            font=12, textvariable=self.__userOutputLog)

        # placing buttons on number frame
        self.__oneB.place(x=15, y=127.5, height=41.25, width=45)
        self.__twoB.place(x=75, y=127.5, height=41.25, width=45)
        self.__threeB.place(x=135, y=127.5, height=41.25, width=45)
        self.__fourB.place(x=15, y=71.25, height=41.25, width=45)
        self.__fiveB.place(x=75, y=71.25, height=41.25, width=45)
        self.__sixB.place(x=135, y=71.25, height=41.25, width=45)
        self.__sevenB.place(x=15, y=15, height=41.25, width=45)
        self.__eightB.place(x=75, y=15, height=41.25, width=45)
        self.__nineB.place(x=135, y=15, height=41.25, width=45)
        self.__zeroB.place(x=15, y=183.75, height=41.25, width=45)
        self.__decimalB.place(x=75, y=183.75, height=41.25, width=45)
        self.__minusB.place(x=135, y=183.75, height=41.25, width=45)

        # placing buttons on right frame
        self.__addB.place(x=15, y=215, height=35, width=60)
        self.__subtractB.place(x=15, y=165, height=35, width=60)
        self.__multiplyB.place(x=15, y=115, height=35, width=60)
        self.__divideB.place(x=15, y=65, height=35, width=60)
        self.__powerB.place(x=15, y=15, height=35, width=60)
        self.__enterB.place(x=15, y=270, height=45, width=60)

        # placing top right clear button
        self.__clearB.place(x=15, y=15, height=45, width=60)

        # placing buttons on top left frame
        self.__quitB.place(x=15, y=15, height=45, width=55)
        self.__delB.place(x=15, y=75, height=30, width=55)
        self.__ansB.place(x=15, y=120, height=30, width=55)

        # placing buttons on graph frame
        self.__yB.place(x=15, y=15, height=30, width=39)
        self.__graphB.place(x=69, y=15, height=30, width=48)
        self.__tableB.place(x=131, y=15, height=30, width=45)
        self.__riemannB.place(x=190, y=15, height=30, width=60)
        self.__xB.place(x=266, y=15, height=30, width=34)

        # placing buttons on left frame
        self.__sinB.place(x=15, y=15, height=30, width=50)
        self.__cosB.place(x=80, y=15, height=30, width=50)
        self.__tanB.place(x=145, y=15, height=30, width=50)
        self.__arcSinB.place(x=15, y=60, height=30, width=50)
        self.__arcCosB.place(x=80, y=60, height=30, width=50)
        self.__arcTanB.place(x=145, y=60, height=30, width=50)
        self.__logB.place(x=145, y=105, height=30, width=50)
        self.__base10B.place(x=80, y=105, height=30, width=50)
        self.__lnB.place(x=145, y=150, height=30, width=50)
        self.__eB.place(x=80, y=150, height=30, width=50)
        self.__sqB.place(x=15, y=105, height=30, width=50)
        self.__sqrtB.place(x=15, y=150, height=30, width=50)


        # placing buttons on top middle frame
        self.__leftParenthesis.place(x=135, y=60, height=30, width=45)
        self.__rightParenthesis.place(x=195, y=60, height=30, width=45)
        self.__commaB.place(x=255, y=60, height=30, width=45)
        self.__pi.place(x=255, y=15, height=30, width=45)
        self.__e.place(x=195, y=15, height=30, width=45)
        self.__i.place(x=135, y=15, height=30, width=45)
        self.__factorial.place(x=75, y=15, height=30, width=45)
        self.__inverse.place(x=15, y=15, height=30, width=45)
        self.__derivative.place(x=75, y=60, height=30, width=45)
        self.__integral.place(x=15, y=60, height=30, width=45)

        # placing Riemann button on Riemann frame
        self.__riemannEnterB.place(x=15, y=120, height=30, width=45)
 
        # placing input and output labels
        self.__inputDisplay.pack(side="top")
        self.__userLogInputDisplay.pack(side="left")
        self.__userLogOutputDisplay.pack(side="right")

        # placing frames
        self.__numbersF.place(x=240, y=480, height=240, width=195)
        self.__rightF.place(x=450, y=390, height=330, width=90)
        self.__topMiddleF.place(x=120, y=360, height=105, width=315)
        self.__leftF.place(x=15, y=480, height=195, width=210)
        self.__topLeftF.place(x=15, y=300, height=165, width=90)
        self.__topRightF.place(x=450, y=300, height=75, width=90)
        self.__graphF.place(x=120, y=300, height=60, width=315)
        self.__enterFuncF.place(x=15, y=15, height=270, width=525)
        self.__riemannF.place(x=15, y=15, height=270, width=525)
        self.__displayF.place(x=15, y=15, height=270, width=525)

        # placing labels
        self.__nameJaLabel.place(x=30, y=685, height=15, width=70)
        self.__nameRiLabel.place(x=116, y=685, height=15, width=100)
        self.__nameThLabel.place(x=15, y=700, height=15, width=100)
        self.__nameJoLabel.place(x=130, y=700, height=15, width=70)
        
        self.__riemannFuncLabel.place(x=60, y=15, height=30, width=200)
        self.__riemannYLabel.place(x=15, y=15, height=30, width=80)
        self.__funcLabel.place(x=15, y=10)
        self.__funcDynLabel.place(x=15, y=40)
        self.__riemannResultL.place(x=15, y=155, height=30, width=400)
        self.__leftBoundL.place(x=290, y=15, height=30, width=100)
        self.__rightBoundL.place(x=270, y=50, height=30, width=130)
        self.__intervalL.place(x=300, y=85, height=30, width=100)
        self.__numRectanglesL.place(x=15, y=50, height=30, width=300)
        self.__typeL.place(x=15, y=85, height=30, width=300)
        self.__tableLabel.place(x=60, y=70)

        # placing entry boxes
        self.__leftBoundE.place(x=410, y=15, height=30, width=90)
        self.__rightBoundE.place(x=410, y=50, height=30, width=90)
        self.__intervalE.place(x=410, y=85, height=30, width=90)
        self.__numRectanglesE.place(x=315, y=50, height=30, width=90)
        self.__typeE.place(x=315, y=85, height=30, width=90)

        # placing mainframe
        self.__mainFrame.place(x=0, y=0, height=735, width=555)

        # setting default window size
        self.__mainProgram.geometry("{}x{}".format(555, 735))
        self.__mainProgram.resizable(width=FALSE, height=FALSE)

        # Figure and subplot for matplotlab - updated everytime
        #     __graph() is called
        self.__f = Figure(figsize=(5,5), dpi = 100)
        self.__a = self.__f.add_subplot(111)

        # Makes sure general calculation frame appears first
        self.__displayF.lift()
        
        mainloop()

    def __update(self, item):
        if self.__enteringFunction:
            newInput = self.__inputFuncVar.get() + item
            self.__inputFuncVar.set(newInput)
        if not self.__enteringFunction or self.__enteringRiemann:
            newInput = self.__inputVar.get() + item
            self.__inputVar.set(newInput)

    def __clear(self):
        if self.__enteringFunction:
            self.__inputFuncVar.set("")
            self.__tableText.set("")
        if not self.__enteringFunction or self.__enteringRiemann:
            self.__inputVar.set("")
            self.__userInputLog.set("")
            self.__userOutputLog.set("")

    def __quit(self):
        if self.__enteringFunction:
            self.__enteringFunction = False
            self.__displayF.lift()
        elif self.__enteringRiemann:
            self.__enteringRiemann = False
            self.__displayF.lift()
        else:
            self.__mainProgram.quit()

    def __del(self):
        if self.__enteringFunction:
            inputLen = len(self.__inputFuncVar.get())
            newInput = self.__inputFuncVar.get()[:inputLen-1]
            self.__inputFuncVar.set(newInput)
        if not self.__enteringFunction or self.__enteringRiemann:
            inputLen = len(self.__inputVar.get())
            newInput = self.__inputVar.get()[:inputLen-1]
            self.__inputVar.set(newInput)

    def __answer(self):
        newInput = self.__inputVar.get() + self.__ans
        self.__inputVar.set(newInput)

    def __calculate(self, processFunc):
        function = ProcessFun(processFunc).process()
        if not self.__enteringFunction or self.__enteringRiemann:
            try:
                if not "integrate" in function or "derivative" in function:
                    function += "+0*X"
                    X = 10
                evalOutput = eval(function)
                if str(evalOutput)[0] == "(":
                    output = float(evalOutput[0])
                else:
                    output = evalOutput
                if output > 9999999999 or output < -9999999999:
                    self.__outputVar.set("ERROR - Overload")
                elif output < 0.00000001 and output > -0.00000001:
                    self.__outputVar.set("0")
                    self.__ans = '0'
                elif str(output) == "nan":
                    self.__outputVar.set("ERROR")
                elif int(output) != 0 and output % int(output) == 0:
                    output = int(output)
                    self.__outputVar.set(str(output))
                    self.__ans = str(output)
                else:
                    self.__outputVar.set(str(output))
                    self.__ans = str(output)
            except:
                self.__outputVar.set("ERROR")
            newInput = (self.__userInputLog.get() + "\n" + processFunc)
            self.__userInputLog.set(newInput)
            newInput = (self.__userOutputLog.get() + "\n" +
                        self.__outputVar.get())
            self.__userOutputLog.set(newInput)
            self.__inputVar.set("")
            self.__outputVar.set("")

    def __userEnterFunction(self):
        self.__enteringFunction = True
        self.__enteringRiemann = False
        self.__enterFuncF.lift()

    def __userEnterRiemann(self):
        self.__enteringRiemann = True
        self.__enteringFunction = False
        self.__riemannF.lift()

    def __updateGraph(self, processFunc):
        function = ProcessFun(processFunc).process()
        X = np.arange(-10, 10, np.pi/24)
        if function != "":
            y = eval(function)
            self.__a.clear()
            self.__a.plot(X, y)
            pyplot.xlabel("x")
            pyplot.ylabel("y")
            self.__a.grid(True)

    def __table(self, processFunc):
        function = ProcessFun(processFunc).process()
        self.__tableText.set("")
        X = np.arange(float(self.__leftBoundE.get()),
                float(self.__rightBoundE.get()) +
                float(self.__intervalE.get()), float(self.__intervalE.get()))
        y = eval(function)
        xList = []
        yList = []
        for i in X:
            xList.append(str(round(i, 3)))
        for i in y:
            yList.append(str(round(i, 3)))
        titleXY = self.__tableText.get() + ("X\tY\n-----------------")
        self.__tableText.set(titleXY)
        for i in range(5):
            self.__tableText
            increment = self.__tableText.get() + ("\n"+str(xList[i])+"\t"+
                                                  str(yList[i]))
            self.__tableText.set(increment)

    def __riemann(self, processFunc):
        function = ProcessFun(processFunc).process()
        try:
            rightR = float(self.__rightBoundE.get())
            leftR = float(self.__leftBoundE.get())
            numRecR = int(self.__numRectanglesE.get())
            typeR = self.__typeE.get().lower()
            interval = ((rightR-leftR) / numRecR)
            conditions = [leftR, rightR, numRecR, interval, typeR, function]
            riemannI = RiemannSums(conditions)
            if typeR == "left":
                riemannAnsTemp = (format(riemannI.leftRiemann(), ".8f")\
                                  .rstrip("0").rstrip("."))
                self.__riemannAns.set(riemannAnsTemp)
            elif typeR == "right":
                riemannAnsTemp = (format(riemannI.rightRiemann(), ".8f")\
                                  .rstrip("0").rstrip("."))
            elif typeR == "trapezoidal":
                riemannAnsTemp = (format(((riemannI.leftRiemann() +
                                           riemannI.rightRiemann()) / 2),
                                         ".8f").rstrip("0").rstrip("."))
                self.__riemannAns.set(riemannAnsTemp)
            elif typeR == "midpoint":
                riemannAnsTemp = (format(riemannI.midRiemann(), ".8f")\
                                  .rstrip("0").rstrip("."))
                self.__riemannAns.set(riemannAnsTemp)
            else:
                self.__riemannAns.set("ERROR")
        except:
            self.__riemannAns.set("ERROR")

    def __graph(self, processFunc):
        function = ProcessFun(processFunc).process()
        self.__a.clear()
        X = np.arange(float(self.__leftBoundE.get()),
            float(self.__rightBoundE.get()), np.pi/24)
        y = eval(function)
        self.__a.plot(X, y)
        pyplot.xlabel("x")
        pyplot.ylabel("y")
        self.__a.grid(True)
        canvas = FigureCanvasQTAgg(self.__f)
        canvas.show()
