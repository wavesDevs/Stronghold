import datetime
import sys

#defining password list with dictionaries
passwords = [
    {
    "password" : "Test1",
    "website" : "www.google.com",
    "date_modified" : datetime.datetime(2023, 4, 15),
    "date_added" : datetime.datetime(2022, 1, 10)
    },
    {
    "password" : "Test2",
    "website" : "www.facebook.com",
    "date_modified" : datetime.datetime(2023, 4, 14),
    "date_added" : datetime.datetime(2022, 1, 11)
    },
    {
    "password" : "Test3",
    "website" : "www.youtube.com",
    "date_modified" : datetime.datetime(2023, 4, 13),
    "date_added" : datetime.datetime(2022, 1, 12)
    }
]

#hard-coding master password
master_pw = "1234"

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
def display_pw(passwords):
    #formatting for clean visual in console
    print("\n{:<20} {:<20} {:<20} {:<20}".format("Website", "Password", "Date Modified", "Date Added"))
    print("-" * 80)

    #display logic. iterates through passwords list and prints each item of the password dictionary separately, formatted.
    for password in passwords:
        website = password["website"]
        password_str = password["password"]
        date_modified = password["date_modified"].strftime("%Y-%m-%d")
        date_added = password["date_added"].strftime("%Y-%m-%d")
        print("{:<20} {:<20} {:<20} {:<20}".format(password['website'], password['password'], date_modified, date_added))
    
    print("\n")

#function to create a new password and append it to password list
def create_pw():
    return None

#function to edit an existing password and update the password list
def edit_pw():
    return None



