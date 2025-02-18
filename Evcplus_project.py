
import os
from datetime import datetime
import time

# Function to clear the screen (works for Windows and Unix-based systems)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


    #llllllllllllllllllllllllllllllllllllllllll

import re
from datetime import datetime

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-z]+@[a0-z9]{26,}'
    return re.match(regex, email) is not None

def is_valid_date(date_str):
    # Validate the date format
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def email_activity():
    # Prompt for email and ensure it's valid
    while True:
        email = print("Please enter your email: ")
        email = input("")
        clear_screen()
        if is_valid_email(email):
            break
        print("Invalid email format. Please try again.")
    
    
    reference_date = datetime.strptime("26/10/2021", "%d/%m/%Y")
      # Prompt for the "after" date and ensure it's valid
    while True:
        after_date = print("Please enter a date after 26/10/2021 (DD/MM/YYYY): ")
        after_date = input("")
        clear_screen()
        if is_valid_date(after_date):
            entered_after_date = datetime.strptime(after_date, "%d/%m/%Y")
            if entered_after_date > reference_date:
                break
            else:
                print("The date must be after 26/10/2021. Please try again.")
        else:
            print("Invalid date format. Please try again.")

      # Prompt for the "before" date and ensure it's valid
    while True:
        before_date = print("Please enter a date before 26/10/2024 (DD/MM/YYYY): ")
        before_date = input("")
        if is_valid_date(before_date):
            entered_before_date = datetime.strptime(before_date, "%d/%m/%Y")
            if entered_before_date < reference_date:
                break
            else:
                print("The date must be before 26/10/2024. Please try again.")
        else:
            print("Invalid date format. Please try again.")

    print(f"Your request is being processed, and the activity will be emailed to {email}")

# Function to read PIN from a file or set a default if the file doesn't exist
def read_pin():
    try:
        with open("pin.txt", "r") as file:
            return int(file.read().strip())  # Read the saved PIN from the file
    except FileNotFoundError:
        return 2007  # Default PIN if no file is found

# Function to save the new PIN into a file
def save_pin(new_pin):
    with open("pin.txt", "w") as file:
        file.write(str(new_pin))  # Write the new PIN to the file

# Function to read the balance from a file or set a default balance if not found
def read_balance():
    try:
        with open("balance.txt", "r") as file:
            return float(file.read().strip())  # Read the balance and convert to float for calculations
    except FileNotFoundError:
        return 100  # Default balance if no file is found

# Function to save the updated balance into a file
def save_balance(new_balance):
    with open("balance.txt", "w") as file:
        file.write(f"{new_balance:.2f}")  # Save balance as a formatted number (2 decimal places)

# Function to log transactions
def log_transaction(description, amount):
    with open("transactions.txt", "a") as file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date_time} | {description}: ${amount}\n")

# Function to get the last transaction
def get_last_transaction():
    try:
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()
            if transactions:
                return transactions[-1].strip()
    except FileNotFoundError:
        return "No transactions found."

# Function to get the last three transactions
def get_last_three_transactions():
    try:
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()
            return transactions[-3:] if len(transactions) >= 3 else transactions
    except FileNotFoundError:
        return []

# Function to handle incorrect PIN attempts
def handle_incorrect_pin(attempts):
    if attempts >= 2:
        print("")
        print("PIN qaldan oo lagu celceliyay awgeed adeega, [-EVCPlus-] waa lagaa xayirey.")
        print("")
        print("fadlan isku soo dey 2 daqiiqo ka dib, Mahadsanid!.")
        print("")
        for remaining_minutes in range(2, 0, -1):
            print(f"Remaining minutes: {remaining_minutes}")
            time.sleep(60)  # Wait for 1 minute before checking again
        clear_screen()

# Initial setup
password = read_pin()  # Load current PIN from the file or use the default PIN
Balance = read_balance()  # Load current balance from the file or use the default balance
phone_number = "MSISDN: 252615820767"  # Added phone number
incorrect_pin_attempts = 0  # Track incorrect PIN attempts

# Function to handle the input code (*770# or *711# or #999#)




def check_code():
    global incorrect_pin_attempts
    user_input = input().strip()  # User enters 770#, *711#, or *712 codes
    clear_screen()

    if user_input == "*770#":
        enter_pin_770()  # Go to *770# options
    elif user_input == "*711#":
        enter_pin_711()  # Show balance directly for *711#
    elif user_input == "#999#":
        clear_screen()  # Clear screen before showing phone number
        print(phone_number)  # Show phone number
        check_code()  # Return to main code input
    elif user_input.startswith('*712*') and user_input.endswith('#'):
        handle_712_code(user_input)  # Call the function to handle 712 codes
    elif user_input == "PIN":
        enter_pin()
    elif user_input == "*712#":
        print("Qaabka aad u isticmaashey waa khalad.")
        print("Fadlan isticmaal: *712*number*lacagta*cents#")
    elif user_input == "*713#":
        print("Qaabka aad u isticmaashey waa khalad.")
        print("Fadlan isticmaal: *713*number*lacagta*cents#")
    elif user_input == "*714#":
        print("Qaabka aad u isticmaashey waa khalad.")
        print("Fadlan isticmaal: *714*number*lacagta*cents#")
    elif user_input == "*722#":
        print("Qaabka aad u isticmaashey waa khalad.")
        print("Fadlan isticmaal: *722*number*lacagta*cents#")
    elif user_input == "*736#":
        print("You are not allowed to access this short code")
    elif user_input == "*777#":
        print("Sorry, the operation failed due to the invalid message format")
    else:
        print("Error performing request")
        print("Unknown Error")
          # Re-prompt if code is incorrect


def is_valid_amount(amount_str):
    # Check for format restrictions and leading zeros
    if amount_str < "001":
         print("hhh")
         return False
    
    # Check for multiple decimal points and valid numeric format
    if amount_str.count('.') > 1:
        print("Invalid amount format! Amount must contain at most one decimal point.")
        return False

    # Check for numeric validity
    try:
        amount = float(amount_str)  # Ensure the amount string can be converted to float
        if amount < 0.01:
            print("The minimum amount must be 0.01.")
            return False
        return True
    except ValueError:
        print("Invalid amount format!")
        return False

