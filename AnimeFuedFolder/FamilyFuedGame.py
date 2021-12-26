try:
    import tkinter as tk                # python 3
    from playsound import playsound
    from tkinter import font as tkfont  # python 3
    from tkinter import ttk
    from tkinter.messagebox import showinfo
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["RoundOneStart"] = RoundOneStart(parent=container, controller=self)
        self.frames["RoundOneInput"] = RoundOneInput(parent=container, controller=self)
        self.frames["RoundOneOutput"] = RoundOneOutput(parent=container, controller=self)
        self.frames["RoundTwoStart"] = RoundTwoStart(parent=container, controller=self)
        self.frames["RoundTwoInput"] = RoundTwoInput(parent=container, controller=self)
        self.frames["RoundTwoOutput"] = RoundTwoOutput(parent=container, controller=self)
        self.frames["RoundThreeStart"] = RoundThreeStart(parent=container, controller=self)
        self.frames["RoundThreeInput"] = RoundThreeInput(parent=container, controller=self)
        self.frames["RoundThreeOutput"] = RoundThreeOutput(parent=container, controller=self)
        self.frames["RoundOnePoints"] = RoundOnePoints(parent=container, controller=self)
        self.frames["RoundTwoPoints"] = RoundTwoPoints(parent=container, controller=self)
        self.frames["RoundThreePoints"] = RoundThreePoints(parent=container, controller=self)

        
        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundOneStart"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundOneInput"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundOneOutput"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundTwoStart"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundTwoInput"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundTwoOutput"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundThreeStart"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundThreeInput"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundThreeOutput"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundOnePoints"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundTwoPoints"].grid(row=0, column=0, sticky="nsew")
        self.frames["RoundThreePoints"].grid(row=0, column=0, sticky="nsew")

                
        self.show_frame("StartPage")
        

    
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def changeText(self, butHolder, varHolder):
        butHolder.configure(textvariable = varHolder)

    def resetButton(self, butHolderTwo, varHolderTwo):
        butHolderTwo.configure(textvariable = varHolderTwo)

        

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Round One ",
                            command=lambda: controller.show_frame("RoundOneStart"),
                            width=50,
                            height=10)
        button2 = tk.Button(self, text="Go to Round Two",
                            command=lambda: controller.show_frame("RoundTwoStart"),
                            width=50,
                            height=10)
        button3 = tk.Button(self, text="Go to Round Three",
                            command=lambda: controller.show_frame("RoundThreeStart"),
                            width=50,
                            height=10)
        button1.pack()
        button2.pack()
        button3.pack()

class RoundOneStart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round One's Start Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button4 = tk.Button(self, text="Go to Round One's Point Selection",
                            command=lambda: controller.show_frame("RoundOnePoints"),
                            width=50,
                            height=10)
        
        button1 = tk.Button(self, text="Go to Round One's Input",
                            command=lambda: controller.show_frame("RoundOneInput"),
                            width=50,
                            height=10)
        button2 = tk.Button(self, text="Go to Round One's Output",
                            command=lambda: controller.show_frame("RoundOneOutput"),
                            width=50,
                            height=10)
        button3 = tk.Button(self, text="Go back to Start ",
                            command=lambda: controller.show_frame("StartPage"),
                            width=50,
                            height=10)
        button4.pack()
        button1.pack()
        button2.pack()
        button3.pack()

class RoundTwoStart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round Two's Start Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button4 = tk.Button(self, text="Go to Round Two's Point Selection",
                            command=lambda: controller.show_frame("RoundTwoPoints"),
                            width=50,
                            height=10)

        button1 = tk.Button(self, text="Go to Round Two's Input",
                            command=lambda: controller.show_frame("RoundTwoInput"),
                            width=50,
                            height=10)
        button2 = tk.Button(self, text="Go to Round Two's Output",
                            command=lambda: controller.show_frame("RoundTwoOutput"),
                            width=50,
                            height=10)
        button3 = tk.Button(self, text="Go back to Start ",
                            command=lambda: controller.show_frame("StartPage"),
                            width=50,
                            height=10)
        button4.pack()
        button1.pack()
        button2.pack()
        button3.pack()

