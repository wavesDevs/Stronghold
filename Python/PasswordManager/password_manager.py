import datetime
import sys
import passwordGenerator
import customtkinter
import tkinter.scrolledtext as tkst
import tkinter

#defining password list with dictionaries
passwords = [
    {
    "password" : "Test1",
    "username" : "User1",
    "website" : "www.google.com",
    "date_modified" : datetime.datetime(2023, 4, 15),
    "date_added" : datetime.datetime(2022, 1, 10)
    },
    {
    "password" : "Test2",
    "username" : "User2",
    "website" : "www.facebook.com",
    "date_modified" : datetime.datetime(2023, 4, 14),
    "date_added" : datetime.datetime(2022, 1, 11)
    },
    {
    "password" : "Test3",
    "username" : "User3",
    "website" : "www.youtube.com",
    "date_modified" : datetime.datetime(2023, 4, 13),
    "date_added" : datetime.datetime(2022, 1, 12)
    },
    {
    "password" : "Test4",
    "username" : "User4",
    "website" : "www.reddit.com",
    "date_modified" : datetime.datetime(2023, 4, 12),
    "date_added" : datetime.datetime(2022, 1, 13)
    },
    {
    "password" : "Test5",
    "username" : "User5",
    "website" : "www.twitter.com",
    "date_modified" : datetime.datetime(2023, 4, 11),
    "date_added" : datetime.datetime(2022, 1, 14)
    },
    {
    "password" : "Test6",
    "username" : "User6",
    "website" : "www.netflix.com",
    "date_modified" : datetime.datetime(2023, 4, 10),
    "date_added" : datetime.datetime(2022, 1, 15)
    },
    {
    "password" : "Test7",
    "username" : "User7",
    "website" : "www.spotify.com",
    "date_modified" : datetime.datetime(2023, 4, 9),
    "date_added" : datetime.datetime(2022, 1, 16)
    }
]

#hard-coding master password. DB storage/retrieval should be implemented
master_pw = "1234"

#global variables from display_pw(). necessary to initialize in order to destroy it upon calling display_pw(), so that data can be updated without adding extra frames.
text_widget = None
password_frame = None

#function to retrieve master password (ideally from secure location later, for now its hard-coded)
def get_master():
    return master_pw

#function to check if user input matches the master password, to allow list access.
def check_master(input):
    master = get_master()
    if input == master:
        return True
    else:
        return False

#display function for password list.    
def display_pw(passwords, master):
    # GUI implementation
    # global variables
    global password_frame, text_widget, header_widget

    # if a password frame already exists, destroy all widgets, Allows for updating data without creating new frames.
    if not password_frame:
        password_frame = customtkinter.CTkFrame(master=master)
        password_frame.grid(row=0, column=0, sticky='nsew')
        # password_frame.pack(fill='both', expand=True, padx=20, pady=20)
    else:
        # Clear the contents of the password frame
        for widget in password_frame.winfo_children():
            widget.destroy()

    header_widget = customtkinter.CTkFrame(password_frame)
    header_widget.grid(row=0, column=0, sticky='nsew')
    header_label = customtkinter.CTkLabel(header_widget, font=("Source Code Pro Medium", 12), text=f"{'Index':<10} {'Website':<20} {'Username':<20} {'Password':<30} {'Date Modified':<20} {'Date Added':<20}\n")
    header_label.grid(sticky='w')

    text_widget = customtkinter.CTkTextbox(header_widget, font=("Source Code Pro Medium", 12))
    text_widget.grid(row=1, column=0, sticky='nsew')

    header_widget.grid_columnconfigure(0, minsize=text_widget.winfo_width())

    #display logic
    for i, password in enumerate(passwords, start=1):
        website = password["website"]
        password_str = password["password"]
        username = password["username"]
        
        #if date_modified is a datetime object already, convert to string. If it is not, first convert to a datetime object and then a string.
        #this is necessary in order to properly display the date_modified, because otherwise a type error is thrown.
        if isinstance(password["date_modified"], datetime.datetime):
            date_modified = password["date_modified"].strftime("%Y-%m-%d")
        else:
            date_modified = datetime.datetime.strptime(password["date_modified"], "%Y-%m-%d").strftime("%Y-%m-%d")
        
        #same principal as date_modified, it is necessary to check the object type before displaying.
        if isinstance(password["date_added"], datetime.datetime):
            date_added = password["date_added"].strftime("%Y-%m-%d")
        else:
            date_added = datetime.datetime.strptime(password["date_added"], "%Y-%m-%d").strftime("%Y-%m-%d")

        text_widget.insert('end', f"{i:<10} {website:<20} {username:<20} {password_str:<30} {date_modified:<20} {date_added:<20}\n")

#function to edit an existing password and update the password list
def edit_pw(passwords):
    display_pw(passwords)
    password_index = int(input("Enter the number of the password you would like to edit: ")) - 1
    password = passwords[password_index]
    print(f"You are choosing to edit {password['website']}")
    field = input("Which field would you like to edit? Type 'website', 'username', or 'password': ")
    new_value = input(f"Enter the new {field}: ")
    password[field] = new_value
    password["date_modified"] = datetime.date.today().strftime("%Y-%m-%d")

    print(f"{field.capitalize()} for {password['website']} updated successfully!")

def end():
    sys.exit()