def convert_amount(amount_str):
    # Handle leading zeros
    if amount_str.startswith('0'):
        if amount_str == "00":  # Exactly '00' is invalid
            return None
        elif len(amount_str) == 3:  # '009' to '0.09'
            return float(f"0.{amount_str[1:]}")
        elif len(amount_str) == 2:  # '09' to '0.9'
            return float(f"0.{amount_str[1]}")
    return float(amount_str)  # Return as is for valid integer amounts

def handle_712_code(user_input):
    # Split the USSD input by '*'
    parts = user_input.split('*')

    if len(parts) < 4:
        print("Invalid format!")
        return

    number = parts[2]  # Extract the mobile number

    # Validate the mobile number format
    if (number.startswith('61') or number.startswith('77') or number.startswith('68')) and len(number) == 9:
        # Handle first pattern: *712*number*100#
        if len(parts) == 4:  # Example: *712*612345678*100#
            amount_str = parts[3].rstrip('#')  # Remove the trailing '#'
            if is_valid_amount(amount_str):  # Check if the amount is valid
                amount = convert_amount(amount_str)  # Convert to float with new rules
                if amount is not None:  # Ensure amount conversion was successful
                    if amount.is_integer():
                        print(f"Uwareeji ${amount:.0f} number-ka {number}",)
                        enter_pin_for_transaction(number, amount) 
                    else:
                        print(f"Uwareeji ${amount:.2f} number-ka {number}",)
                        enter_pin_for_transaction(number, amount)  # Prompt for PIN

        # Handle second pattern: *712*number*100*5#
        elif len(parts) == 5:  # Example: *712*612345678*100*5#
            integer_part = parts[3].rstrip('#')  # Get integer part
            decimal_part = parts[4].rstrip('#')  # Get decimal part
            # Combine the integer and decimal parts
            amount_str = f"{integer_part}.{decimal_part}"  
            if is_valid_amount(amount_str):  # Check if the amount is valid
                amount = convert_amount(amount_str)  # Convert to float with new rules
                if amount is not None:  # Ensure amount conversion was successful
                    print(f"Uwareeji ${amount:.2f} number-ka {number}",)
                    enter_pin_for_transaction(number, amount)  # Prompt for PIN

        # Handle case for *712*number*amount*decimal# (e.g., *712*612345678*100*01#)
        elif len(parts) == 6:  # Example: *712*612345678*100*01#
            integer_part = parts[3].rstrip('#')  # Get integer part
            decimal_part = parts[4].rstrip('#')  # Get decimal part
            # Combine the integer and decimal parts
            amount_str = f"{integer_part}.{decimal_part}"  
            if is_valid_amount(amount_str):  # Check if the amount is valid
                amount = convert_amount(amount_str)  # Convert to float with new rules
                if amount is not None:  # Ensure amount conversion was successful
                    print(f"Uwareeji ${amount:.2f} number-ka {number}",)
                    enter_pin_for_transaction(number, amount)  # Prompt for PIN
            else:
                print("Invalid amount format!")

        else:
            print("Invalid USSD format!")

    else:
        print("Invalid mobile number format!")

def enter_pin_for_transaction(number, amount):
    global incorrect_pin_attempts
    pin = input("Fadlan geli PIN-kaaga: ").strip()  # Prompt for PIN
    clear_screen()  # Clear screen after input

    if pin.isdigit():
        if int(pin) == password:  # Check if the entered PIN is correct
            uwareeji_evcplus(number, amount)  # Proceed with the transaction
            incorrect_pin_attempts = 0  # Reset incorrect PIN attempts
        else:
            incorrect_pin_attempts += 1
            print("[-EVCPLUS-] Numberka sirta ah waa khalad")
            handle_incorrect_pin(incorrect_pin_attempts)  # Handle incorrect attempts
            enter_pin_for_transaction(number, amount)  # Re-prompt if PIN is wrong
    else:
        print("[-EVCPLUS-] Numberka sirta ah waa khalad")
        enter_pin_for_transaction(number, amount)  # Re-prompt if PIN is wrong
def enter_pin_for_transaction(number, amount):
    global incorrect_pin_attempts
    print("Fadlan geli PIN-kaaga: ")
    pin = input().strip()  # Prompt for PIN
    clear_screen()  # Clear screen after input

    if pin.isdigit():
        if int(pin) == password:  # Check if the entered PIN is correct
            uwareeji_evcplus1(number, amount)  # Proceed with the transaction
            incorrect_pin_attempts = 0  # Reset incorrect PIN attempts
        else:
            incorrect_pin_attempts += 1
            print("[-EVCPLUS-] Numberka sirta ah waa khalad")
            handle_incorrect_pin(incorrect_pin_attempts)  # Handle incorrect attempts
              # Re-prompt if PIN is wrong
    else:
        print("[-EVCPLUS-] Numberka sirta ah waa khalad")
         # Re-prompt if PIN is wrong

def uwareeji_evcplus1(number, amount):
    global Balance
 
        # Proceed with transfer logic
    amount_cents = float(amount) * 100  # Convert to cents for easier calculations
    if amount_cents <= Balance:
            Balance -= amount_cents  # Deduct amount from balance
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"[-EVCPlus ] ${amount:.2f} ayaad u wareejisay {number}", -amount_cents / 100)  # Log transaction
            if amount.is_integer():
               print(f"[-EVCPLUS-] ${amount} ayaad u wareejisay  {number}")
               print(f"Haraagaagu waa ${Balance / 100:.2f}.")
            else:
                print(f"[-EVCPLUS-] ${amount:.2f} ayaad u wareejisay  {number}")
                print(f"Haraagaagu waa ${Balance / 100:.2f}.") 
    else:   
        print("Haraagaagu kugu ma filna!")
  


