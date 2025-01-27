import re
from tkinter import *
from tkinter import messagebox
from .base_gui import BaseGUI
from bll.user_bll import UserBLL
from dto.user_dto import UserDTO
from utils.checker import Checker

class SignupGUI(BaseGUI):
    def __init__(self, parent: Tk):
        super().__init__(parent, 500, 500)
        self.parent.title("Signup Form")
        self.email = None
        self.password = None
        self.repassword = None
        self.login_button = None
        self.user_bll = UserBLL()
        print("SignupGUI is running")
        self.create_widgets()
        self.run()

    def create_widgets(self):
        Label(self.parent, text="Enter your email: ", font=("Arial", 12), anchor="w").pack(pady=5, padx=20, fill="x")  # Thêm nhãn cho email
        self.email = Entry(self.parent, font=("Arial", 12), width=30)
        self.email.pack(pady=5, padx=20, fill="x")

        Label(self.parent, text="Enter password (at least 8 characters):", font=("Arial", 12), anchor="w").pack(pady=5, padx=20, fill="x")  # Thêm nhãn cho password
        self.password = Entry(self.parent, font=("Arial", 12), width=30, show="*")  # Hiển thị password dưới dạng dấu *
        self.password.pack(pady=5, padx=20, fill="x")
        
        Label(self.parent, text="Enter password again:", font=("Arial", 12), anchor="w").pack(pady=5, padx=20, fill="x")  # Thêm nhãn cho password
        self.repassword = Entry(self.parent, font=("Arial", 12), width=30, show="*")  # Hiển thị password dưới dạng dấu *
        self.repassword.pack(pady=5, padx=20, fill="x")

        self.signup_button = Button(self.parent, text="Signup", font=("Arial", 12), width=20, command=self.handle_submit)  # Gọi hàm on_signup khi nhấn nút
        self.signup_button.pack(pady=10)

        # Thêm dòng chuyển hướng sang form Login
        frame = Frame(self.parent)
        frame.pack(pady=5, padx=20, fill="x", anchor="w")

        Label(frame, text="Did you have account?", font=("Arial", 12)).pack(side="left")  # Nhãn nằm bên trái
        self.login_button = Button(frame, text="Let's Login", font=("Arial", 12, "underline"), fg="blue", bd=0, command=self.open_login_form)
        self.login_button.pack(side="left", padx=5)

    def get_email(self):
        return self.email.get().strip()

    def get_password(self):
        return self.password.get()

    def get_repassword(self):
        return self.repassword.get()
    
    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
    
    def is_valid_password(self, password):
        return len(password) >= 8
    
    def is_valid_repassword(self, password, repassword):
        return password == repassword
    
    def is_valid(self, email, password, repassword):
        if not email or not password or not repassword:
            error = "Email and password mustn't be emty."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        elif not Checker.is_valid_email(email):
            error = "Invalid email format. Please enter a valid email."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        elif Checker.is_exist_email(email):
            messagebox.showerror("Error", f"Email {email} is already exist.")
            print(f"Email {email} is already exist.")
            self.email.delete(0, END)
        
        elif not Checker.is_valid_password(password):
            error = "Password at least 8 characters."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        elif not Checker.is_valid_repassword(password, repassword):
            error = "Password and repassword must be the same."
            print(error)
            messagebox.showerror("Error", error)
            return False
        
        else: 
            return True
        
    def handle_submit(self):
        try:
            email = self.get_email()
            password = self.get_password()
            repassword = self.get_repassword()
                
            if not self.is_valid(email, password, repassword):
                self.password.delete(0, END)
                self.repassword.delete(0, END)
                
            else:
                messagebox.showinfo("Success", f"Signup successful!\nEmail: {email}")
                print(f"Signup successful! Email: {email}, Password: {password}")
                user = UserDTO(1, email, password)
                self.user_bll.insert(user)
                
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"Error: {e}")
            
    def open_login_form(self):
        from .login_gui import LoginGUI # Import LoginGUI ở đây để tránh lỗi circular import
        self.destroy()
        root = Tk()
        LoginGUI(root)

