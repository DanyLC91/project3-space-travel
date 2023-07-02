#All the imports for the program
import gspread
from google.oauth2.service_account import Credentials
from data import bio, contact, mercury_text, venus_text, the_moon_text, \
     mars_text, jupyter_text, saturn_text, uranus_text, neptune_text,\
     availability, faqs


#Program credentials and setting up link for spreadsheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('space_travel_data')

#Welcome message
print('''
 
                      \033[1m CosmoLink Travel \033[0m
        
                'Where Imagination Meets Infinity'


''')

#Main Menu setting 
def menu():
    print("Menu:")
    print("1. Bio")
    print("2. Our Packages")
    print("3. FAQs")
    print("4. Get your Ticket")
    print("5. Contact")
    print("6. Exit")

    choice = input("To navigate our Menu, Please one of the following\
options (1-6):\n ")

#Back to Main Menu option with input
    def back_to_menu():
        choice2 = input("Press 0 to go back to the MENU options\n")

        if choice2 == "0":
            menu()
        else:
            print("Invalid choice. Please try again.")
            input()
            menu()    
#BIO section
    if choice == "1":
        bio()
        back_to_menu()

#Our Packages section
    elif choice == "2":
        print("\033[1m Our Packages \033[0m")
        print('''      
        1. Mercury
        2. Venus
        3. The Moon
        4. Mars
        5. Jupiter
        6. Saturn
        7. Uranus
        8. Neptune
        ''')

#FAQs section
    elif choice == "3":

#Get Your Tickets section
    elif choice == "4":

#Contact section
    elif choice == "5":
        contact()
        back_to_menu()

#Exit the program
    elif choice == "6":
        print("Exiting the program.")
        return

#If character other than 1 t0 6 enter, loop for new input
    else:
        print("Invalid choice. Please try again.")
        menu()


menu()