# Function for entering PIN
def enter_pin():
    global incorrect_pin_attempts
    pin = input("Fadlan geli PIN-kaaga: ")
    pin = input("").strip()  # Prompt for PIN
    clear_screen()  # Clear screen after input

    if pin.isdigit():
        if int(pin) == password:
            show_options()  # Show options if PIN is correct
            incorrect_pin_attempts = 0  # Reset incorrect PIN attempts
        else:
            incorrect_pin_attempts += 1
            print("[-EVCPLUS-] Numberka sirta ah waa khalad")
            handle_incorrect_pin(incorrect_pin_attempts)
            enter_pin()  # Re-prompt if PIN is wrong
    else:
        print("[-EVCPLUS-] PIN-ka waa khalad")
        enter_pin()  # Re-prompt if PIN is wrong

# Function for *770# PIN entry
def enter_pin_770():
    
    global incorrect_pin_attempts
    
    pin = print("Fadlan geli PIN-kaaga: ")
    pin = input("").strip()  # Prompt for PIN
    clear_screen()  # Clear screen after input

    if pin.isdigit():
        if int(pin) == password:
            show_options()  # Show options if PIN is correct
            incorrect_pin_attempts = 0  # Reset incorrect PIN attempts
        else:
            incorrect_pin_attempts += 1
            print("[-EVCPLUS-] Numberka sirta ah waa khalad")
            handle_incorrect_pin(incorrect_pin_attempts)
            enter_pin_770()  # Re-prompt if PIN is wrong
    else:
        print("PIN-kaagu waa khalad")
        enter_pin_770()  # Re-prompt if PIN is wrong

# Function for *711# PIN entry and show balance
def enter_pin_711():
    global incorrect_pin_attempts
    pin = print("Fadlan geli PIN-kaaga: ")
    pin = input("").strip()  # Prompt for PIN
    clear_screen()  # Clear screen after input

    if pin.isdigit():
        if int(pin) == password:
            itus_haraaga()
            incorrect_pin_attempts = 0  # Reset incorrect PIN attempts
        else:
            incorrect_pin_attempts += 1
            print("[-EVCPLUS-] Numberka sirta ah waa khalad")
            handle_incorrect_pin(incorrect_pin_attempts)
            enter_pin_711()  # Re-prompt if PIN is wrong
    else:
        print("[-EVCPLUS-] PIN-ka waa khalad")
        enter_pin_711()  # Re-prompt if PIN is wrong
        
# Function to show options after PIN is accepted for *770#
def show_options():
    clear_screen()  # Clear screen before showing options
    print("   EVCPlus")  # Title for EVCPlus menu
    print("1. Itus Haraaga")
    print("2. Kaarka Hadalka")
    print("3. Bixi Bill")
    print("4. Uwareeji EVCPlus")
    print("5. Warbixin Kooban")
    print("6. Salaam Bank")
    print("7. Maareynta")
    print("8. Bill Payment")
    option = input().strip()  # No prompt, user selects an option
    clear_screen()  # Clear screen after input

    if option == '1':
       itus_haraaga()
   
    elif option == '2':
        show_kaarka_hadalka_options()
    elif option == '3':
        show_bixi_bill_options()
    elif option == '4':
        uwareeji_evcplus()
    elif option == '5':
        show_warbixin_options()
    elif option == '6':
        show_salaaam_bank_options()
    elif option == '7':
        show_maareynta_options()
    elif option == '8':
        print("Taaj service selected.")

    else:
        print("Fadlan dooro Number sax ah!")
          # Re-prompt if an invalid option is selected
def itus_haraaga():
    clear_screen()
    balance_in_dollars = Balance / 100  # Convert cents back to dollars

    # Display the balance as dollars with one decimal place
       # Re-read updated balance from the file
             
   # Display the updated balance correctly
    if (Balance / 100).is_integer():
        print(f"[-ECVPlus-] Haraagaagu waa: ${Balance / 100}")
    else:
        print(f"[-ECVPlus-] Haraagaagu waa: ${Balance / 100:.2f}")

# Function to show options under Kaarka Hadalka (option 2)
def show_kaarka_hadalka_options():
    clear_screen()  # Clear screen before showing options
    print("   Kaarka Hadalka")  # Title for Kaarka Hadalka
    print("1. Ku shubo Airtime")
    print("2. Ugu shub Airtime")
    print("3. Mifi packages")
    print("4. Ku shubo internet")
    print("5. Ugu shub qof kale (MMT)")
    print("6. Recharge Balance")  # New option to recharge balance

    kaarka_option = input().strip()  # No prompt, user selects an option
    clear_screen()  # Clear screen after input

    if kaarka_option == '1':
        ku_shubo_airtime()  # Call function for Airtime
    elif kaarka_option == '2':
        ugu_shub_airtime()  # Call the new function for Ugu shub Airtime
    elif kaarka_option == '3':
          mifi_packages()
    elif kaarka_option == '4':
        ku_shubo_internet()
    elif kaarka_option == '5':
        ugu_shub_qof_kale_mmt()
    elif kaarka_option == '6':
        recharge_balance()  # Call function to recharge balance
    else:
        print("Fadlan dooro Number sax ah!")
         