class RoundThreeStart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round Three's Start Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button4 = tk.Button(self, text="Go to Round Three's Point Selection",
                            command=lambda: controller.show_frame("RoundThreePoints"),
                            width=50,
                            height=10)
        button1 = tk.Button(self, text="Go to Round Three's Input",
                            command=lambda: controller.show_frame("RoundThreeInput"),
                            width=50,
                            height=10)
        button2 = tk.Button(self, text="Go to Round Three's Output",
                            command=lambda: controller.show_frame("RoundThreeOutput"),
                            width=50,
                            height=10)
        button3 = tk.Button(self, text="Go back to Start ",
                            command=lambda: controller.show_frame("StartPage"),
                            width=50,
                            height=10)
        button4.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        
class RoundOnePoints(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round One's Points Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Go to Round One's Start",
                            command=lambda: controller.show_frame("RoundOneStart"),
                            width=50,
                            height=10)

        button1.pack()

        
        label2 = tk.Label(self, text = "Enter in the Point Values for each Answer (1 - 8)")
        label2.pack()
        e1 = tk.Entry(self, textvariable = RoundOneAnswerOnePoints)
        e1.pack()
        e2 = tk.Entry(self, textvariable = RoundOneAnswerTwoPoints)
        e2.pack()
        e3 = tk.Entry(self, textvariable = RoundOneAnswerThreePoints)
        e3.pack()
        e4 = tk.Entry(self, textvariable = RoundOneAnswerFourPoints)
        e4.pack()
        e5 = tk.Entry(self, textvariable = RoundOneAnswerFivePoints)
        e5.pack()
        e6 = tk.Entry(self, textvariable = RoundOneAnswerSixPoints)
        e6.pack()
        e7 = tk.Entry(self, textvariable = RoundOneAnswerSevenPoints)
        e7.pack()
        e8 = tk.Entry(self, textvariable = RoundOneAnswerEigthPoints)
        e8.pack()

class RoundTwoPoints(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round Two's Points Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Go to Round Two's Start",
                            command=lambda: controller.show_frame("RoundTwoStart"),
                            width=50,
                            height=10)

        button1.pack()


        
        label2 = tk.Label(self, text = "Enter in the Point Values for each Answer (1 - 8)")
        label2.pack()
        e1 = tk.Entry(self, textvariable = RoundTwoAnswerOnePoints)
        e1.pack()
        e2 = tk.Entry(self, textvariable = RoundTwoAnswerTwoPoints)
        e2.pack()
        e3 = tk.Entry(self, textvariable = RoundTwoAnswerThreePoints)
        e3.pack()
        e4 = tk.Entry(self, textvariable = RoundTwoAnswerFourPoints)
        e4.pack()
        e5 = tk.Entry(self, textvariable = RoundTwoAnswerFivePoints)
        e5.pack()
        e6 = tk.Entry(self, textvariable = RoundTwoAnswerSixPoints)
        e6.pack()
        e7 = tk.Entry(self, textvariable = RoundTwoAnswerSevenPoints)
        e7.pack()
        e8 = tk.Entry(self, textvariable = RoundTwoAnswerEigthPoints)
        e8.pack()

class RoundThreePoints(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round Three's Points Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Go to Round Three's Start",
                            command=lambda: controller.show_frame("RoundThreeStart"),
                            width=50,
                            height=10)

        button1.pack()


        
        label2 = tk.Label(self, text = "Enter in the Point Values for each Answer (1 - 8)")
        label2.pack()
        e1 = tk.Entry(self, textvariable = RoundThreeAnswerOnePoints)
        e1.pack()
        e2 = tk.Entry(self, textvariable = RoundThreeAnswerTwoPoints)
        e2.pack()
        e3 = tk.Entry(self, textvariable = RoundThreeAnswerThreePoints)
        e3.pack()
        e4 = tk.Entry(self, textvariable = RoundThreeAnswerFourPoints)
        e4.pack()
        e5 = tk.Entry(self, textvariable = RoundThreeAnswerFivePoints)
        e5.pack()
        e6 = tk.Entry(self, textvariable = RoundThreeAnswerSixPoints)
        e6.pack()
        e7 = tk.Entry(self, textvariable = RoundThreeAnswerSevenPoints)
        e7.pack()
        e8 = tk.Entry(self, textvariable = RoundThreeAnswerEigthPoints)
        e8.pack()
        
