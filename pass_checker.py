import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import zxcvbn
from pwnedpasswords import check as check_password_breach
import string
import random
import threading
import os

# Function to check password strength
def check_password_strength(password):
    strength = zxcvbn.zxcvbn(password)
    score = strength['score']  # 0-4
    feedback = strength['feedback']
    return score, feedback

# Function to check if password has been breached
def check_breach(password):
    try:
        result = check_password_breach(password)
        return result > 0, result
    except Exception as e:
        print(f"Error checking password breach: {e}")
        return False, 0

# Function to generate a strong password
def generate_strong_password(length=16):
    charset = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(charset) for _ in range(length))

# GUI Application Class
class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.iconbitmap('pass_checker.ico')

        # Title Label
        self.title_label = ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Password Entry
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(root, textvariable=self.password_var, show="*", width=30, font=("Helvetica", 12))
        self.password_entry.pack(pady=10)
        self.password_entry.bind('<Return>', lambda event: self.evaluate_password())

        # Strength Display
        self.strength_label = ttk.Label(root, text="Strength: ", font=("Helvetica", 12))
        self.strength_label.pack(pady=5)

        # Breach Display
        self.breach_label = ttk.Label(root, text="", font=("Helvetica", 10), foreground="red")
        self.breach_label.pack(pady=5)

        # Buttons Frame
        self.buttons_frame = ttk.Frame(root)
        self.buttons_frame.pack(pady=10)

        # Check Button
        self.check_button = ttk.Button(self.buttons_frame, text="Check Password", command=self.evaluate_password)
        self.check_button.grid(row=0, column=0, padx=5)

        # Generate Button
        self.generate_button = ttk.Button(self.buttons_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=0, column=1, padx=5)

        # Copy Button (Initially Hidden)
        self.copy_button = ttk.Button(root, text="Copy Password", command=self.copy_password)
        self.copy_button.pack(pady=5)
        self.copy_button.pack_forget()  # Hide initially

    def evaluate_password(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Input Error", "Please enter a password.")
            return

        # Disable buttons during processing
        self.disable_buttons()

        # Use threading to prevent GUI freezing
        threading.Thread(target=self.process_password, args=(password,)).start()

    def process_password(self, password):
        score, feedback = check_password_strength(password)
        breached, breach_count = check_breach(password)

        # Update UI in the main thread
        self.root.after(0, self.update_ui, score, feedback, breached, breach_count)

    def update_ui(self, score, feedback, breached, breach_count):
        # Strength Mapping
        strength_map = {
            0: ("Very Weak", "red"),
            1: ("Weak", "orange"),
            2: ("Fair", "yellow"),
            3: ("Strong", "light green"),
            4: ("Very Strong", "green")
        }

        strength_text, color = strength_map.get(score, ("Unknown", "black"))
        self.strength_label.config(text=f"Strength: {strength_text}", foreground=color)

        # Breach Information
        if breached:
            self.breach_label.config(text=f"⚠️ This password has been seen {breach_count} times before!", foreground="red")
        else:
            self.breach_label.config(text="✅ This password has not been found in any breaches.", foreground="green")

        # Enable buttons after processing
        self.enable_buttons()

    def generate_password(self):
        new_password = generate_strong_password()
        self.password_var.set(new_password)
        self.breach_label.config(text="")
        self.strength_label.config(text="Strength: ")

        # Show copy button
        self.copy_button.pack(pady=5)

    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    def disable_buttons(self):
        self.check_button.config(state="disabled")
        self.generate_button.config(state="disabled")

    def enable_buttons(self):
        self.check_button.config(state="normal")
        self.generate_button.config(state="normal")

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()