# Function to handle Ugu shub Airtime (option 1 under Kaarka Hadalka)
def ku_shubo_airtime():
    global Balance
    print("Fadlan geli lacagta")  # Prompt user for amount
    amount = input().strip()

    try:
        # Convert the input to float
        amount = float(amount)  
        amount_cents = int(amount * 100)  # Convert dollars to cents

        if amount_cents > 0:  # Ensure the recharge amount is positive
            if Balance >= amount_cents:  # Check if balance is sufficient
                clear_screen()
                print(f"Mahubtaa in aad ${amount:.2f} ugu shubtid undefined?")
                print("1. Haa")
                print("2. Maya")
                confirmation = input().strip()
                clear_screen()

                if confirmation == '1':
                    Balance -= amount_cents  # Deduct from balance
                    save_balance(Balance)  # Save the updated balance
                    log_transaction("Airtime Purchase", amount_cents)  # Log the transaction
                    clear_screen()
                    
                    # Display the recharged amount
                    if amount.is_integer():
                        print(f"Waad ku guuleysatay inaad ku shubato ${int(amount)} Airtime")
                    else:
                        print(f"Waad ku guuleysatay inaad ku shubato ${amount:.2f} Airtime")
                    print("")
                    print("252615820767")
                    print("")
                    
                    # After the transaction, re-read the balance from file to ensure it's up to date
                    Balance = read_balance()  # Re-read updated balance from the file
                    
                    # Display the updated balance correctly
                    if (Balance / 100).is_integer():
                        print(f"Haraagaagu waa: ${Balance / 100:.0f}")
                        date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
                        print(date_time)
                    else:
                        print(f"Haraagaagu waa: ${Balance / 100:.2f}")
                        date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
                        print(date_time)
                else:
                    print("Mahadsanid!")
            else:
                print("Haraagaagu kuma filna.")  # Insufficient balance
        else:
            print("Lacag sax ah ma ahan.")  # Handle negative or zero amount
    except ValueError:
        print("Lacag sax ah ma ahan.")  # Catch invalid inputs
        ku_shubo_airtime()  # Reprompt the user

               

# Function to handle Ugu shub Airtime (option 2 under Kaarka Hadalka)
def ugu_shub_airtime():
    global Balance
    while True:
        try:
            print("Fadlan Geli Mobile-ka")
            number = int(input())
            number = str(number)
            clear_screen()
            break
        except ValueError:
                print("Invalid data type")
                

    # Proceed to enter the amount, keep asking until a valid amount is provided
    while True:
        print("Fadlan Geli lacagta")
        amount = input().strip()
        clear_screen()

        try:
            # Try to convert the input to a float
            amount = float(amount)
            amount_cents = int(amount * 100)
            # Check if the amount is positive
            if amount > 0:
                break  # Exit loop if valid amount is entered
            else:
                print("Lacagtu waa inay noqotaa mid togan!")  # Amount must be positive
        except ValueError:
            print("You can only enter a number!")  # Handle invalid input
            ugu_shub_airtime()

    # Ask for confirmation
    print(f"Mahubtaa inaad u shubto ${amount:.2f} qofka lambarkiisu yahay {number}?")
    print("1. Haa")
    print("2. Maya")
    confirmation = input().strip()
    clear_screen()

    if confirmation == '1':
        # Validation occurs ONLY AFTER user presses '1'
        # Check if the number starts with 61 or 77 and ensure it's exactly 9 digits long
        if (number.startswith('61') or number.startswith('77')) and len(number) != 9:
            print("Numberka kaarka hadalka aad u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!.")  # Invalid number for 61 or 77 after confirmation
            return

        # Check if the number starts with 061 and ensure it's either 9 or 10 digits long
        elif number.startswith('061') and len(number) not in [9, 10]:
            print("Numberka kaarka hadalka aad u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!.")  # Invalid number for 061 after confirmation
            return

        # If the number doesn't start with valid prefixes (061, 61, 77)
        elif not (number.startswith('061') or number.startswith('61') or number.startswith('77')):
            print("Numberka kaarka hadalka aad u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!.")  # Invalid number due to invalid prefix
            return

        # If valid, check balance
        if amount <= Balance:
            Balance -= amount_cents  # Deduct the amount from balance
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"Ugu shub Airtime {number}", -amount_cents)  # Log the transaction
            print(f"Waxad ${amount:.2f} ugu shubtay {number}")
            print(f"[-EVCPlus-] Haraagaaga waa ${Balance / 100:.2f}")
            date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
            print(date_time)
            
        else:
            print("Haraaga xisaabtaadu kuguma filna, Mobile No:")
            print("252615820767")
    else:
        print("Mahadsanid!.")


# Function to handle Mifi packages (option 3 under Kaarka Hadalka)
def mifi_packages():
    clear_screen()  # Clear screen before showing options
    print("   Mifi Packages")
    print("1. Ku shubo data Mifi")

    mifi_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if mifi_option == '1':
        ku_shubo_data_mifi()  # Call function to handle data purchase
    else:
        print("Fadlan dooro number sax ah!")
          

# Function to handle Ku shubo data Mifi (under Mifi Packages)
def ku_shubo_data_mifi():
    clear_screen()
    print("1. Isbuucle (Weekly)")
    print("2. Maalinle (Daily)")
    print("3. Bille (Mifi)")

    data_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if data_option == '1':
        show_weekly_data_options()  # Show weekly data options
    elif data_option == '2':
        show_daily_data_options()  # Show daily data options
    elif data_option == '3':
        show_monthly_data_options()  # Show monthly data options
    else:
        print("Fadlan dooro number sax ah!")  # Placeholder for invalid input

# Function to show weekly data options
def show_weekly_data_options():
    global Balance
    clear_screen()
    print("1. $5 = 10GB")
    print("2. $10 = 25GB")

    weekly_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if weekly_option == '1':
        data_price = 500  # Price for 10GB
        data_gb = 10
    elif weekly_option == '2':
        data_price = 100  # Price for 25GB
        data_gb = 25
    else:
        print("Invalid option. Dib u day.")
        show_weekly_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to show daily data options
def show_daily_data_options():
    global Balance
    clear_screen()
    print("1. $1 = 2GB")
    print("2. $2 = 5GB")

    daily_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if daily_option == '1':
        data_price = 10  # Price for 2GB
        data_gb = 2
    elif daily_option == '2':
        data_price = 20  # Price for 5GB
        data_gb = 5
    else:
        print("Invalid option. fadlan dooro number sax ah!")
        show_daily_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to show monthly data options
