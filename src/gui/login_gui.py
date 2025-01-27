import re
from tkinter import *
from tkinter import messagebox
from .base_gui import BaseGUI
from bll.user_bll import UserBLL
from utils.checker import Checker

class LoginGUI(BaseGUI):
    def __init__(self, parent: Tk):
        super().__init__(parent, 500, 500)
        self.parent.title("Login Form")
        self.email = None
        self.password = None
        self.login_button = None
        self.user_bll = UserBLL()
        print("LoginGUI is running")  
        self.create_widgets()
        self.run()
            
    def create_widgets(self):
        Label(self.parent, text="Enter your email: ", font=("Arial", 12), anchor="w").pack(pady=5, padx=20, fill="x")  # Thêm nhãn cho email
        self.email = Entry(self.parent, font=("Arial", 12), width=30)
        self.email.pack(pady=5, padx=20, fill="x")

        Label(self.parent, text="Enter password (at least 8 characters):", font=("Arial", 12), anchor="w").pack(pady=5, padx=20, fill="x")  # Thêm nhãn cho password
        self.password = Entry(self.parent, font=("Arial", 12), width=30, show="*")  # Hiển thị password dưới dạng dấu *
        self.password.pack(pady=5, padx=20, fill="x")

        self.login_button = Button(self.parent, text="Login", font=("Arial", 12), width=20, command=self.handle_submit)  # Gọi hàm on_login khi nhấn nút
        self.login_button.pack(pady=10)
        
        # Thêm dòng chuyển hướng sang form Signup
        frame = Frame(self.parent)
        frame.pack(pady=5, padx=20, fill="x", anchor="w")

        Label(frame, text="Did you not have account?", font=("Arial", 12)).pack(side="left")  # Nhãn nằm bên trái
        self.signup_button = Button(frame, text="Let's Signup", font=("Arial", 12, "underline"), fg="blue", bd=0, command=self.open_signup_form)
        self.signup_button.pack(side="left", padx=5)

    def get_email(self):
        return self.email.get().strip()

    def get_password(self):
        return self.password.get()

    def is_valid(self, email, password):
        if not email or not password:
            error = "Email and password mustn't be emty."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        elif not Checker.is_valid_email(email):
            error = "Invalid email format. Please enter a valid email."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        elif not Checker.is_exist_email(email):
                messagebox.showerror("Error", f"Email {email} is not exist.")
                print(f"Email {email} is not exist.")
                self.password.delete(0, END)
        
        elif not Checker.is_valid_password(password):
            error = "Password at least 8 characters."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        else: 
            return True
        
    def handle_submit(self):
        try:
            email = self.get_email()
            password = self.get_password()
                
            if not self.is_valid(email, password):
                self.password.delete(0, END)
                
            else:
                messagebox.showinfo("Success", f"Login successful!\nEmail: {email}")
                print(f"Login successful! Email: {email}, Password: {password}")
                user = self.user_bll.get_by_email(email)
                user.set_state(2)
                self.user_bll.update(user)
                self.destroy()
                
        except Exception as e:
            print(e)
            messagebox.showerror("Error", e)
            
    def open_signup_form(self):
        from .signup_gui import SignupGUI # Import SignupGUI ở đây để tránh lỗi circular import
        self.destroy()
        root = Tk()
        SignupGUI(root)