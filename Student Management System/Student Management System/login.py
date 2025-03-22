from tkinter import*
import PIL
from PIL import Image,ImageTk
import PIL.Image
from tkinter import ttk,messagebox
import sqlite3
from register import Register
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        
        self.bg=ImageTk.PhotoImage(file="images/4.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/3.jpeg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=360,height=450)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=420,y=100,width=700,height=450)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,'bold'),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,'bold'),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)


        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,'bold'),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)


        btn_reg=Button(login_frame,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_window).place(x=250,y=320)

        btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2",command=self.forget_password_window).place(x=450,y=320)


        btn_login=Button(login_frame,text="Login",font=("times new roman",20,'bold'),fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=250,y=380,width=180,height=40)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forger_password(self):
        if self.txt_email.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select currect security quetion/ Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_pass.get(),self.txt_email.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password Has Been Reset,You can login by Entering new password")
                    self.reset()
                    self.root2.destroy()
            except Exception as es:    
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter Email to reset the Password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter the valid Email to reset the Password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+200")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,'bold'),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    question=Label(self.root2,text="Security Question",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=100)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",15),state='readonly',justify=CENTER )
                    self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",20,'bold'),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",bg="green",fg="white",font=("times new roman",15,'bold'),command=self.forger_password).place(x=90,y=340)
                    


            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)



    def register_window(self):
        self.root.destroy()
        os.system("python register.py")  

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)             
                else:
                    messagebox.showinfo("Success",f"Welcome {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")  

                con.close()
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()