def show_monthly_data_options():
    global Balance
    clear_screen()
    print("1. $20 = 40GB")
    print("2. $40 = 85GB")
    print("3. $60 = 150GB")
    print("4. $30 = Unlimited month")

    monthly_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if monthly_option == '1':
        data_price = 200  # Price for 40GB
        data_gb = 40
    elif monthly_option == '2':
        data_price = 400  # Price for 85GB
        data_gb = 85
    elif monthly_option == '3':
        data_price = 600  # Price for 150GB
        data_gb = 150
    elif monthly_option == '4':
        data_price = 300  # Price for unlimited
        data_gb = 'Unlimited'
    else:
        print("Invalid option. fadlan dooro number sax ah!.")
        show_monthly_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to process data purchase
def process_data_purchase(data_price, data_gb):
    global Balance
    # Ask for phone number
    while True:
        try:
            print("Fadlan Geli Mobile-ka")
            number = int(input())
            number = str(number)
            clear_screen()
            break
        except ValueError:
                print("Invalid data type")

    # Validate the phone number (must start with 61 or 77 and be 9 digits long)
    if (phone_number.startswith('61') or phone_number.startswith('77')) and len(phone_number) == 9:
        if Balance >= data_price:  # Check if the balance is sufficient
            Balance -= data_price  # Deduct the amount from the balance
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"Mifi Data Recharge ({data_gb}GB) to {phone_number}", {-data_price / 100})  # Log transaction
            print("Sent successfully.")
        else:
            print("Macsalaam. Haraagaagu kuma filna.")
    else:
        print("Loodiraha ma ahan mid jira")

    # After the transaction, re-read the balance from the file
    # Re-read updated balance from the file
     
#uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

# Function to handle Mifi packages (option 3 under Kaarka Hadalka)
def ku_shubo_internet():
    clear_screen()  # Clear screen before showing options
    print("   Mifi Packages")
    print("1. Ku shubo data Mifi")

    internet_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if internet_option == '1':
        ku_shubo_data_mifi()  # Call function to handle data purchase
    else:
        print("Invalid option. Dib u day.")
        ku_shubo_internet() # Re-prompt if an invalid option is selected

# Function to handle Ku shubo data Mifi (under Mifi Packages)
def ku_shubo_data_internet():
    clear_screen()
    print("1. Isbuucle (Weekly)")
    print("2. Maalinle (Daily)")
    print("3. Bille (Mifi)")

    data_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if data_option == '1':
        show_weekly_data_options()  # Show weekly data options
    elif data_option == '2':
        show_daily_data_options()  # Show daily data options
    elif data_option == '3':
        show_monthly_data_options()  # Show monthly data options
    else:
        print("Fadlan dooro number sax ah")  # Placeholder for invalid input

# Function to show weekly data options
def show_weekly_data_options():
    global Balance
    clear_screen()
    print("1. $5 = 10GB")
    print("2. $10 = 25GB")

    weekly_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if weekly_option == '1':
        data_price = 500 # Price for 10GB
        data_gb = 10
    elif weekly_option == '2':
        data_price = 100  # Price for 25GB
        data_gb = 25
    else:
        print("Invalid option. fadlan isku dey mar kale")
        show_weekly_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to show daily data options
def show_daily_data_options():
    global Balance
    clear_screen()
    print("1. $1 = 2GB")
    print("2. $2 = 5GB")

    daily_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if daily_option == '1':
        data_price = 10  # Price for 2GB
        data_gb = 20
    elif daily_option == '2':
        data_price = 20  # Price for 5GB
        data_gb = 5
    else:
        print("Invalid option. Dib u day.")
        show_daily_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to show monthly data options
def show_monthly_data_options():
    global Balance
    clear_screen()
    print("1. $20 = 40GB")
    print("2. $40 = 85GB")
    print("3. $60 = 150GB")
    print("4. $30 = Unlimited month")

    monthly_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if monthly_option == '1':
        data_price = 2000  # Price for 40GB
        data_gb = 40
    elif monthly_option == '2':
        data_price = 4000  # Price for 85GB
        data_gb = 85
    elif monthly_option == '3':
        data_price = 6000 # Price for 150GB
        data_gb = 150
    elif monthly_option == '4':
        data_price = 3000  # Price for unlimitedzy
        data_gb = 'Unlimited'
    else:
        print("Invalid option. Dib u day.")
        show_monthly_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to process data purchase
def process_data_purchase(data_price, data_gb):
    global Balance
    # Ask for phone number
    while True:
        try:
            print("Fadlan Geli Mobile-ka")
            phone_number = int(input())
            phone_number = str(phone_number)
            clear_screen()
            break
        except ValueError:
                print("Invalid data type")
    clear_screen()

    # Validate the phone number (must start with 61 or 77 and be 9 digits long)
    if (phone_number.startswith('61') or phone_number.startswith('77')) and len(phone_number) == 9:
        if Balance >= data_price:  # Check if the balance is sufficient
            Balance -= data_price  # Deduct the amount from the balance
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"Mifi Data Recharge ({data_gb}GB) to {phone_number}", {-data_price / 100})   # Log transaction
            print(f"Mifi Data Recharge ({data_gb}GB) to {phone_number} Sent successfully.")
        else:
            print("Macsalaamo! Haraagaagu kugu ma filna.")
    else:
        print("loodiraha ma ahan mid jira")

    # After the transaction, re-read the balance from the file
    Balance = read_balance()  # Re-read updated balance from the file
    print(f"[-EVCPlus-] Haraagaaga waa ${Balance / 100:.2f}")



#uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

#77777777777777777777777777777777777777777777777777777777777777777777777777




# Function to handle Mifi packages (option 3 under Kaarka Hadalka)
def ugu_shub_qof_kale_mmt_options():
    clear_screen()  # Clear screen before showing options
    print("   Mifi Packages")
    print("1. Ku shubo data Mifi")

    mifi_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if mifi_option == '1':
        ku_shubo_data_mifi()  # Call function to handle data purchase
    else:
        print("Invalid option. Dib u day.")
        ugu_shub_qof_kale_mmt_options()  # Re-prompt if an invalid option is selected

