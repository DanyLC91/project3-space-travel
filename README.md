# Project 2 - Space Travel



[CosmoLink Travel](https://space-travel01-358659227732.herokuapp.com/)



## About




The Space Travel project is a Python app that hosts a fictitious company named CosmoLink Travel, which offers information about trips and gives use to buy one.
This program utilizes the gspread library to interact with the Google Sheets API for data storage and retrieval.
This project was created for Code Institute Project 3.


## Features


### Menu Option

The menu system is designed to provide a seamless and intuitive user experience. It guides users through the available options, validates their inputs, and performs the necessary actions based on their selections.
The app provides a user-friendly menu system that allows users to interact with various functionalities offering the following features:


1. #### Bio: 
This option provides users with information about the space agency and its mission. 

2. #### Our Trips
 Users can select this option to explore the available space travel packages offered by the agency. The menu provides a detailed list of packages, including destinations, durations, and prices. Users can get an overview of the exciting space journeys they can embark on.

3. #### FAQs
The Frequently Asked Questions (FAQs) section aims to address common queries and concerns of users. Users can find valuable information to make informed decisions about their space travel experience.

4. #### Get your Tickets
 By selecting this option, users will be guided through a step-by-step process to select their desired trip, provide personal details, and get details for the necessary payment.

5. #### Contacts
Users can access the contact information of the space agency through this menu option.

6. #### Exit
This option will terminate the program.



### Trip Booking



Users can book a space trip by selecting a destination from a list of eight planets. The program presents the available destinations and prompts the user to enter their personal details. The user is required to provide their name, last name, date of birth, gender, address, phone number, and date of travel. The program performs input validation to ensure that the provided data is correct and complete.



### Data Storage



The passenger information is securely stored in a Google Sheets spreadsheet. The program utilizes the gspread library to establish a connection with the Google Sheets API. It creates a worksheet named "passenger" to store the passenger data. Each row in the spreadsheet represents a passenger, and the columns correspond to different attributes. When a user books a trip, the program appends a new row with the passenger's information to the spreadsheet. This ensures that the data is organized and easily accessible for future reference.



### Details Confirmation



To review the most recent passenger information, the program allows users to retrieve the last row of saved data from the Google Sheets spreadsheet. This feature ensures that users can easily access the latest entries and verify their details or track the most recent bookings made.

### Data.py

As there was much information and text for this app, to keep a tidy structure, a secondary Python file was created to host all functions that were hosting big pieces of text.
These functions were then imported and used in the main app file run.py.



## Functionality

The programs was done at 80 charactes lenght, as per requested by Code Institute, for Heroku deployment.


## Frameworks - Libraries - Programs Used

-Gitpod
-Youtube (tutorial for learning python)
-Google Auth
-Heroku (for app deployment)
-PyCharm (for offline programming)
-ChatGPT (for fictional content data)



## Development Issues

I had problems committing/pushing the program through Codeanywhere, so after chatting with my tutor, I decided that the best option for this project was uploaded via GitPod.

Adding credentials issues problem was solved thanks to tutor help.


## Credits

Special Thanks to my tutor Gareth McGirr for all the help


###### Disclaimer: the fictitious data placed on the BIO, FAQs, Contacts, PLanets info and other fictional details have been a mix of my own inspiration and ChatGPT generation. The AI was not use to create the code, as it's banned by Code Institute.