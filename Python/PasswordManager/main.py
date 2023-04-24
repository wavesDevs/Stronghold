from password_manager import *

#main function    
def main():
    #while loop to allow user to continue trying to enter master password if entered incorrectly
    while True:
        user_master = input("Enter the master password: ")

        #user options
        if check_master(user_master):
            print("\nSuccess! What would you like to do?\n")
            print("Enter the number that corresponds to the desired action:")
            print("1) View passwords")
            print("2) Create a new password")
            print("3) Edit an existing password")
            print("4) Exit")
            user_choice = input()
            
            #while loop to allow user to enter a choice, with sys.exit() option to terminate entire script if selected.
            while True:
                if user_choice == '1':
                    display_pw(passwords)
                    break
                elif user_choice == '2':
                    create_pw(passwords)
                    break
                elif user_choice == '3':
                    edit_pw(passwords)
                    break
                elif user_choice == '4':
                    end()
                else:
                    print("Invalid choice, please enter either '1', '2', '3', or '4' to proceed.")
        else:
            print("Incorrect master password. Try again")

#run program
main()