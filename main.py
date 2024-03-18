import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from options_panel import open_option_panel

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your authentication logic here
    # For simplicity, let's check if the username and password are not empty
    if username and password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        open_option_panel(root)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    username = entry_username.get()
    password = entry_password.get()

    # Add your registration logic here
    # For simplicity, let's check if the username and password are not empty
    if username and password:
        messagebox.showinfo("Registration Successful", "Account created for " + username + "!")
    else:
        messagebox.showerror("Registration Failed", "Please enter a valid username and password")

# Create the main window
root = tk.Tk()
root.title("Welcome To Animal Connect")
heading_font = ("Chewy", 30, "bold")

# Create and place widgets
label_heading = tk.Label(root, text="Welcome To Animal Connect", font=heading_font, fg="#FF69B4")
label_heading.pack(pady=10)

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root, font=('Helvetica', 12), bd=2, relief=tk.GROOVE)
entry_username.pack(pady=5, padx=20)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", font=('Helvetica', 12), bd=2, relief=tk.GROOVE)
entry_password.pack(pady=5, padx=20)

btn_login = tk.Button(root, text="Login", command=login, font=('Helvetica', 12), bg='#4CAF50', fg='white', relief=tk.RAISED)
btn_login.pack(pady=10)

btn_register = tk.Button(root, text="Register", command=register, font=('Helvetica', 12), bg='#008CBA', fg='white', relief=tk.RAISED)
btn_register.pack(pady=5)

pet_image = tk.PhotoImage(file="peticon.png")
label_pet = tk.Label(root, image=pet_image)
label_pet.pack(pady=10)

root.mainloop()