# Function to handle Ku shubo data Mifi (under Mifi Packages)
def ugu_shub_qof_kale_mmt():
    clear_screen()
    print("1. Isbuucle (Weekly)")
    print("2. Maalinle (Daily)")
    print("3. Bille (Mifi)")

    data_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if data_option == '1':
        show_weekly_data_options()  # Show weekly data options
    elif data_option == '2':
        show_daily_data_options()  # Show daily data options
    elif data_option == '3':
        show_monthly_data_options()  # Show monthly data options
    else:
        print("Option not yet implemented.")  # Placeholder for invalid input

# Function to show weekly data options
def show_weekly_data_options():
    global Balance
    clear_screen()
    print("1. $5 = 10GB")
    print("2. $10 = 25GB")

    weekly_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if weekly_option == '1':
        data_price = 500  # Price for 10GB
        data_gb = 10
    elif weekly_option == '2':
        data_price = 100  # Price for 25GB
        data_gb = 25
    else:
        print("Invalid option. Dib u day.")
        show_weekly_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to show daily data options
def show_daily_data_options():
    global Balance
    clear_screen()
    print("1. $1 = 2GB")
    print("2. $2 = 5GB")

    daily_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if daily_option == '1':
        data_price = 10  # Price for 2GB
        data_gb = 2
    elif daily_option == '2':
        data_price = 20  # Price for 5GB
        data_gb = 5
    else:
        print("Invalid option. Dib u day.")
        show_daily_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to show monthly data options
def show_monthly_data_options():
    global Balance
    clear_screen()
    print("1. $20 = 40GB")
    print("2. $40 = 85GB")
    print("3. $60 = 150GB")
    print("4. $30 = Unlimited month")

    monthly_option = input().strip()  # No prompt, user selects an option
    clear_screen()

    if monthly_option == '1':
        data_price = 2000  # Price for 40GB
        data_gb = 40
    elif monthly_option == '2':
        data_price = 4000  # Price for 85GB
        data_gb = 85
    elif monthly_option == '3':
        data_price = 6000  # Price for 150GB
        data_gb = 150
    elif monthly_option == '4':
        data_price = 3000  # Price for unlimited
        data_gb = 'Unlimited'
    else:
        print("Invalid option. Dib u day.")
        show_monthly_data_options()  # Re-prompt if an invalid option is selected
        return

    process_data_purchase(data_price, data_gb)

# Function to process data purchase
def process_data_purchase(data_price, data_gb):
    global Balance
    # Ask for phone number
    while True:
        try:
            print("Fadlan Geli Mobile-ka")
            phone_number = int(input())
            phone_number = str(phone_number).strip()
            clear_screen()
            break
        except ValueError:
                print("Invalid data type")
    clear_screen()

    # Validate the phone number (must start with 61 or 77 and be 9 digits long)
    if (phone_number.startswith('61') or phone_number.startswith('77')) and len(phone_number) == 9:
        if Balance >= data_price:  # Check if the balance is sufficient
            Balance -= data_price  # Deduct the amount from the balance
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"Mifi Data Recharge ({data_gb}GB) to {phone_number}", -data_price / 100)   # Log transaction
            print(f"Mifi Data Recharge ({data_gb}GB) to {phone_number} Sent successfully.")
        else:
            print("Macsalaam. Haraagaagu kuma filna.")
    else:
        print("Numberka aad lacagta u direyso ma ahan mid sax ah ")
        print("Fadlan iska hubi")

    # After the transaction, re-read the balance from the file
    Balance = read_balance()  # Re-read updated balance from the file
    print(f"[-EVCPlus-] Haraagaaga waa ${Balance / 100:.2f}")






#88888888888888888888888888888888888888888888888888888888888888888888888888

def adjust_money(amount):
    min_amount = 0.01
    max_amount = 500

    # Validate the amount
    if amount < min_amount or amount > max_amount:
        return "Invalid input. The amount must be between 0.01 and 500"
    else:
        return amount



# Function to recharge the balance
def recharge_balance():
    global Balance
    MAX_LIMIT_CENTS = 50000  # $500 in cents

    print("Enter the amount you want to recharge")
    amount = input().strip()
    clear_screen()

    try:
        amount = float(amount)  # Convert input to float
        
        # Validate the recharge amount using adjust_money
        valid_amount = adjust_money(amount)
        if isinstance(valid_amount, str):
            print(valid_amount)  # Display error message for invalid input
            return

        amount_cents = int(valid_amount * 100)  # Convert dollars to cents

        if amount_cents > 0:  # Ensure the recharge amount is positive
            if Balance + amount_cents > MAX_LIMIT_CENTS:
                print(f"Your balance has reached the maximum limit, You can't recharge futrher")
                print()
                print("Connect your mobile money to your bank acount to enable seamless recharges")
                input()
                clear_screen()
                return

            Balance += amount_cents  # Add the amount to balance
            save_balance(Balance)  # Save the updated balance
            log_transaction("Recharge Balance", amount_cents /100)  # Log the transaction
            
            # Display the recharged amount with no decimal places if it's a whole number
            if valid_amount.is_integer():
                 print(f"You have successfully recharged your balance with an amount of ${valid_amount:.2f}")
                 print(f"Your currect balance is now ${Balance / 100:.2f}") 
                 date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
                 print(date_time)
        else:
            print("Invalid input")  # Handle negative or zero amount
    except ValueError:
        print("Invalid data input")  # Catch invalid inputs


# Function to handle options under bixi biil (option 3)
def show_bixi_bill_options():
    global Balance
    clear_screen()
    print("   Kaarka Hadalka")  # Title for Kaarka Hadalka
    print("1. Post paid")
    print("2. Ku Iibso")

    bixi_option = input().strip()  # No prompt, user selects an option
    clear_screen() 
    if bixi_option == '1':
        print("  Post paid") 
        print("1. Ogow Biilka")
        print("2. Bixi Bill")
        print("3. Kabixi Bill")

        post_paid_option = input().strip()
        clear_screen()
    if post_paid_option == '1':
        ogow_biilka_option()
    elif post_paid_option == '2':
        pay_biil_option()
    elif post_paid_option == '3':
        show_bixi_bill_options()
    else:
       print("Fadlan dooro number sax ah")
