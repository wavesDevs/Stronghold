import customtkinter
import tkinter.messagebox
from password_manager import *
from passwordGenerator import *

# Limitations
# This GUI has functional windows and buttons, however is not fully finished.
# Buttons currently print to console, which would ideally have implementation within the window instead.
# However, for the purpose of this project, the logic itself was more important, and the GUI is more of a quality of life feature.

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
    screen.title("wavesDev Password Manager")

    # unused frame here for reference.
    # frame = customtkinter.CTkFrame(master=screen)
    # frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Main frame with widgets
    screen.logo_label = customtkinter.CTkLabel(screen, text="Password Manager", font=customtkinter.CTkFont(size=20, weight="bold"))
    screen.logo_label.pack(padx=20, pady=(20, 10))
    screen.button_1 = customtkinter.CTkButton(screen, text = "Password List", command=lambda: display_pw(passwords))
    screen.button_1.pack(padx=20, pady=10)
    screen.button_2 = customtkinter.CTkButton(screen, text = "Create Password", command=lambda: create_pw(passwords))
    screen.button_2.pack(padx=20, pady=10)
    screen.button_3 = customtkinter.CTkButton(screen, text = "Edit Password", command=lambda: edit_pw(passwords))
    screen.button_3.pack(padx=20, pady=10)
    screen.button_4 = customtkinter.CTkButton(screen, text = "Exit", command=lambda: end())
    screen.button_4.pack(padx=20, pady=10)

    # withdrawing the root window, which was for master password
    root.withdraw()
    screen.mainloop()
        
def initial_window():

    # initialzinig window
    global root
    root = customtkinter.CTk()
    root.geometry("500x250")
    root.title("wavesDev Password Manager")

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