from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

# comments started
def fact(n):
     if n==0:
          return 1
     return n*fact(n-1)


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register window")
        self.root.geometry("1550x800+0+0")






        #variable defining ######
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_conpassword=StringVar()






        bg_image=Image.open("registerbg1.jpeg")
        resized=bg_image.resize((1300,700),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(resized)
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0)

        ##frame
        frame=Frame(self.root,bg="#E6E6E6")
        frame.place(x=320,y=110,width=640,height=500)


        image1=Image.open("regicon.png")
        resized2=image1.resize((200,200),Image.ANTIALIAS)
        self.loginimage=ImageTk.PhotoImage(resized2)
        labelimg1=Label(image=self.loginimage)
        labelimg1.place(x=585,y=130,width=120,height=100)

        reg=Label(frame,text="REGISTRATION",font=("times new roman",20,"bold"),fg="red",bg="#E6E6E6")
        reg.place(x=220,y=110)


        ####entry field
        fname=Label(frame,text="First name",font=("times new roman",15),bg="#E6E6E6")
        fname.place(x=30,y=150)

        self.fnameuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fnameuser.place(x=30,y=180,width=180)

        ###last name###
        Lname=Label(frame,text="Last name",font=("times new roman",15),bg="#E6E6E6")
        Lname.place(x=420,y=150)

        self.lnameuser=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lnameuser.place(x=420,y=180,width=180)

        ##### CONTACT
        cno=Label(frame,text="Contact number",font=("times new roman",15),bg="#E6E6E6")
        cno.place(x=30,y=220)

        self.contno=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contno.place(x=30,y=250,width=180)

        ##gmail
        gmail=Label(frame,text="Email",font=("times new roman",15),bg="#E6E6E6")
        gmail.place(x=420,y=220)

        self.gmailid=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.gmailid.place(x=420,y=250,width=180)



        ####security
        security_q=Label(frame,text="select security question",font=("times new roman",15),bg="#E6E6E6")
        security_q.place(x=30,y=290)

        self.sec_question=ttk.Combobox(frame,textvariable=self.var_securityQ,text="select security question",font=("times new roman",15,"bold"),state="readonly")
        self.sec_question["values"]=("select any one option","your date of birth","your nick name","your friend name")
        self.sec_question.current(0)
        self.sec_question.place(x=30,y=330,width=200)


        



        ####your answer
        answer=Label(frame,text="Your answer",font=("times new roman",15),bg="#E6E6E6")
        answer.place(x=420,y=290)

        self.secansr=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.secansr.place(x=420,y=320,width=180)


        ##passwordd
        pas=Label(frame,text="Password",font=("times new roman",15),bg="#E6E6E6")
        pas.place(x=30,y=370)

        self.paskey=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        self.paskey.place(x=30,y=400,width=180)


        cpas=Label(frame,text="cofirm password",font=("times new roman",15),bg="#E6E6E6")
        cpas.place(x=420,y=370)

        self.cpaskey=ttk.Entry(frame,textvariable=self.var_conpassword,font=("times new roman",15,"bold"))
        self.cpaskey.place(x=420,y=400,width=180)


        ###buttun ##
        signbtn=Button(frame,command=self.registerdata,text="SIGN UP",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="black",activebackground="yellow")
        signbtn.place(x=30,y=440,width=100,height=35)


        loginbtn=Button(frame,text="LOG IN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="black",activebackground="yellow")
        loginbtn.place(x=440,y=440,width=100,height=35)
        


        ####FUNCTION DEFINATION #########
    def registerdata(self):
            if self.var_fname.get()=="" or self.var_email.get()==""or self.var_securityQ.get()=="select any one option":
                messagebox.showerror("Error","All fields are required")
            elif self.var_password.get()!=self.var_conpassword.get():
                messagebox.showerror("Error","passworf and confirmed password are different please enter the same.")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@singh.03",database="project")
                cur = conn.cursor()
                query=("select* from register where email=%s")
                value=(self.var_email.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","USER ALREADY EXITS")
                else:
                     cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_password.get()

                                                                                         ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","user registered")





root=Tk()
obj=register(root)

root.mainloop()