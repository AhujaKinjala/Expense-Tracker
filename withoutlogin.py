from tkinter import *
from tkinter import messagebox
from DBHelper import *
from table import SimpleTable
from letstrack import *
import datetime
from AdminAnalytics import *
class withoutlog:
    def __init__(self,root):
        self.root=root
        self.label_frame = LabelFrame(root, text='Welcome to Expense Tracker-TDK!!',height=300,width=500,background='#E0FFFD',padx=10,font=("inter",14,"bold"),fg="#1D79A0")
        self.label_frame.place(x=30,y=10)
        self.frame2=LabelFrame(root,height=450,width=500,background="#E0FFFD",text="Features",font=("inter",14,"bold"),fg="#1D79A0")
        self.frame2.place(x=30,y=335)
        self.frame3=Frame(root,height=300,width=900,highlightthickness=3,highlightbackground='#1D79A0')
        self.frame3.place(x=600,y=10)
        self.frame4=Frame(root,height=450,width=900,background="#D9F8FF",highlightthickness=3,highlightbackground='#1D79A0')
        self.frame4.place(x=600,y=335)
        self.res={}
        self.add_button()
        root.state("zoomed")
        root.title("Expense Tracker-TDK")
        root.configure(bg="white")
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
        self.raw_image = Image.open("open2.png").resize((20, 22))
        self.img = ImageTk.PhotoImage(self.raw_image)
        self.raw_image2 = Image.open("close.png").resize((20, 22))
        self.img2 = ImageTk.PhotoImage(self.raw_image2)
        self.display3= Button(self.label_frame, image=self.img, command=lambda :self.show(self.pwd,self.display3), pady=5, padx=20)
        self.display3.img = self.img
        self.display3.place(x=410,y=152)
        self.labelu = Label(self.label_frame, text='Username :', font=("Times New Roman", 18, "bold"), fg="#1D79A0",bg="#E0FFFD")
        self.labelu.place(x=75, y=100)
        self.labelp = Label(self.label_frame, text='Password :', font=("Times New Roman", 18, "bold"), fg="#1D79A0", bg="#E0FFFD")
        self.labelp.place(x=75, y=150)
        self.logb=Button(self.label_frame,text="LogIn",bg="#1D79A0",fg="white",font=("Times New Roman",14,"bold"),padx=10,command=lambda: self.authenticate())
        self.logb.place(x=380,y=200)
        self.resetb = Button(self.label_frame, text="Reset", bg="#1D79A0", fg="white",font=("Times New Roman", 14, "bold"), padx=10,command=self.clear)
        self.resetb.place(x=280, y=200)
        self.regb = Button(self.label_frame, text="Register", bg="#1D79A0", fg="white",font=("Times New Roman", 14, "bold"), padx=10,command=self.regform)
        self.regb.place(x=10, y=200)
        self.balance=Label(self.frame4,height=2,text="Balance : Rs. 0/-",font=("Times New Roman",18,"bold"),fg="#1D79A0",bg="white",borderwidth=2, relief="solid")
        self.balance.place(x=10,y=2)
        self.goal=Label(self.frame4,height=2,width=10,text="Budget/day:",font=("Times New Roman",18,"bold"),fg="#1D79A0",bg="#F4FAFC",borderwidth=2, relief="solid")
        self.goal.place(x=500,y=2)
        self.egoal = Entry(self.frame4,  width=10, font=("Arial", 32, "bold"),fg="black", bg="#F4FAFC", borderwidth=2, relief="solid")
        self.egoal.place(x=650, y=2)
        self.egoal.insert(END, self.res.get("monthly",0)//30)
        self.bar = Image.open("Bar_graph.png")
        self.bar = self.bar.resize((890,290))
        self.finbar = ImageTk.PhotoImage(self.bar)
        self.graph=Label(self.frame3,image=self.finbar)
        self.graph.place(x=0,y=0)
        self.graph.bind('<Enter>',lambda e: self.error())
        self.msg=Message(self.frame2,text="""1.Stores your daily Expense
        
2.Accordingly shows weekly as well as monthly analysis 

3.Gives you an alert when you cross your Budget

4.Reminds You about your ultimate goal of saving

5.Now,What are you waiting for login Genius""",bg="#E0FFFD",font=("Times New Roman", 20, "bold"),fg="#1D79A0",width=480)
        self.msg.place(x=0,y=0)
    def error(self):
        if len(self.res)==0:
                self.labell = Label(self.graph, height=12, width=70, text='Login First to get it activated',bg='#D9F8FF',fg='#1D79A0',font=("Times New Roman",18,"bold"))
                self.labell.place(x=0,y=0)
                self.labell.after(2000, self.labell.destroy)
        else:
            pass
    def authenticate(self):
        usename=self.username.get()
        pword=self.pwd.get()
        params = (usename, pword)
        query = "Select * from User where Username=%s and Password=SHA(%s)"
        self.res = get_data(query, params)
        if (self.res is None):
            messagebox.showerror('Incorrect credentials','The username and password entered does not match. Please re-enter')
            self.clear()
        else:
            self.label_frame.destroy()
            print("Login Successful")
            self.loggedin(usename)
    def loggedin(self,usename):
        self.root.configure(bg='#1D79A0')
        self.logf=LabelFrame(self.root, text=f"Welcome {self.res['Username']}",height=300,width=500,background='#E0FFFD',padx=10,font=("inter",14,"bold"),fg="#1D79A0",pady=10)
        self.logf.place(x=30,y=10)
        self.username=Label(self.logf, text=f"Name : {self.res['Name']} ", font=("Times New Roman", 18, "bold"), fg="#1D79A0",bg="#E0FFFD",pady=10)
        self.username.grid(row=0,column=0,sticky='w')
        self.logout=Button(self.logf,text="LogOut",bg="#1D79A0",fg="white",font=("Times New Roman",14,"bold"),padx=10,command=lambda: self.logoutt())
        self.logout.grid(row=0,column=1,sticky='e')

        self.edit = Button(self.logf, text="Edit", bg="#1D79A0", fg="white", font=("Times New Roman", 14, "bold"),
                             padx=10, command=lambda: self.editt())
        self.edit.grid(row=4, column=1, sticky='e')
        self.email = Label(self.logf, text=f"Email : {self.res['email']} ",font=("Times New Roman", 18, "bold"), fg="#1D79A0", bg="#E0FFFD",pady=10)
        self.email.grid(row=1, column=0,sticky='w')
        self.monthly= Label(self.logf, text=f"Monthly Expense : {self.res['monthly']} ", font=("Times New Roman", 18, "bold"), fg="#1D79A0", bg="#E0FFFD",pady=10)
        self.monthly.grid(row=2, column=0,sticky='w')
        self.maxmon = Label(self.logf, text=f"Max Monthly Expense : {self.res['Maxexp']} ",font=("Times New Roman", 18, "bold"), fg="#1D79A0", bg="#E0FFFD",pady=10)
        self.maxmon.grid(row=3, column=0,sticky='w')
        self.moto = Label(self.logf, text=f"Motivation : {self.res['moto']} ",font=("Times New Roman", 18, "bold"), fg="red", bg="#E0FFFD",pady=10)
        self.moto.grid(row=4, column=0,sticky='w')
        self.logf.grid_propagate(0)
        self.graph.destroy()
        self.msg.destroy()
        self.frame2.configure(text="Monthly Analysis")
        self.egoal.delete(0,END)
        self.egoal.insert(END, self.res.get("monthly", 0) // 30)
        Analytics(self.frame3,self.frame2,self.res)
        self.addtable()
    def editt(self):
        self.top2 = Toplevel(self.root)
        # self.top1.configure(bg="white")
        self.top2.title("Registration")
        self.top2.geometry("600x600")

        self.pf = Frame(self.top2, height=200, width=200, bg="#E0FFFD")
        self.pf.pack(expand=1, fill=BOTH)

        self.regf = Label(self.pf, text="Registration Form", font=("Times New Roman", 22, "bold underline"),
                          bg="#E0FFFD")
        self.regf.grid(row=0, column=0, sticky='w')

        self.name = Label(self.pf, text='Name :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.name.grid(row=1, column=0, pady=10, sticky='e')

        self.usname = Label(self.pf, text='Username :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.usname.grid(row=2, column=0, pady=10, sticky='e')

        self.mexp = Label(self.pf, text='Monthly Expense :', font=("Times New Roman", 20, "bold"), fg="black",
                          bg="#E0FFFD")
        self.mexp.grid(row=3, column=0, pady=10, sticky='e')

        self.maxexp = Label(self.pf, text='Maximum Monthly Expense :', font=("Times New Roman", 20, "bold"), fg="black",
                            bg="#E0FFFD")
        self.maxexp.grid(row=4, column=0, pady=10, sticky='e')

        self.email = Label(self.pf, text='Email :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.email.grid(row=5, column=0, pady=10, sticky='e')

        self.passw = Label(self.pf, text='Password :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.passw.grid(row=6, column=0, pady=10, sticky='e')

        self.cpassw = Label(self.pf, text='Confirm Password :', font=("Times New Roman", 20, "bold"), fg="black",
                            bg="#E0FFFD")
        self.cpassw.grid(row=7, column=0, pady=10, sticky='e')

        self.moto = Label(self.pf, text='Motivation :', font=("Times New Roman", 20, "bold"), fg="black", bg="#E0FFFD")
        self.moto.grid(row=8, column=0, pady=10, sticky='e')

        self.ename = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", borderwidth=2,
                           relief="solid")
        self.ename.insert(END, self.res.get("Name", 0))
        self.ename.grid(row=1, column=1, pady=6, sticky='w')
        self.ename.focus_set()
        self.eusname = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                             borderwidth=2)
        self.eusname.insert(END, self.res.get("Username", 0))
        self.eusname.grid(row=2, column=1, pady=6, sticky='w')

        self.emexp = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                           borderwidth=2)
        self.emexp.insert(END, self.res.get("monthly", 0))
        self.emexp.grid(row=3, column=1, pady=6, sticky='w')

        self.emaxexp = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                             borderwidth=2)
        self.emaxexp.insert(END, self.res.get("Maxexp", 0))
        self.emaxexp.grid(row=4, column=1, pady=6, sticky='w')

        self.eemail = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                            borderwidth=2)
        self.eemail.insert(END, self.res.get("email", 0))
        self.eemail.grid(row=5, column=1, pady=6, sticky='w')

        self.raw_image = Image.open("open2.png").resize((20, 22))

        self.img = ImageTk.PhotoImage(self.raw_image)
        self.display = Button(self.pf, image=self.img, command=lambda: self.show(self.epassw, self.display), pady=5,
                              padx=20)
        self.display.grid(row=6, column=2)

        self.raw_image2 = Image.open("close.png").resize((20, 22))

        self.img2 = ImageTk.PhotoImage(self.raw_image2)

        self.epassw = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                            borderwidth=2, show="*")
        # self.epassw.insert(END, self.res.get("Password", 0))
        self.epassw.grid(row=6, column=1, pady=6, sticky='w')

        self.display2 = Button(self.pf, image=self.img, command=lambda: self.show(self.ecpassw, self.display2), pady=5,
                               padx=20)
        self.display2.grid(row=7, column=2)

        self.ecpassw = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                             borderwidth=2, show="*")
        # self.ecpassw.insert(END, self.res.get("Password", 0))
        self.ecpassw.grid(row=7, column=1, pady=6, sticky='w')

        self.emoto = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",
                           borderwidth=2)
        # self.emoto.insert(END, self.res.get("moto", 0))
        self.emoto.grid(row=8, column=1, pady=6, sticky='w')

        self.submit = Button(self.pf, text="Submit", font=("Times New Roman", 18, 'bold'), fg='white', bg='#1D79A0',
                             command=lambda: self.update_user())
        self.submit.grid(row=9, column=0, columnspan=2, rowspan=2, sticky='e', pady=15)

        self.top2.mainloop()


    def update_user(self):
        x=self.res.get("UserId")
        name = self.ename.get()
        user = self.eusname.get()
        mexp = self.emexp.get()
        maxexp = self.emaxexp.get()
        email = self.eemail.get()
        pwd = self.epassw.get()
        co_pwd = self.ecpassw.get()
        moto = self.emoto.get()
        params = (name, user, mexp, maxexp, email, pwd, moto,x)
        query = "Update user set Name=%s,Username=%s,monthly=%s,Maxexp=%s,email=%s,Password=SHA(%s),Moto=%s where UserId=%s"
        execute_query(query, params)

        messagebox.showinfo('Success!', f'Your {user} data is updated')

        params = (user, pwd)

        query = "Select * from User where Username=%s and Password=SHA(%s)"
        self.res = get_data(query, params)
        self.loggedin(user)
        self.top2.destroy()




    def logoutt(self):
        self.res.clear()
        messagebox.showinfo("LoggedOut","You are logged out successfully")
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.label_frame.destroy()
        import letstrack
        letstrack.fpage(self.root)


    def regform(self):
        self.top2 = Toplevel(self.root)
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

        self.moto = Label(self.pf, text='Motivation :', font=("Times New Roman", 20, "bold"), fg="black",bg="#E0FFFD")
        self.moto.grid(row=8, column=0, pady=10, sticky='e')

        self.ename = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",borderwidth=2,relief="solid")
        # self.ename.insert(END, self.res.get("Name",0))
        self.ename.grid(row=1, column=1, pady=6, sticky='w')

        self.ename.focus_set()

        self.eusname = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        # self.eusname.insert(END, self.res.get("Username", 0))
        self.eusname.grid(row=2, column=1, pady=6, sticky='w')

        self.emexp = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        # self.emexp.insert(END, self.res.get("monthly", 0))
        self.emexp.grid(row=3, column=1, pady=6, sticky='w')

        self.emaxexp = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        # self.emaxexp.insert(END,self.res.get("Maxexp",0))
        self.emaxexp.grid(row=4, column=1, pady=6, sticky='w')

        self.eemail =Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2)
        # self.eemail.insert(END, self.res.get("email", 0))
        self.eemail.grid(row=5, column=1, pady=6, sticky='w')

        self.raw_image = Image.open("open2.png").resize((20, 22))

        self.img = ImageTk.PhotoImage(self.raw_image)
        self.display = Button(self.pf, image=self.img, command=lambda :self.show(self.epassw,self.display), pady=5, padx=20)
        self.display.grid(row=6, column=2)

        self.raw_image2 = Image.open("close.png").resize((20, 22))

        self.img2 = ImageTk.PhotoImage(self.raw_image2)

        self.epassw = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2,show="*")
        # self.epassw.insert(END, self.res.get("Password", 0))
        self.epassw.grid(row=6, column=1, pady=6, sticky='w')

        self.display2 = Button(self.pf, image=self.img, command=lambda : self.show(self.ecpassw,self.display2), pady=5, padx=20)
        self.display2.grid(row=7, column=2)

        self.ecpassw = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white",relief="solid",borderwidth=2,show="*")
        # self.ecpassw.insert(END, self.res.get("Password", 0))
        self.ecpassw.grid(row=7, column=1, pady=6, sticky='w')

        self.emoto = Entry(self.pf, font=("Times New Roman", 14, "bold"), fg="black", bg="white", relief="solid",borderwidth=2)
        # self.emoto.insert(END,self.res.get("moto",0))
        self.emoto.grid(row=8, column=1, pady=6, sticky='w')

        self.submit=Button(self.pf,text="Submit",font=("Times New Roman",18,'bold'),fg='white',bg='#1D79A0', command=lambda: self.create_user())
        self.submit.grid(row=9,column=0,columnspan=2,rowspan=2,sticky='e',pady=15)

        self.top2.mainloop()

    def show(self, pwd, widget):
        if pwd["show"]=="*":
            pwd.configure(show="")
            widget.configure(image=self.img2)
        else:
            pwd.configure(show="*")
            widget.configure(image=self.img)
    def create_user(self):
        name=self.ename.get()
        user = self.eusname.get()
        mexp=self.emexp.get()
        maxexp=self.emaxexp.get()
        email=self.eemail.get()
        pwd = self.epassw.get()
        co_pwd = self.ecpassw.get()
        moto=self.emoto.get()
        if (pwd != co_pwd):
            messagebox.showerror("Mismatch", "Passwords don't match. Please re-enter")
        else:
            params = (name,user,mexp,maxexp,email,pwd,moto)
            query = "Insert into user(Name,Username,monthly,Maxexp,email,Password,Moto) Values(%s,%s,%s,%s,%s,SHA(%s),%s)"
            execute_query(query, params)
            messagebox.showinfo('Success!', f'User with username {user} created successfully. Please login again.')
            self.top2.destroy()


    def addtable(self):
        x=self.res['UserId']
        query = f"select expid,product,amt from expense join user on expense.UserId=user.UserId where expense.UserId=%s and today=curdate()"
        result = get_all_data(query,x)
        print(result)
        self.expense_table = SimpleTable(self.frame4, rows=len(result), columns=len(result[0]), height=300, width=800)
        self.expense_table.place(x=10,y=75)
        self.expense_table.grid_propagate(0)

        for r in range(len(result)):  # r  in range(4)--> r=0,1,2,3
            for c in range(len(result[0])):  # c in range(2) c-> 0,1
                self.expense_table.set(row=r, column=c, value=result[r][c])

        self.total_price = map(lambda x: x[2], result[1:])
        self.total_price = sum(self.total_price)

        self.total=Label(self.frame4,text=f'Total Amount: {self.total_price}',height=2,font=("Times New Roman",18,"bold"),fg="#1D79A0",bg="white",borderwidth=2, relief="solid")
        self.total.place(x=650,y=385)

        self.balance.configure(text=f'Balance :Rs{int(self.egoal.get())-self.total_price}/-')
        self.diff=int(self.egoal.get())-self.total_price

        print(self.diff)
        print(self.total_price)
        print(self.egoal.get())
        if self.total_price >=int(0.9*int(self.egoal.get())):
            messagebox.showerror("Danger..", "close your eyes see that gem for which you are saving ,Now Take a look at your goal")
            self.balance.configure(bg='red',fg="white")
        elif self.total_price>=int(0.5*int(self.egoal.get())) and self.total_price<int(0.9*int(self.egoal.get())):
            self.balance.configure(bg='orange',fg='white')
        else:
            self.balance.configure(bg='green',fg='white')



    def toplvl1(self):
        if len(self.res) == 0:
            messagebox.showerror("Not Logged in","Hello user,first please login yourself")
        else:
            self.top1=Toplevel(self.root)
            self.top1.configure(bg="white")
            self.top1.title("Add your expense")
            self.top1.geometry("600x400")
            self.desc=Label(self.top1,background="white",text="Description :",fg="#1D79A0",font=("inter",20,"bold"))
            self.desc.place(x=45,y=80)
            self.dlabel=Entry(self.top1,width=40,fg='black',bg='white',borderwidth=2, relief="solid")
            self.dlabel.place(x=235,y=90)
            self.dlabel.focus_set()
            self.amt = Label(self.top1, background="white", text="Amount :", fg="#1D79A0", font=("inter", 20, "bold"))
            self.amt.place(x=45, y=150)
            self.alabel = Entry(self.top1, width=40, fg='black', bg='white', borderwidth=2, relief="solid")
            self.alabel.place(x=235, y=160)
            self.done=Button(self.top1,height=2,width=15,bg='#1D79A0',fg='white',text="Done",font=("Times New Roman",10,"bold"),command= lambda : self.entertab())
            self.done.place(x=265,y=225)
            self.top1.mainloop()

    def entertab(self):
        describe=self.dlabel.get()
        amount=self.alabel.get()
        goal=self.egoal.get()

        if describe=="" or amount=="":
            messagebox.showerror("Empty..", "Please Enter all the credentials!!")
        else:

                self.top1.destroy()
                params = (self.res['UserId'],describe,amount,datetime.datetime.today().date(),goal)
                query = "Insert into expense(UserId,product,amt,today,goal) Values(%s,%s,%s,%s,%s)"
                execute_query(query, params)
                messagebox.showinfo('Success!', f'You have spent {amount} on {describe} as been recorded')
                self.addtable()


    def clear(self):
        self.username.delete(0, END)
        self.pwd.delete(0, END)
        self.username.focus_set()



if(__name__=="__main__"):
    root=Tk()
    m=withoutlog(root)
    root.mainloop()