class RoundOneInput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the First Round's Input", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"),
                           width=50,
                           height=10)
        button.pack()
        button1 = tk.Button(self, text="Go to Round One's Start ",
                            command=lambda: controller.show_frame("RoundOneStart"),
                            width=50,
                            height=10)
        button1.pack()


        global RoundOneAnswerOnePoints
        RoundOneAnswerOnePoints = tk.StringVar()
        global RoundOneAnswerTwoPoints
        RoundOneAnswerTwoPoints = tk.StringVar()
        global RoundOneAnswerThreePoints
        RoundOneAnswerThreePoints = tk.StringVar()
        global RoundOneAnswerFourPoints
        RoundOneAnswerFourPoints = tk.StringVar()
        global RoundOneAnswerFivePoints
        RoundOneAnswerFivePoints = tk.StringVar()
        global RoundOneAnswerSixPoints
        RoundOneAnswerSixPoints = tk.StringVar()
        global RoundOneAnswerSevenPoints
        RoundOneAnswerSevenPoints = tk.StringVar()
        global RoundOneAnswerEigthPoints
        RoundOneAnswerEigthPoints = tk.StringVar()
        
        global RoundOneAnswerOne
        RoundOneAnswerOne = tk.StringVar()
        global RoundOneAnswerTwo
        RoundOneAnswerTwo = tk.StringVar()
        global RoundOneAnswerThree
        RoundOneAnswerThree = tk.StringVar()
        global RoundOneAnswerFour
        RoundOneAnswerFour = tk.StringVar()
        global RoundOneAnswerFive
        RoundOneAnswerFive = tk.StringVar()
        global RoundOneAnswerSix
        RoundOneAnswerSix = tk.StringVar()
        global RoundOneAnswerSeven
        RoundOneAnswerSeven = tk.StringVar()
        global RoundOneAnswerEigth
        RoundOneAnswerEigth = tk.StringVar()
        
        label2 = tk.Label(self, text = "Enter in the answers", font=controller.title_font)
        label2.pack()
        e1 = tk.Entry(self, textvariable = RoundOneAnswerOne,
                      width=50)
        e1.pack()
        e2 = tk.Entry(self, textvariable = RoundOneAnswerTwo,
                      width=50)
        e2.pack()
        e3 = tk.Entry(self, textvariable = RoundOneAnswerThree,
                      width=50)
        e3.pack()
        e4 = tk.Entry(self, textvariable = RoundOneAnswerFour,
                      width=50)
        e4.pack()
        e5 = tk.Entry(self, textvariable = RoundOneAnswerFive,
                      width=50)
        e5.pack()
        e6 = tk.Entry(self, textvariable = RoundOneAnswerSix,
                      width=50)
        e6.pack()
        e7 = tk.Entry(self, textvariable = RoundOneAnswerSeven,
                      width=50)
        e7.pack()
        e8 = tk.Entry(self, textvariable = RoundOneAnswerEigth,
                      width=50)
        e8.pack()