#showing ogow biilka option
def ogow_biilka_option():
       print("error occurred, please try again later")

#showing bixi biil submenu option
def pay_biil_option():
    global Balance
    print("Fadlan Geli Mobile-ka")
    number = input().strip()
    clear_screen()

    # Proceed to enter the amount, keep asking until a valid amount is provided
    while True:
        print("Fadlan Geli lacagta")
        amount = input().strip()
        clear_screen()

        try:
            # Try to convert the input to a float
            amount = float(amount)
            amount_cents = int(amount * 100)
            # Check if the amount is positive
            if amount > 0:
                break  # Exit loop if valid amount is entered
            else:
                print("Invalid input!")  # Amount must be positive
        except ValueError:
            print("You can only enter a number!")  # Handle invalid input
            ugu_shub_airtime()

    # Ask for confirmation
    print(f"Mahubtaa inaad ${amount:.2f} biil ahaan ugu dirtid qofka lambarkiisu yahay {number}?")
    print("1. Haa")
    print("2. Maya")
    confirmation = input().strip()
    clear_screen()

    if confirmation == '1':
        # Validation occurs ONLY AFTER user presses '1'
        # Check if the number starts with 61 or 77 and ensure it's exactly 9 digits long
        if (number.startswith('61') or number.startswith('77')) and len(number) != 9:
            print("Numberka aad biilka u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!.")  # Invalid number for 61 or 77 after confirmation
            return

        # Check if the number starts with 061 and ensure it's either 9 or 10 digits long
        elif number.startswith('061') and len(number) not in [9, 10]:
            print("Numberka aad biilka u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!.")  # Invalid number for 061 after confirmation
            return

        # If the number doesn't start with valid prefixes (061, 61, 77)
        elif not (number.startswith('061') or number.startswith('61') or number.startswith('77')):
            print("Numberka aad biilka u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!.")  # Invalid number due to invalid prefix
            return

        # If valid, check balance
        if amount_cents <= Balance:
            Balance -= amount_cents  # Deduct the amount from balance
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"Bixi biil {number}", -amount)  # Log the transaction
            print(f"Waxad ${amount} Biil ahaan ugu dirtay {number}")
            print(f"[-EVCPlus-] Haraagaaga waa ${Balance /100:.2f}")
            date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
            print(date_time)
            
        else:
            print("Haraaga xisaabtaadu kuguma filna, Mobile No:")
            print("252615820767")
    else:
        print("Mahadsanid!.")
 
 # Function to handle options under uwareeji (option 

def uwareeji_evcplus():
    global Balance
    clear_screen()
    
    while True:
        try:
            print("Fadlan Geli Mobile-ka")
            number = int(input(""))
            number = str(number)
            clear_screen()
            break
        except ValueError:
            print("Invalid data type")
        

    # Proceed to enter the amount, keep asking until a valid amount is provided
    while True:
        print("Fadlan Geli lacagta")
        amount = input().strip()
        
        
        clear_screen()

        # Check if the input is a valid float or int
        try:
            amount = float(amount)  # Convert input to float
            amount_cents = int(amount * 100) # Convert dollars to cents
            break  # Exit loop if a valid amount is entered
        except ValueError:
            print("You can only enter a valid number!")  # Catch invalid inputs
    # Ask for confirmation
    if amount.is_integer():
       print(f"Mahubtaa inaad ${amount} u wareejisid {number}?")
       print("1. Haa")
       print("2. Maya")
    else:
       print(f"Mahubtaa inaad ${amount:.2f} u wareejisid {number}?")
       print("1. Haa")
       print("2. Maya")
    confirmation = input().strip()
    clear_screen()
    
    if confirmation == '1':
        # Validation occurs ONLY AFTER the user presses '1'
        # Check if the number starts with 61 or 77 and ensure it's exactly 9 digits long
        if (number.startswith('61') or number.startswith('77')) and len(number) != 9:
            print("Numberkan ma diwaansana, ")
            print("si aad isku diwaan geliso garaac *770# ama laxiriir 141/101 ama")
            print("Whatsapp +252615000000")  # Invalid number for 61 or 77 after confirmation
            return
        # Check if the number starts with 061 and ensure it's either 9 or 10 digits long
        elif number.startswith('61') and len(number) not in [9, 10]:
            print("Numberka aad lacagta u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!")  # Invalid number for 061 after confirmation
            return

        # If the number doesn't start with valid prefixes (061, 61, 77)
        elif not (number.startswith('61') or number.startswith('77')):
            print("Numberka aad lacagta u direyso ma ahan mid sax ah,")
            print("fadlan iska hubi!")  # Invalid number due to invalid prefix
            return       
 
        # If valid, check balance
        if amount_cents <= Balance:
            Balance -= amount_cents  # Deduct the amount from balance in cents
            save_balance(Balance)  # Save the updated balance
            log_transaction(f"[-EVCPlus-] {amount:.2f} ayaad u wareejisay {number} ", -amount_cents / 100)  # Log the transaction
            if amount.is_integer():
                print(f"[-EVCPlus-] ${amount} ayaad u wareejisay {number}")
                print(f"Haraagaagu waa ${Balance / 100}")
                date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
                print(date_time)
                
                

            else:
                print(f"[-EVCPlus-] ${amount:.2f} ayaad u wareejisay {number}")
                    # Display the recharged amount with no decimal places if it's a whole number
                print(f"Haraagaagu waa ${Balance / 100:.2f}") 
                date_time = datetime.now().strftime("Date: %Y-%m-%d %H:%M:%S")
                print(date_time)
                
              
            
        else:
            print("Haraaga xisaabtaadu kuguma filna, Mobile No:")
            print("252615820767")
    else:
        print("Mahadsanid!")
  
