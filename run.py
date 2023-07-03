#All the imports for the program
import gspread
from google.oauth2.service_account import Credentials
from data import bio, contact, mercury_text, venus_text, the_moon_text, \
     mars_text, jupyter_text, saturn_text, uranus_text, neptune_text,\
     availability, faqs, bank
import datetime


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

#Function to input and select a planet trip
def trips_options():

    destination = input("Please enter a number between 1 and 8 to find out\
more about the planet trips: ")
    #while statement to catch a non valid character and loop till
    #correct input by user
    while destination not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        destination = input("Invalid destination. Please enter a number\
between 1 and 8: ")

    #Setting up function to retrieve data from spreadsheet 
    trip_details = SHEET.worksheet('trip_details')
    column_names = trip_details.row_values(1)
    row_data = trip_details.row_values(int(destination) + 1)
    print(column_names)
    print(row_data)

    #If/Else selector for planets menu
    if destination == "1":
        mercury_text()
    elif destination == "2":
        venus_text()
    elif destination == "3":
        the_moon_text()
    elif destination == "4":
        mars_text()
    elif destination == "5":
        jupyter_text()
    elif destination == "6":
        saturn_text()
    elif destination == "7":
        uranus_text()
    elif destination == "8":
        neptune_text()

#Secondary menu choice for user
    while True:
        menu_choice = input('''
            If you would like to see more Planets, please type P.
            If you would like to go back to the Main Menu, please type E: ''')

        if menu_choice == "P":
            trips_options()
            break
        elif menu_choice == "E":
            menu()
            break
        else:
            print("Invalid input. Please enter 'P' or 'E'.")


#FAQs answers function
def data_faqs():

#FAQs answers are stored in a spreadsheet
    answers_faqs = SHEET.worksheet('answers')
#User input to fetch correct answer data
    choice = input("Please enter a number from 1 to 20 to fetch the \
corresponding cell value: ")
    if choice.isdigit() and 1 <= int(choice) <= 20:
        row_data = answers_faqs.row_values(int(choice))
        print(row_data)
        #While statement to give use an option to see more answers
        #or to go back to main menu
        while True:
            choice1 = input('''
                    If you would like to see more Answers, please type A.
                    If you would like to go back to the Main Menu,\
please type E: ''')

            if choice1 == "A":
                data_faqs()
                break
            elif choice1 == "E":
                menu()
                break
            else:
                print("Invalid input. Please enter 'A' or 'E'.")
    else:
        print("Invalid input. Please enter a valid number from 1 to 20.")
        data_faqs()

#Price function from a spreadsheet
def price():
    chosen_destination = input("Please enter a number between 1 and 8 to\
select a planet:")
    while chosen_destination not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
          chosen_destination = input("Invalid destination. Please enter a \
number between 1 and 8: ")

    trip_details = SHEET.worksheet('trip_details')
    column_names = trip_details.row_values(1)
    row_data = trip_details.row_values(int(chosen_destination) + 1)

    # Retrieve the values of the 1st and 4th columns to display
    column1_value = row_data[0]
    column4_value = row_data[3]

    print(column_names[0], ":", column1_value)
    print(column_names[3], ":", column4_value)

#Passenger object to gather and save user input
class Passenger:

    def __init__(self):
        self.name = ""
        self.lastName = ""
        self.dateOfBirth = None
        self.gender = ""
        self.addressLine1 = ""
        self.addressLine2 = ""
        self.cityTown = ""
        self.countyProvince = ""
        self.country = ""
        self.postCode = ""
        self.phoneNumber = ""
        self.dateOfTravel = None

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
        availability()
        trips_options()

#FAQs section
    elif choice == "3":
        faqs()
        data_faqs()
        back_to_menu()

#Get Your Tickets section
    elif choice == "4":
        bank()

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


