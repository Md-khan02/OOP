# In this task, we are going to be creating email simulator using OOP. 
# First, open the file called email.py
# To define the email class. Constructor wth email details and read status
class Email:
    has_been_read_default = False # Class variable

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address # Sender's email adress
        self.subject_line = subject_line # Email's subject line
        self.email_content = email_content # Content of the email
        self.has_been_read = Email.has_been_read_default # Email read status, initialized to False
    
    # Method to mark an email as read
    def mark_as_read(self):
        self.has_been_read = True

# Initialize an empty list to store email objects
inbox = []

# Function to populate the inbox with three sample emails
def populate_inbox():
    inbox.append(Email("user1@example.com", "Welcome to HyperionDev!", "Congratulations on joining our platform."))
    inbox.append(Email("user2@example.com", "Great work on bootcamp!", "Your progress is impressive, Keep it up!."))
    inbox.append(Email("user3@example.com", "Your excellant marks!", "Your recent submission was outstanding."))

# Function to list all emails in the index with their read status
# with prints each email's subject line wirh a corresponding number.
def list_emails():
    print("\nList of Emails:")
    for index, email in enumerate(inbox):
        read_status = "(Read)" if email.has_been_read else "(Unread)"
        print(f"{index} {email.subject_line} {read_status}")


# Function to display the contents of a selected email and marks it as read
def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}\n")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")  
    else:
        print("Invalid email index. Please try again.")

# --- Email Program --- #
# Populate the Inbox with sample emails for use in the program
populate_inbox()

# User menu for email operations
while True:
    try:
       user_choice = input('''\nWould you like to:
       1. Read an email
       2. View unread emails
       3. Quit application

       Enter selection: ''')
    
       if user_choice == '1':
          list_emails()
          email_index = int(input("Enter the number of the email you want to read: "))
          read_email(email_index)
       elif user_choice == '2':
          print("\nUnread Emails:")
          for index, email in enumerate(inbox):
              if not email.has_been_read:
                 print(f"{index} {email.subject_line} (Unread)")
       elif user_choice == '3':
          print("Quitting application. Goodbye!")
          break # Exit the while loop to quit the application
       else:
          print("Oops - incorrect input. Please enter a valid option.")
    except ValueError:
       print("Please enter a number for your choice.")
