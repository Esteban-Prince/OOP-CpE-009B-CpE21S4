from tkinter import *

class MyWindow:
    def __init__(self, win):
        #common widgets
        win.configure(bg="lightblue")
        self.Label1 = Label(win, fg = "Red", text = "Calculator", font=("Times New Roman", 20, "bold"), bg="lightblue")
        self.Label1.place(x = 140, y = 20)
        self.Label2 = Label(win, text = "Number 1:")
        self.Label2.place(x = 50, y = 80)
        self.Entry1 = Entry(win, bd = 2)
        self.Entry1.place(x = 150, y = 80)
        self.Label3 = Label(win, text = "Number 2:")
        self.Label3.place(x = 50, y = 120)
        self.Entry2 = Entry(win, bd = 2)
        self.Entry2.place(x = 150, y = 120)
        self.Label4 = Label(win, text = "Result:")
        self.Label4.place(x = 50, y = 160)
        self.Entry3 = Entry(win, bd = 2)
        self.Entry3.place(x = 150, y = 160)

        self.Button1 = Button(win, fg = "Blue", text = "Add")
        self.Button1.place(x = 50, y = 200)
        self.Button2 = Button(win, fg = "Red", text = "Subtract")
        self.Button2.place(x = 100, y= 200)
        self.Button3 = Button(win, fg = "Green", text = "Multiply")
        self.Button3.place(x = 170, y = 200)
        self.Button4 = Button(win, fg = "Orange", text = "Divide")
        self.Button4.place(x = 245, y= 200)

        self.Button1.bind('<Button-1>', self.add)
        self.Button2.bind('<Button-1>', self.sub)
        self.Button3.bind('<Button-1>', self.multiply)
        self.Button4.bind('<Button-1>', self.divide)

    def add(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multiply(self, win):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def divide(self, win):
        try:
            self.Entry3.delete(0, 'end')
            num1 = int(self.Entry1.get())
            num2 = int(self.Entry2.get())
            result = (num1) / (num2)
            self.Entry3.insert(END, str(result))
        except Error:
            result = "Error: Division by Zero"
            self.Entry3.insert(END, str(result))

window = Tk()
MywWin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()