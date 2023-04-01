from tkinter import *
root=Tk()
root.state("zoomed")
root.title("Expense Tracker-TDK")
root.configure(bg="white")

class log:
    def __init__(self,root):
        self.frame=Frame(root,height=300,width=500,background='yellow',padx=10)
        self.frame.place(x=30,y=10)
        self.frame2=Frame(root,height=450,width=500,background="green")
        self.frame2.place(x=30,y=335)
        self.frame3=Frame(root,height=300,width=900,background="purple")
        self.frame3.place(x=600,y=10)
        self.frame4=Frame(root,height=450,width=900,background="lightblue")
        self.frame4.place(x=600,y=335)
c=log(root)
root.mainloop()