class RoundTwoInput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Second Round's Input", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"),
                           width=30,
                           height=10)
        button.pack()

        button1 = tk.Button(self, text="Go to Round Two's Start ",
                            command=lambda: controller.show_frame("RoundTwoStart"),
                            width=30,
                            height=10)
        button1.pack()


        global RoundTwoAnswerOnePoints
        RoundTwoAnswerOnePoints = tk.StringVar()
        global RoundTwoAnswerTwoPoints
        RoundTwoAnswerTwoPoints = tk.StringVar()
        global RoundTwoAnswerThreePoints
        RoundTwoAnswerThreePoints = tk.StringVar()
        global RoundTwoAnswerFourPoints
        RoundTwoAnswerFourPoints = tk.StringVar()
        global RoundTwoAnswerFivePoints
        RoundTwoAnswerFivePoints = tk.StringVar()
        global RoundTwoAnswerSixPoints
        RoundTwoAnswerSixPoints = tk.StringVar()
        global RoundTwoAnswerSevenPoints
        RoundTwoAnswerSevenPoints = tk.StringVar()
        global RoundTwoAnswerEigthPoints
        RoundTwoAnswerEigthPoints = tk.StringVar()

        
        global RoundTwoAnswerOne
        RoundTwoAnswerOne = tk.StringVar()
        global RoundTwoAnswerTwo
        RoundTwoAnswerTwo = tk.StringVar()
        global RoundTwoAnswerThree
        RoundTwoAnswerThree = tk.StringVar()
        global RoundTwoAnswerFour
        RoundTwoAnswerFour = tk.StringVar()
        global RoundTwoAnswerFive
        RoundTwoAnswerFive = tk.StringVar()
        global RoundTwoAnswerSix
        RoundTwoAnswerSix = tk.StringVar()
        global RoundTwoAnswerSeven
        RoundTwoAnswerSeven = tk.StringVar()
        global RoundTwoAnswerEigth
        RoundTwoAnswerEigth = tk.StringVar()
        
        label2 = tk.Label(self, text = "Enter in the answers", font=controller.title_font)
        label2.pack()
        e1 = tk.Entry(self, textvariable = RoundTwoAnswerOne,
                      width=50)
        e1.pack()
        e2 = tk.Entry(self, textvariable = RoundTwoAnswerTwo,
                      width=50)
        e2.pack()
        e3 = tk.Entry(self, textvariable = RoundTwoAnswerThree,
                      width=50)
        e3.pack()
        e4 = tk.Entry(self, textvariable = RoundTwoAnswerFour,
                      width=50)
        e4.pack()
        e5 = tk.Entry(self, textvariable = RoundTwoAnswerFive,
                      width=50)
        e5.pack()
        e6 = tk.Entry(self, textvariable = RoundTwoAnswerSix,
                      width=50)
        e6.pack()
        e7 = tk.Entry(self, textvariable = RoundTwoAnswerSeven,
                      width=50)
        e7.pack()
        e8 = tk.Entry(self, textvariable = RoundTwoAnswerEigth,
                      width=50)
        e8.pack()

class RoundThreeInput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Third Round's Input", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"),
                           width=30,
                           height=10)
        button.pack()

        button1 = tk.Button(self, text="Go to Round Three's Start ",
                            command=lambda: controller.show_frame("RoundThreeStart"),
                            width=30,
                            height=10)
        button1.pack()


        global RoundThreeAnswerOnePoints
        RoundThreeAnswerOnePoints = tk.StringVar()
        global RoundThreeAnswerTwoPoints
        RoundThreeAnswerTwoPoints = tk.StringVar()
        global RoundThreeAnswerThreePoints
        RoundThreeAnswerThreePoints = tk.StringVar()
        global RoundThreeAnswerFourPoints
        RoundThreeAnswerFourPoints = tk.StringVar()
        global RoundThreeAnswerFivePoints
        RoundThreeAnswerFivePoints = tk.StringVar()
        global RoundThreeAnswerSixPoints
        RoundThreeAnswerSixPoints = tk.StringVar()
        global RoundThreeAnswerSevenPoints
        RoundThreeAnswerSevenPoints = tk.StringVar()
        global RoundThreeAnswerEigthPoints
        RoundThreeAnswerEigthPoints = tk.StringVar()

        
        global RoundThreeAnswerOne
        RoundThreeAnswerOne = tk.StringVar()
        global RoundThreeAnswerTwo
        RoundThreeAnswerTwo = tk.StringVar()
        global RoundThreeAnswerThree
        RoundThreeAnswerThree = tk.StringVar()
        global RoundThreeAnswerFour
        RoundThreeAnswerFour = tk.StringVar()
        global RoundThreeAnswerFive
        RoundThreeAnswerFive = tk.StringVar()
        global RoundThreeAnswerSix
        RoundThreeAnswerSix = tk.StringVar()
        global RoundThreeAnswerSeven
        RoundThreeAnswerSeven = tk.StringVar()
        global RoundThreeAnswerEigth
        RoundThreeAnswerEigth = tk.StringVar()
        
        label2 = tk.Label(self, text = "Enter in the answers", font=controller.title_font)
        label2.pack()
        e1 = tk.Entry(self, textvariable = RoundThreeAnswerOne,
                      width=50)
        e1.pack()
        e2 = tk.Entry(self, textvariable = RoundThreeAnswerTwo,
                      width=50)
        e2.pack()
        e3 = tk.Entry(self, textvariable = RoundThreeAnswerThree,
                      width=50)
        e3.pack()
        e4 = tk.Entry(self, textvariable = RoundThreeAnswerFour,
                      width=50)
        e4.pack()
        e5 = tk.Entry(self, textvariable = RoundThreeAnswerFive,
                      width=50)
        e5.pack()
        e6 = tk.Entry(self, textvariable = RoundThreeAnswerSix,
                      width=50)
        e6.pack()
        e7 = tk.Entry(self, textvariable = RoundThreeAnswerSeven,
                      width=50)
        e7.pack()
        e8 = tk.Entry(self, textvariable = RoundThreeAnswerEigth,
                      width=50)
        e8.pack()


