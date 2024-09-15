from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import math,random,os
import datetime

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()



class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("log in page")
        self.root.geometry("1550x800+0+0")

        bg_image=Image.open("bgimage3.jpg")
        resized=bg_image.resize((1300,700),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(resized)
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0)

        frame=Frame(self.root,bg="#E6E6E6")
        frame.place(x=450,y=130,width=340,height=500)

        image1=Image.open("log1img.jpg")
        resized2=image1.resize((100,100),Image.ANTIALIAS)
        self.loginimage=ImageTk.PhotoImage(resized2)
        labelimg1=Label(image=self.loginimage)
        labelimg1.place(x=560,y=130,width=120,height=100)

        log_in=Label(frame,text="Log In",font=("times new roman",20,"bold"),fg="black",bg="#E6E6E6")
        log_in.place(x=130,y=110)

        ##label user name
        user_name=Label(frame,text="Username",font=("times new roman",15,),fg="black",bg="#E6E6E6")
        user_name.place(x=25,y=170)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=35,y=205,width=270)
        #pasword frame
        pass_word=Label(frame,text="Password",font=("times new roman",15,),fg="black",bg="#E6E6E6")
        pass_word.place(x=25,y=250)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=35,y=285,width=270)
        # login button 
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="black",activebackground="yellow")
        loginbtn.place(x=120,y=330,width=100,height=35)
        # forget password
        passbtn=Button(frame,command=self.forgot_password_window,text="Forget password",font=("times new roman",15),borderwidth=0,fg="black",bg="#E6E6E6",activeforeground="black",activebackground="#E6E6E6")
        passbtn.place(x=25,y=380,width=150)
        # NEW USER
        newuserbtn=Button(frame,command=self.register_window,text="New User          ",font=("times new roman",15),borderwidth=0,fg="black",bg="#E6E6E6",activeforeground="black",activebackground="#E6E6E6")
        newuserbtn.place(x=25,y=430,width=150)

    

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)





    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Warning","All enrty field are reqired to log in")
        elif self.txtuser.get()=="shivam" and self.txtpass.get()=="shivam":
            messagebox.showinfo("success","Congratulation log in successfull")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@singh.03",database="project")
            cur = conn.cursor()
            cur.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Bill_App(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
#########reset ##################
    def reset_pass(self):
        if self.secansr.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@singh.03",database="project")
            cur = conn.cursor()
            qury=("select * from register where email=%s and contact=%s")
            value=(self.txtuser.get(),self.secansr.get())
            cur.execute(qury,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct phone",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                valu=(self.txt_newpass.get(),self.txtuser.get())
                cur.execute(query,valu)


                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password has been reset please log in with new password.",parent=self.root2)
                self.root2.destroy()















    


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@singh.03",database="project")
            cur = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            print(row)


            if row==None:
                messagebox.showerror("My Error","please enter the valid userr name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+450+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="#E6E6E6")
                l.place(x=0,y=10,relwidth=1)


                 ####security
                security_q=Label(self.root2,text="Please enter your contact",font=("times new roman",10),bg="#E6E6E6")
                security_q.place(x=50,y=80)

                security_q2=Label(self.root2,text="which you entered during account creation",font=("times new roman",10),bg="#E6E6E6")
                security_q2.place(x=50,y=100)

                



                ####your answer
                answer=Label(self.root2,text="Your answer",font=("times new roman",15),bg="#E6E6E6")
                answer.place(x=50,y=150)

                self.secansr=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.secansr.place(x=50,y=180,width=250)

                ##new password####
                new_password=Label(self.root2,text="Enter new password",font=("times new roman",15),bg="#E6E6E6")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="black",activebackground="yellow")
                btn.place(x=140,y=290)


#############2.37.14#############################################
# #######################################################################################################################################################


























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
        ######framme
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


        loginbtn=Button(frame,command=self.return_login,text="LOG IN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="black",activebackground="yellow")
        loginbtn.place(x=440,y=440,width=100,height=35)
        


        ####FUNCTION DEFINATION #########
    def registerdata(self):
            if self.var_fname.get()=="" or self.var_email.get()==""or self.var_securityQ.get()=="select any one option":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.var_password.get()!=self.var_conpassword.get():
                messagebox.showerror("Error","passworf and confirmed password are different please enter the same.",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@singh.03",database="project")
                cur = conn.cursor()
                query=("select* from register where email=%s")
                value=(self.var_email.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","USER ALREADY EXITS",parent=self.root)
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
                messagebox.showinfo("success","user registered",parent=self.root)


    def return_login(self):

        self.root.destroy()















################################################################main code file ###############################################################

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("BILLINIG SOFTWARE OF SUPERMART")
        self.root.iconbitmap('C:\\Users\\LENOVO\\Desktop\\collage code\\user_icon_251371.ico')
        title=Label(self.root,text="CHANDIGARH SUPER MART. ",bd=12,relief=SUNKEN,bg="#000000",fg="white",font=("Bradley Hand ITC",30,"bold"),pady=2).pack(fill=X)
         #=============Variables defining.........======================
        #=============books........======================
        self.seventh=IntVar()
        self.eighth=IntVar()
        self.ninth=IntVar()
        self.tenth=IntVar()
        self.eleventh=IntVar()
        self.twelveth=IntVar()
        ##===============__________cpoies assing-------------======
        self.cseventh=IntVar()
        self.ceighth=IntVar()
        self.cninth=IntVar()
        self.ctenth=IntVar()
        self.celeventh=IntVar()
        self.ctwelveth=IntVar()
        #===========....products assing..========#
        self.black_pen=IntVar()
        self.blue_pen=IntVar()
        self.punch_paper=IntVar()
        self.book_cover=IntVar()
        self.pencil=IntVar()
        self.chart_paper=IntVar()
        #...................variable for customer.....========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        self.date_time=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.date_time.set(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self.search_bill=StringVar()
        #=============final bill==============
        self.books_price=StringVar()
        self.copies_price=StringVar()
        self.stationary_price=StringVar()

        
       
        # books#####>>>>...... blank frame
        book_frame=LabelFrame(self.root,bd=10,relief=SUNKEN,text="Daily utilities",font=("times new roman",15,"bold"),fg="black",bg="#FFFF00")
        book_frame.place(x=1000,y=80,width=285,height=380)
        seventh_lbl=Label(book_frame,text="shampoo",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="red").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        seventh_txt=Entry(book_frame,width=10,textvariable=self.seventh,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        eighth_lbl=Label(book_frame,text="detergent",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="red").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        eighth_txt=Entry(book_frame,width=10,textvariable=self.eighth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        ninth_lbl=Label(book_frame,text="face wash",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="red").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        ninth_txt=Entry(book_frame,width=10,textvariable=self.ninth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        tenth_lbl=Label(book_frame,text="tooth paste",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="red").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tenth_txt=Entry(book_frame,width=10,textvariable=self.tenth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        eleventh_lbl=Label(book_frame,text="soap",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="red").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        eleventh_txt=Entry(book_frame,width=10,textvariable=self.eleventh,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        twelveth_lbl=Label(book_frame,text="hand wash",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="red").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        twelveth_txt=Entry(book_frame,width=10,textvariable=self.twelveth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        # ..........billing area frames.......,...........
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=3,y=80,width=440,height=380)
        bill_title=Label(F5,text="Final Bill",font=("Bradley Hand ITC",20,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #...................copies set frame,,,,.....#####################
        copy_frame=LabelFrame(self.root,bd=10,relief=SUNKEN,text="groceries",font=("times new roman",15,"bold"),fg="black",bg="#FFFF00")
        copy_frame.place(x=440,y=80,width=285,height=380)
        cseventh_lbl=Label(copy_frame,text="pulse",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cseventh_txt=Entry(copy_frame,width=10,textvariable=self.cseventh,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        ceighth_lbl=Label(copy_frame,text="salt",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        ceighth_txt=Entry(copy_frame,width=10,textvariable=self.ceighth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        cninth_lbl=Label(copy_frame,text="sugar",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cninth_txt=Entry(copy_frame,width=10,textvariable=self.cninth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        ctenth_lbl=Label(copy_frame,text="spieces",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        ctenth_txt=Entry(copy_frame,width=10,textvariable=self.ctenth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        celeventh_lbl=Label(copy_frame,text="rice",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        celeventh_txt=Entry(copy_frame,width=10,textvariable=self.celeventh,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        ctwelveth_lbl=Label(copy_frame,text="oil",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        ctwelveth_txt=Entry(copy_frame,width=10,textvariable=self.ctwelveth,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        ##.......................+==============stationary products,...........#
        stationary_product=LabelFrame(self.root,bd=10,relief=SUNKEN,text="groceries",font=("times new roman",15,"bold"),fg="black",bg="#FFFF00")
        stationary_product.place(x=700,y=80,width=300,height=380)
        blackpen_lbl=Label(stationary_product,text="milk",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        blackpen_txt=Entry(stationary_product,width=10,textvariable=self.black_pen,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        bluepen_lbl=Label(stationary_product,text="curd",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        bluepen_txt=Entry(stationary_product,width=10,textvariable=self.blue_pen,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        punchpaper_lbl=Label(stationary_product,text="banana",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        punchpaper_txt=Entry(stationary_product,width=10,textvariable=self.punch_paper,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        bookcover_lbl=Label(stationary_product,text="potato",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        bookcover_txt=Entry(stationary_product,width=10,textvariable=self.book_cover,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        pencil_lbl=Label(stationary_product,text="onion",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        pencil_txt=Entry(stationary_product,width=10,textvariable=self.pencil,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        chartpaper_lbl=Label(stationary_product,text="egg",font=("Bradley Hand ITC",20,"bold"),bg="#FFFF00",fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        chartpaper_txt=Entry(stationary_product,width=10,textvariable=self.chart_paper,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
       
        #my final frame....========================#################33
        final_bill=LabelFrame(self.root,bd=10,relief=GROOVE,text="Totaling area",font=("times new roman",15,"bold"),fg="black",bg="#FFFF00")
        final_bill.place(x=3,y=465,relwidth=1,height=380)
        m1_lbl=Label(final_bill,text="Total daily utilities",bg="#FFFF00",fg="black",font=("Bradley Hand ITC",14,"bold")).grid(row=0,column=0,padx=20,pady=10,sticky="w")
        m1_txt=Entry(final_bill,width=15,textvariable=self.books_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2_lbl=Label(final_bill,text="Total groceries1",bg="#FFFF00",fg="black",font=("Bradley Hand ITC",14,"bold")).grid(row=1,column=0,padx=20,pady=10,sticky="w")
        m2_txt=Entry(final_bill,width=15,textvariable=self.copies_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3_lbl=Label(final_bill,text="Total groceries2 ",bg="#FFFF00",fg="black",font=("Bradley Hand ITC",14,"bold")).grid(row=2,column=0,padx=20,pady=10,sticky="w")
        m3_txt=Entry(final_bill,width=15,textvariable=self.stationary_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c1_lbl=Label(final_bill,text="Customer name",bg="#FFFF00",fg="black",font=("Bradley Hand ITC",14,"bold")).grid(row=0,column=3,padx=20,pady=10,sticky="w")
        c1_txt=Entry(final_bill,width=15,textvariable=self.c_name,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=10)

        c2_lbl=Label(final_bill,text="phone no",bg="#FFFF00",fg="black",font=("Bradley Hand ITC",14,"bold")).grid(row=1,column=3,padx=20,pady=10,sticky="w")
        c2_txt=Entry(final_bill,width=15,textvariable=self.c_phon,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=10)

        
        total_btn=Button(final_bill,text="Total",command=self.total,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=2,column=3,padx=5,pady=5)
        gbill_btn=Button(final_bill,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=2,column=4,padx=5,pady=5)
        clear_btn=Button(final_bill,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=1,column=7,padx=5,pady=5)
        exit_btn=Button(final_bill,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=1,column=12,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.b_s=self.seventh.get()*200
        self.b_e=self.eighth.get()*400
        self.b_n=self.ninth.get()*150
        self.b_t=self.tenth.get()*100
        self.b_el=self.eleventh.get()*20
        self.b_tl=self.twelveth.get()*50
        self.total_books_price=int(self.b_s + self.b_e + self.b_n + self.b_t + self.b_el + self.b_tl)
                                   
        self.books_price.set("Rs. "+str(self.total_books_price))
        
        self.c_s=self.seventh.get()*95
        self.c_e=self.eighth.get()*20
        self.c_n=self.ninth.get()*40
        self.c_t=self.tenth.get()*150
        self.c_el=self.eleventh.get()*100
        self.c_tl=self.twelveth.get()*250
        self.total_copies_price=int(self.c_s + self.c_e + self.c_n + self.c_t + self.c_el + self.c_tl)
                                    
        self.copies_price.set("Rs. "+str(self.total_copies_price))
        
        self.st_b_p=self.black_pen.get()*60
        self.st_bl_p=self.blue_pen.get()*80
        self.st_p_p=self.punch_paper.get()*5
        self.st_b_c=self.book_cover.get()*25
        self.st_p=self.pencil.get()*40
        self.st_c_p=self.chart_paper.get()*6
        self.total_stationary_price=int(self.st_b_p + self.st_bl_p + self.st_p_p + self.st_b_c + self.st_p + self.st_c_p)                            
                                    
        self.stationary_price.set("Rs. "+str(self.total_stationary_price))
        
        self.total_bill=int(self.total_books_price + self.total_copies_price + self.total_stationary_price)


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Chandigarh super mart")
        self.textarea.insert(END,"\n chandigarh sec-43 near hp petrol pump")
        self.textarea.insert(END,"\n\t ******************")
        self.textarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Date and Time  :{self.date_time.get()}")
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
        
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")

    ##=========
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are Required")
        elif self.books_price.get()=="Rs. 0.0" and self.copies_price.get()=="Rs. 0.0" and self.stationary_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Selected")
        else:
            self.welcome_bill()
            #===cosmatics=====
            if self.seventh.get()!=0:
                self.textarea.insert(END,f"\n shampoo\t\t{self.seventh.get()}\t\t{self.b_s}")
            if self.eighth.get()!=0:
                self.textarea.insert(END,f"\n detergent\t\t{self.eighth.get()}\t\t{self.b_e}")
            if self.ninth.get()!=0:
                self.textarea.insert(END,f"\n facewash\t\t{self.ninth.get()}\t\t{self.b_n}")
            if self.tenth.get()!=0:
                self.textarea.insert(END,f"\n toothpaste\t\t{self.tenth.get()}\t\t{self.b_t}")
            if self.eleventh.get()!=0:
                self.textarea.insert(END,f"\n soap\t\t{self.eleventh.get()}\t\t{self.b_el}")
            if self.twelveth.get()!=0:
                self.textarea.insert(END,f"\n handwash\t\t{self.twelveth.get()}\t\t{self.b_tl}")
            #===Grocery=====
            if self.cseventh.get()!=0:
                self.textarea.insert(END,f"\n pulse\t\t{self.cseventh.get()}\t\t{self.c_s}")
            if self.ceighth.get()!=0:
                self.textarea.insert(END,f"\n salt\t\t{self.ceighth.get()}\t\t{self.c_e}")
            if self.cninth.get()!=0:
                self.textarea.insert(END,f"\n sugar\t\t{self.cninth.get()}\t\t{self.c_n}")
            if self.ctenth.get()!=0:
                self.textarea.insert(END,f"\n spices\t\t{self.ctenth.get()}\t\t{self.c_t}")
            if self.celeventh.get()!=0:
                self.textarea.insert(END,f"\n rice\t\t{self.celeventh.get()}\t\t{self.c_el}")
            if self.twelveth.get()!=0:
                self.textarea.insert(END,f"\n oil\t\t{self.ctwelveth.get()}\t\t{self.c_tl}")
            
            #===Cold Drink=====
            if self.black_pen.get()!=0:
                self.textarea.insert(END,f"\n milk\t\t{self.black_pen.get()}\t\t{self.st_b_p}")
            if self.blue_pen.get()!=0:
                self.textarea.insert(END,f"\n curd\t\t{self.blue_pen.get()}\t\t{self.st_bl_p}")
            if self.punch_paper.get()!=0:
                self.textarea.insert(END,f"\n banana\t\t{self.punch_paper.get()}\t\t{self.st_p_p}")
            if self.book_cover.get()!=0:
                self.textarea.insert(END,f"\n potato\t\t{self.book_cover.get()}\t\t{self.st_b_c}")
            if self.pencil.get()!=0:
                self.textarea.insert(END,f"\n onion    \t\t{self.pencil.get()}\t\t{self.st_p}")
            if self.chart_paper.get()!=0:
                self.textarea.insert(END,f"\n egg\t\t{self.chart_paper.get()}\t\t{self.st_c_p}")

           
            self.textarea.insert(END,f"\n Total Bill  \t\t\t Rs. {self.total_bill}")
            self.textarea.insert(END,f"\n---------- thank you -------------------")
        self.save_bill()
#########  save bill
        
        
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("C:\\Users\\LENOVO\\Desktop\\software design\\save bill\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfullt")
        else:
            return
##---------------_______________clear data--------###


    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============books======================
            self.seventh.set(0)
            self.eighth.set(0)
            self.ninth.set(0)
            self.tenth.set(0)
            self.eleventh.set(0)
            self.twelveth.set(0)
            #=============copies========================
            self.cseventh.set(0)
            self.ceighth.set(0) 
            self.cninth.set(0)
            self.ctenth.set(0)
            self.celeventh.set(0)
            self.ctwelveth.set(0)
            #=============stationary====================
            self.black_pen.set(0)
            self.blue_pen.set(0)
            self.punch_paper.set(0)
            self.book_cover.set(0)
            self.pencil.set(0)
            self.chart_paper.set(0)
            #=============Total Product Price ====================
            self.books_price.set("")
            self.copies_price.set("")
            self.stationary_price.set("")

            
            #=============Customer Detail================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            self.date_time.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.date_time.set(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()






        





main()