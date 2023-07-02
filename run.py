#All the imports for the program
import gspread
from google.oauth2.service_account import Credentials


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


