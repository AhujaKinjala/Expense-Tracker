from tkinter import *
root=Tk()
root.state("zoomed")
root.title("Expense Tracker-TDK")
root.configure(bg="white")

class withoutlog:
    def __init__(self,root):
        self.label_frame = LabelFrame(root, text='Welcome to Expense Tracker-TDK!!',height=300,width=500,background='#E0FFFD',padx=10,font=("inter",14,"bold"),fg="#1D79A0")
        self.label_frame.place(x=30,y=10)
        self.frame2=Frame(root,height=450,width=500,background="green")
        self.frame2.place(x=30,y=335)
        self.frame3=Frame(root,height=300,width=900,background="purple")
        self.frame3.place(x=600,y=10)
        self.frame4=Frame(root,height=450,width=900,background="#D9F8FF")
        self.frame4.place(x=600,y=335)
        self.add_button()
    def add_button(self):
        self.addb=Button(self.frame4,width=10,background="#1D79A0",fg="white",text="Add",font=("Times New Roman",20,"bold"),command=self.toplvl1)
        self.addb.place(x=10,y=385)
        self.label5=Label(self.label_frame,text='Login',font=("Times New Roman",24,"bold"),fg="#1D79A0",bg="#E0FFFD")
        self.label5.place(x=175,y=40)
        self.username=Entry(self.label_frame,width=30,bg='white',borderwidth=2, relief="solid")
        self.username.focus_set()
        self.username.place(x=225,y=105)
        self.pwd = Entry(self.label_frame, width=30, bg='white', borderwidth=2, relief="solid",show="*")
        self.pwd.place(x=225, y=155)
        self.labelu = Label(self.label_frame, text='Username :', font=("Times New Roman", 18, "bold"), fg="#1D79A0",bg="#E0FFFD")
        self.labelu.place(x=75, y=100)
        self.labelp = Label(self.label_frame, text='Password :', font=("Times New Roman", 18, "bold"), fg="#1D79A0", bg="#E0FFFD")
        self.labelp.place(x=75, y=150)
        self.logb=Button(self.label_frame,text="LogIn",bg="#1D79A0",fg="white",font=("Times New Roman",14,"bold"),padx=10)
        self.logb.place(x=380,y=200)
        self.resetb = Button(self.label_frame, text="Reset", bg="#1D79A0", fg="white",font=("Times New Roman", 14, "bold"), padx=10,command=self.clear)
        self.resetb.place(x=280, y=200)
        self.regb = Button(self.label_frame, text="Register", bg="#1D79A0", fg="white",font=("Times New Roman", 14, "bold"), padx=10,command=self.regform)
        self.regb.place(x=10, y=200)
        self.balance=Label(self.frame4,height=2,text="Balance : Rs. 0/-",font=("Times New Roman",18,"bold"),fg="#1D79A0",bg="white",borderwidth=2, relief="solid")
        self.balance.place(x=10,y=2)
        self.goal=Label(self.frame4,height=2,width=6,text="Goal:",font=("Times New Roman",18,"bold"),fg="#1D79A0",bg="#F4FAFC",borderwidth=2, relief="solid")
        self.goal.place(x=650,y=2)
        self.egoal = Entry(self.frame4,  width=6, font=("Arial", 32, "bold"),fg="black", bg="#F4FAFC", borderwidth=2, relief="solid")
        self.egoal.place(x=750, y=2)

    def regform(self):
        self.top2 = Toplevel(root)
        #self.top1.configure(bg="white")
        self.top2.title("Registration")
        self.top2.geometry("600x600")

        self.pf=Frame(self.top2,height=200,width=200,bg="#E0FFFD")
        self.pf.pack(expand=1,fill=BOTH)

        self.regf=Label(self.pf,text="Registration Form",font=("Times New Roman", 22, "bold underline"),bg="#E0FFFD")
        self.regf.grid(row=0,column=0,sticky='w')

        self.name=Label( self.pf,text='Name :', font=("Times New Roman", 20, "bold"), fg="black",bg="#E0FFFD")
        self.name.grid(row=1,column=0,pady=10,sticky='e')

        self.usname = Label(self.pf, text='Username :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.usname.grid(row=2, column=0, pady=10, sticky='e')

        self.mexp = Label(self.pf, text='Monthly Expense :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.mexp.grid(row=3, column=0, pady=10, sticky='e')

        self.maxexp = Label(self.pf, text='Maximum Monthly Expense :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.maxexp.grid(row=4, column=0, pady=10, sticky='e')

        self.email = Label(self.pf, text='Email :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.email.grid(row=5, column=0, pady=10, sticky='e')

        self.passw = Label(self.pf, text='Password :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.passw.grid(row=6, column=0, pady=10, sticky='e')

        self.cpassw = Label(self.pf, text='Confirm Password :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.cpassw.grid(row=7, column=0, pady=10, sticky='e')

        self.ename = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",borderwidth=2,relief="solid")
        self.ename.grid(row=1, column=1, pady=6, sticky='w')

        self.eusname = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        self.eusname.grid(row=2, column=1, pady=6, sticky='w')

        self.emexp = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        self.emexp.grid(row=3, column=1, pady=6, sticky='w')

        self.emaxexp = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        self.emaxexp.grid(row=4, column=1, pady=6, sticky='w')

        self.eemail =Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        self.eemail.grid(row=5, column=1, pady=6, sticky='w')

        self.epassw = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2,show="*")
        self.epassw.grid(row=6, column=1, pady=6, sticky='w')

        self.ecpassw = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2,show="*")
        self.ecpassw.grid(row=7, column=1, pady=6, sticky='w')

        self.submit=Button(self.pf,text="Submit",font=("Times New Roman",18,'bold'),fg='white',bg='#1D79A0')
        self.submit.grid(row=8,column=0,columnspan=2,rowspan=2,sticky='e',pady=15)







        self.top2.mainloop()



    def toplvl1(self):
        self.top1=Toplevel(root)
        self.top1.configure(bg="white")
        self.top1.title("Add your expense")
        self.top1.geometry("600x400")
        self.desc=Label(self.top1,background="white",text="Description :",fg="#1D79A0",font=("inter",20,"bold"))
        self.desc.place(x=45,y=80)
        self.dlabel=Entry(self.top1,width=40,fg='black',bg='white',borderwidth=2, relief="solid")
        self.dlabel.place(x=235,y=90)
        self.amt = Label(self.top1, background="white", text="Amount :", fg="#1D79A0", font=("inter", 20, "bold"))
        self.amt.place(x=45, y=150)
        self.alabel = Entry(self.top1, width=40, fg='black', bg='white', borderwidth=2, relief="solid")
        self.alabel.place(x=235, y=160)
        self.done=Button(self.top1,height=2,width=15,bg='#1D79A0',fg='white',text="Done",font=("Times New Roman",10,"bold"))
        self.done.place(x=265,y=225)
        self.top1.mainloop()

    def clear(self):
        self.username.delete(0, END)
        self.pwd.delete(0, END)
        self.username.focus_set()

c=withoutlog(root)
root.mainloop()