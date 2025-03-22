from tkinter import*
from PIL import Image,ImageTk
import PIL.Image
from tkinter import ttk,messagebox
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")


        self.bg=ImageTk.PhotoImage(file="images/2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/1.jpeg")
        left=Label(self.root,image=self.left).place(x=50,y=100,width=360,height=500)


        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=100,width=700,height=500)


        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,'bold'),bg="white",fg="green").place(x=50,y=30)


        f_name=Label(frame1,text="First Name",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=100)
        self.txt_f_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_f_name.place(x=50,y=130,width=250)


        l_name=Label(frame1,text="Last Name",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=370,y=100)
        self.txt_l_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_l_name.place(x=370,y=130,width=250)


        contact=Label(frame1,text="Contact Number",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

       
        question=Label(frame1,text="Security Question",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER )
        self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        password=Label(frame1,text="Password",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)


        self.var_chk=IntVar()        
        chk=Checkbutton(frame1,text="I Agree The Term & Condition",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new romas",12),bg="white").place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/6.jpeg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.redister_data).place(x=50,y=400,width=350,height=100)
        btn_login=Button(self.root,text="Sign in",font=("time new roman",20),bd=0,cursor="hand2",command=self.login_window).place(x=150,y=450,width=170)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")  


    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def redister_data(self):
        if self.txt_f_name.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
              messagebox.showerror("Error","All Fields Are required",parent=self.root)
              self.txt_l_name.get()

        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Condition",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showinfo("Error","User already exist,Please try another Email",parent=self.root)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password)values(?,?,?,?,?,?,?)",
                            (
                                self.txt_f_name.get(),
                                self.txt_l_name.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get(),
                            ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showinfo("Success",f"Error Due to {str(es)}",parent=self.root)


                

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()