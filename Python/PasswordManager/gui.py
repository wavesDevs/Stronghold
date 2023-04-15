import tkinter as tk
from password_manager import get_master, check_master

# Create the main window
root = tk.Tk()
root.geometry("1280x720")
root.title("Password Manager")

# Create a label and text box for the master password
master_password_label = tk.Label(root, text="Enter your master password:")
master_password_label.pack()
master_password_textbox = tk.Entry(root, show="*")
master_password_textbox.pack()

# Function to check the master password
def check_password():
    password = master_password_textbox.get()
    check_master()
    if check_master:
        enable_buttons()
    else:
        print("Wrong password")
    # Call your password checking function here
    # If password is correct, enable the buttons

def enable_buttons():
    view_passwords_button.config(state="normal")
    create_password_button.config(state="normal")
    edit_password_button.config(state="normal")
    exit_button.config(state="normal")

# Create the buttons
view_passwords_button = tk.Button(root, text="View Passwords", state="disabled")
create_password_button = tk.Button(root, text="Create a New Password", state="disabled")
edit_password_button = tk.Button(root, text="Edit an Existing Password", state="disabled")
exit_button = tk.Button(root, text="Exit", command=root.quit)

# Pack the buttons
view_passwords_button.pack()
create_password_button.pack()
edit_password_button.pack()
exit_button.pack()

# Bind the check_password function to the Return key
root.bind("<Return>", lambda event: check_password())

# Start the main loop
root.mainloop()