class RoundOneOutput(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round One's Output ", font=controller.title_font)
        label.place(x=800, y=0)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"),
                           width=20,
                           height=5)
        button.place(x=750, y=900)

        button1 = tk.Button(self, text="Go to Round One's Start ",
                            command=lambda: controller.show_frame("RoundOneStart"),
                            width=20,
                            height=5)
        button1.place(x=1000, y=900)

        buttonResetRoundOne = tk.Button(self, text="Reset Answers to Points ",
                            command=lambda: [controller.resetButton(b1, RoundOneAnswerOnePoints), controller.resetButton(b2, RoundOneAnswerTwoPoints), controller.resetButton(b3, RoundOneAnswerThreePoints), controller.resetButton(b4, RoundOneAnswerFourPoints), controller.resetButton(b5, RoundOneAnswerFivePoints), controller.resetButton(b6, RoundOneAnswerSixPoints), controller.resetButton(b7, RoundOneAnswerSevenPoints), controller.resetButton(b8, RoundOneAnswerEigthPoints)],
                            width=20,
                            height=5)
        buttonResetRoundOne.place(x=500, y=900)
        
        b1 = tk.Button(self, textvariable = RoundOneAnswerOnePoints,
                       command=lambda: [controller.changeText(b1, RoundOneAnswerOne), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b1.place(x=550, y=100)
        b2 = tk.Button(self, textvariable = RoundOneAnswerTwoPoints,
                       command=lambda: [controller.changeText(b2, RoundOneAnswerTwo), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b2.place(x=550, y=300)
        b3 = tk.Button(self, textvariable = RoundOneAnswerThreePoints,
                       command=lambda: [controller.changeText(b3, RoundOneAnswerThree), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b3.place(x=550, y=500)
        b4 = tk.Button(self, textvariable = RoundOneAnswerFourPoints,
                       command=lambda: [controller.changeText(b4, RoundOneAnswerFour), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b4.place(x=550, y=700)
        b5 = tk.Button(self, textvariable = RoundOneAnswerFivePoints,
                       command=lambda: [controller.changeText(b5, RoundOneAnswerFive), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b5.place(x=1000, y=100)
        b6 = tk.Button(self, textvariable = RoundOneAnswerSixPoints,
                       command=lambda: [controller.changeText(b6, RoundOneAnswerSix), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b6.place(x=1000, y=300)
        b7 = tk.Button(self, textvariable = RoundOneAnswerSevenPoints,
                       command=lambda: [controller.changeText(b7, RoundOneAnswerSeven), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b7.place(x=1000, y=500)
        b8 = tk.Button(self, textvariable = RoundOneAnswerEigthPoints,
                       command=lambda: [controller.changeText(b8, RoundOneAnswerEigth), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b8.place(x=1000, y=700)
        

class RoundTwoOutput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round Two's Output ", font=controller.title_font)
        label.place(x=800, y=0)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"),
                           width=20,
                           height=5)
        button.place(x=750, y=900)

        button1 = tk.Button(self, text="Go to Round Two's Start ",
                            command=lambda: controller.show_frame("RoundTwoStart"),
                            width=20,
                            height=5)
        button1.place(x=1000, y=900)

        buttonResetRoundTwo = tk.Button(self, text="Reset Answers to Points ",
                            command=lambda: [controller.resetButton(b1, RoundTwoAnswerOnePoints), controller.resetButton(b2, RoundTwoAnswerTwoPoints), controller.resetButton(b3, RoundTwoAnswerThreePoints), controller.resetButton(b4, RoundTwoAnswerFourPoints), controller.resetButton(b5, RoundTwoAnswerFivePoints), controller.resetButton(b6, RoundTwoAnswerSixPoints), controller.resetButton(b7, RoundTwoAnswerSevenPoints), controller.resetButton(b8, RoundTwoAnswerEigthPoints)],
                            width=20,
                            height=5)
        buttonResetRoundTwo.place(x=500, y=900)
        
        b1 = tk.Button(self, textvariable = RoundTwoAnswerOnePoints,
                       command=lambda: [controller.changeText(b1, RoundTwoAnswerOne), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b1.place(x=550, y=100)
        b2 = tk.Button(self, textvariable = RoundTwoAnswerTwoPoints,
                       command=lambda: [controller.changeText(b2, RoundTwoAnswerTwo), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b2.place(x=550, y=300)
        b3 = tk.Button(self, textvariable = RoundTwoAnswerThreePoints,
                       command=lambda: [controller.changeText(b3, RoundTwoAnswerThree), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b3.place(x=550, y=500)
        b4 = tk.Button(self, textvariable = RoundTwoAnswerFourPoints,
                       command=lambda: [controller.changeText(b4, RoundTwoAnswerFour), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b4.place(x=550, y=700)
        b5 = tk.Button(self, textvariable = RoundTwoAnswerFivePoints,
                       command=lambda: [controller.changeText(b5, RoundTwoAnswerFive), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b5.place(x=1000, y=100)
        b6 = tk.Button(self, textvariable = RoundTwoAnswerSixPoints,
                       command=lambda: [controller.changeText(b6, RoundTwoAnswerSix), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b6.place(x=1000, y=300)
        b7 = tk.Button(self, textvariable = RoundTwoAnswerSevenPoints,
                       command=lambda: [controller.changeText(b7, RoundTwoAnswerSeven), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b7.place(x=1000, y=500)
        b8 = tk.Button(self, textvariable = RoundTwoAnswerEigthPoints,
                       command=lambda: [controller.changeText(b8, RoundTwoAnswerEigth), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b8.place(x=1000, y=700)

class RoundThreeOutput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Round Three's Output ", font=controller.title_font)
        label.place(x=800, y=0)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"),
                           width=20,
                           height=5)
        button.place(x=750, y=900)
        
        button1 = tk.Button(self, text="Go to Round Three's Start ",
                            command=lambda: controller.show_frame("RoundThreeStart"),
                            width=20,
                            height=5)
        button1.place(x=1000, y=900)

        buttonResetRoundThree = tk.Button(self, text="Reset Answers to Points ",
                            command=lambda: [controller.resetButton(b1, RoundThreeAnswerOnePoints), controller.resetButton(b2, RoundThreeAnswerTwoPoints), controller.resetButton(b3, RoundThreeAnswerThreePoints), controller.resetButton(b4, RoundThreeAnswerFourPoints), controller.resetButton(b5, RoundThreeAnswerFivePoints), controller.resetButton(b6, RoundThreeAnswerSixPoints), controller.resetButton(b7, RoundThreeAnswerSevenPoints), controller.resetButton(b8, RoundThreeAnswerEigthPoints)],
                            width=20,
                            height=5)
        buttonResetRoundThree.place(x=500, y=900)

        b1 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b1, RoundThreeAnswerOne), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b1.place(x=550, y=100)
        b2 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b2, RoundThreeAnswerTwo), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b2.place(x=550, y=300)
        b3 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b3, RoundThreeAnswerThree), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b3.place(x=550, y=500)
        b4 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b4, RoundThreeAnswerFour), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b4.place(x=550, y=700)
        b5 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b5, RoundThreeAnswerFive), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b5.place(x=1000, y=100)
        b6 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b6, RoundThreeAnswerSix), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b6.place(x=1000, y=300)
        b7 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b7, RoundThreeAnswerSeven), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b7.place(x=1000, y=500)
        b8 = tk.Button(self, textvariable = RoundThreeAnswerOnePoints,
                       command=lambda: [controller.changeText(b8, RoundThreeAnswerEigth), playsound('Correct.mp3')],
                       width=60,
                       height=10)
        b8.place(x=1000, y=700)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
