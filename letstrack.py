from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.state("zoomed")
root.title("Expense Tracker-TDK")

class fpage:
    def __init__(self,root):
        self.frame=Frame(root)
        self.frame.pack(expand=1,fill=BOTH)

        self.img=Image.open("minip1.jpg").resize((1550,800))
        self.mini1=ImageTk.PhotoImage(self.img)
        self.label1=Label(self.frame,image=self.mini1)
        self.label1.pack(expand=1,fill=BOTH)
        self.let=Button(self.label1,height=2,width=30,bg='#1D79A0',fg='white',text="Let's Track",font=("Times New Roman",10,"bold"))
        self.let.place(x=700,y=550)
        self.label2=Label(self.label1,text="Expense",font=("Inter",70,"bold"),bg="white",fg="#1D79A0")
        self.label2.place(x=635,y=225)
        self.label3 = Label(self.label1, text="Tracker", font=("Inter", 70, "bold"), bg="white", fg="#1D79A0")
        self.label3.place(x=650, y=325)
        self.pig=Image.open("piggy.png").resize((150,150))
        self.pigtk=ImageTk.PhotoImage(self.pig)
        self.label4=Label(self.label1,height=100,width=100,image=self.pigtk,bg="white")
        self.label4.place(x=780,y=430)
        self.frame.pack_propagate(0)
c=fpage(root)
root.mainloop()