# Function to handle options under Warbixin Kooban (option 5)
def show_warbixin_options():
    clear_screen()  # Clear screen before showing options
    print("   Warbixin Kooban")  # Title for Warbixin Kooban
    print("1. Last Action")
    print("2. Last 3 Actions")
    print("3. Email Me My Activity")
    warbixin_option = input().strip()
    clear_screen()

    if warbixin_option == '1':
        print(f"Last Action: {get_last_transaction()}")
    elif warbixin_option == '2':
        last_three = get_last_three_transactions()
        if last_three:
            print("Last 3 Actions:")
            for transaction in last_three:
                print(transaction.strip())
    elif warbixin_option == '3':
        email_activity()
    
    else:
        print("Fadlan dooro number sax ah!")  #cancel if the user choose invalid option

# Function to show options under Salaam Bank ( option 6)  
def show_salaaam_bank_options():
    clear_screen()
    print("   Salaam Bank")
    print("1. Ka Wareeji EVCPlus")
    
    salaam_bank_option = input().strip()
    clear_screen()
    if salaam_bank_option == '1':
       fadlan_dooro_xisaabta_bangiga()
    else:
        print("fadlan dooro number sax ah!")


# Function to choose options under ka wareeji evcplus
def fadlan_dooro_xisaabta_bangiga():
    global Balance
    
    print("   Fadlan dooro xisaabta Bangiga")
    print('1. SALAAM SOMALI BANK')
    print("2. Salaam Sch")
    print("3. Bank Beeraha")
    print("4. Daarusalaam Bank")
    print()
    print("These services are on maintenance, we are sorry for any problems")
    print("You can go ahead and check the status in our updates.")
    print("Thank you for your patience,")
    print()
    dooro_option = input().strip()
    clear_screen()
    if   dooro_option == '1':
         salaam_bank()
    elif dooro_option == '2':
         salaam_sch()
    elif dooro_option == '3':
         bank_beeraha()
    elif dooro_option == '4':
         daarusalaam_bank()
    else:
         fadlan_dooro_xisaabta_bangiga()
# function to hundle salaam bank ( one of the submenu options of option 6)
def salaam_bank():
    global balance
    print("Hello customers, we oplogize you that this service isn't still working propably")
    print("we will directly release this service on DECEMBER 8th 2024")
    print()
    print("please leave a comment, and share thought with us ✌")
    print()
    comment = input()
    clear_screen()
    print(comment)
    clear_screen()
    print("""Waxaan ku faraxsanahay in aad ka mid tahay macaamiisheena
sida joogtada ah u isticmaala adeegyada aan bixino,
fariintaada weey nasoo gaartey, cosigaagana waan tix gelin doonaa.
          """)
          
# function to hundle salaam Sch ( one of the submenu options of option 6)
def salaam_sch():
    global balance
    print("Hello customers, we oplogize you that this service isn't still working propably")
    print("we will directly release this service on DECEMBER 8th 2024")
    print()
    print("please leave a comment")
    print()
    comment = input()
    clear_screen()
    print(comment)
    clear_screen()
    print("""We are happy that you are one of our valued customers,
who consistenly use 
          """)    
    
# function to hundle Bank beeraha ( one of the submenu options of option 6)
def bank_beeraha():
    global balance
    print("Hello customers, we oplogize you that this service isn't still working propably")
    print("we will directly release this service on DECEMBER 8th 2024")
    print()
    print("please leave a comment")
    print()
    comment = input()
    clear_screen()
    print(comment)
    clear_screen()
    print("""Waxaan ku faraxsanahay in aad ka mid tahay macaamiisheena
sida joogtada ah u isticmaala adeegyada aan bixino,
fariintaada weey nasoo gaartey, cosigaagana waan tix gelin doonaa.
          """)    

# function to hundle salaam Sch ( one of the submenu options of option 6)
def daarusalaam_bank():
    global balance
    print("Hello customers, we oplogize you that this service isn't still working propably")
    print("we will directly release this service on DECEMBER 8th 2024")
    print()
    print("please leave a comment and share us your thoughts")
    print()
    comment = input()
    clear_screen()
    print(comment)
    clear_screen()
    print("""Waxaan ku faraxsanahay in aad ka mid tahay macaamiisheena
sida joogtada ah u isticmaala adeegyada aan bixino,
fariintaada weey nasoo gaartey, cosigaagana waan tix gelin doonaa.
          """)  
# Function to show options under Maareynta (option 7)
def show_maareynta_options():
    clear_screen()  # Clear screen before showing options
    print("   Maareynta")  # Title for Maareynta
    print("1. Bedel lambarka sirta ah")
    print("2. Bedel luuqadda")
    print("3. Wargelin mobile lumay")
    print("4. Lacag xirasho")
    print("5. U celi lacag qaldantay")

    maareynta_option = input().strip()
    clear_screen()
    if maareynta_option == '1':
           change_pin()  # Call function to change PIN
    elif maareynta_option == '2':
        change_lang()
    
# Function to change PIN
def change_pin():
    global password
    print("Geli PIN-ka cusub:")
    new_pin = input().strip()
    clear_screen()

    if new_pin.isdigit() and len(new_pin) == 4:
        print("Ku celi PIN-ka cusub:")
        confirm_pin = input().strip()
        clear_screen()

        if new_pin == confirm_pin:
            password = int(new_pin)
            save_pin(password)  # Save the new PIN to the file
            print("Hambalyo! Waad ku guulaysatay in aad bedesho Pin-kaaga.")
        else:
            print("INPUT MISMATCH.")
            print("Hubi PIN-kaaga")
            change_pin()  # Re-prompt if the confirmation doesn't match
            clear_screen()
    else:
        print("Invalid Input Format (DataType).")
        change_pin()  # Re-prompt if the new PIN is invalid
def change_lang():
    print("   Change Lanaguage")
    print("1. Somali")
    print("1. English")
    change_lang = int(input(""))
    clear_screen()
    if change_lang == 1:
        print("Hambalyo waad ku guulaysatey in aad bedesho luuqada")
    elif change_lang == 2:
        print("congrats you seccessfully changed the language")
        

# Start the program
clear_screen()    # Clear the screen before starting
print("ENG: ABAAS CAAQIL 🏫")
check_code()  # Call the function to check input code




