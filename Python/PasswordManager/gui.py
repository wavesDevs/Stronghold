import customtkinter
import tkinter
from tkinter import messagebox
from password_manager import *
from passwordGenerator import *

# Limitations
# This GUI has functional windows and buttons, however is not fully finished.
# Some buttons currently print to console, which would ideally have implementation within the window instead.

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def master():
    if entry1.get() == master_pw:
        main_window()
    else:
        tkinter.messagebox.showerror("Error", "Wrong master password was entered.\n-Please try again.")

def main_window():
    
    #Initializing screen
    global screen
    screen = customtkinter.CTk()
    screen.geometry("1280x720")
    screen.title("Stronghold")

    # left frame with buttons
    frame_left = customtkinter.CTkFrame(master=screen)
    frame_left.pack(side="left", pady=20, padx=20, fill='y')
    
    # left frame widgets
    screen.logo_label = customtkinter.CTkLabel(frame_left, text="Stronghold", font=customtkinter.CTkFont(size=20, weight="bold"))
    screen.logo_label.pack(padx=20, pady=(20, 10))
    screen.button_1 = customtkinter.CTkButton(frame_left, text = "Password List", command=lambda: display_pw(passwords, frame_right))
    screen.button_1.pack(padx=20, pady=10)
    screen.button_2 = customtkinter.CTkButton(frame_left, text = "Create Password", command=lambda: create_pw(passwords, frame_right))
    screen.button_2.pack(padx=20, pady=10)
    screen.button_3 = customtkinter.CTkButton(frame_left, text = "Edit Password", command=lambda: edit_pw(passwords))
    screen.button_3.pack(padx=20, pady=10)
    screen.button_4 = customtkinter.CTkButton(frame_left, text = "Exit", command=lambda: end())
    screen.button_4.pack(padx=20, pady=10)

    # Default password frame
    frame_right = customtkinter.CTkFrame(master=screen)
    frame_right.pack(side='right', padx=20, pady=20, fill='both', expand=True)

    # withdrawing the root window, which was for master password
    root.withdraw()
    screen.mainloop()

# def open_input_dialog():
#     dialog = customtkinter.CTkInputDialog(title="Create Password", input_items=[("Website:", ""), ("Username:", ""), ("Password:", "")])
#     values = dialog.get_input()
#     if values:
#         return {"website": values[0], "username": values[1], "password": values[2]}
#     else:
#         return None
    
#function to create a new password and append it to password list
def create_pw(passwords, frame_right):
    # destroy any widgets currently in frame_right
    for widget in frame_right.winfo_children():
        widget.destroy()
    
    # Create the website entry and label
    web_label = customtkinter.CTkLabel(frame_right, text="Website:", pady=20)
    web_label.grid(row=0, column=0)
    web_entry = customtkinter.CTkEntry(frame_right, width=250)
    web_entry.grid(row=0, column=1)

    # Create the username entry and label
    username_label = customtkinter.CTkLabel(frame_right, text="Username:", pady=20)
    username_label.grid(row=1, column=0)
    username_entry = customtkinter.CTkEntry(frame_right, width=250)
    username_entry.grid(row=1, column=1)

    # Create the password choice combobox and label
    pw_choice_label = customtkinter.CTkLabel(frame_right, text="Password:", pady=20)
    pw_choice_label.grid(row=2, column=0)
    pw_choice = customtkinter.CTkComboBox(frame_right, values=["Generate Random Password", "Enter Your Own Password"], width=250)
    pw_choice.grid(row=2, column=1)

    # Create the password entry and label, but hide it for now
    pw_label = customtkinter.CTkLabel(frame_right, text="Password:")
    pw_label.grid(row=3, column=0)
    pw_entry = customtkinter.CTkEntry(frame_right, width=250, show="*")
    pw_entry.grid(row=3, column=1)
    pw_label.grid_remove()
    pw_entry.grid_remove()

    def show_pw_entry():
        pw_label.grid()
        pw_entry.grid()

    def hide_pw_entry():
        pw_label.grid_remove()
        pw_entry.grid_remove()

    def generate_pw_entry():
        generated_pw = pass_gen()
        pw_entry.delete(0, "end")
        pw_entry.insert(0, generated_pw)

    def save_password():
        website = web_entry.get()
        username = username_entry.get()
        if pw_choice.get() == 0:
            password = pw_entry.get()
        else:
            password = generate_pw_entry()
        if website != "" and password != "":
            new_password = {
                "website": website,
                "username": username,
                "password": password,
                "date_added": datetime.date.today().strftime("%Y-%m-%d"),
                "date_modified": datetime.date.today().strftime("%Y-%m-%d")
            }
            passwords.append(new_password)
            messagebox.showinfo(title="Success", message="Password saved successfully!")
        else:
            messagebox.showerror(title="Error", message="Please fill in all required fields.")
        

    if pw_choice.get() == 0:
        pw_choice.bind("<<ComboboxSelected>>", lambda e: generate_pw_entry())
        show_pw_entry()
    else:
        pw_choice.bind("<<ComboboxSelected>>", lambda e: hide_pw_entry())
        hide_pw_entry()

    # Create the save button
    save_button = customtkinter.CTkButton(frame_right, text="Save", command=lambda: save_password())
    save_button.grid(row=4, column=1)
        
def initial_window():

    # initialzinig window
    global root
    root = customtkinter.CTk()
    root.geometry("500x250")
    root.title("Stronghold")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Master Password", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.pack(pady=12, padx=10)

    global entry1
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Master Password", show="*")
    entry1.pack(pady=12, padx=10)

    button=customtkinter.CTkButton(master=frame, text="Login", command=lambda: master())
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

    root.mainloop()

# used for testing within gui file, as opposed to running main
initial_window()