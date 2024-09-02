from sql_db import *

if __name__ == '__main__':
    print("Welcome to Gold Bank.")
    
    # Gather customer information
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your email: ")

    # Connect to the database and create tables if they don't exist
    conn = create_tables()

    # Check if the customer already exists
    existing_customer = check_customer_exists(conn, firstName, lastName, email)

    if existing_customer:
        print("Customer already exists in the system.")
        acc = input("Would you like to view your account details or open a new account? (View/Open/Exit): ").strip().lower()
        
        if acc == "view":
            # Assuming you would implement a function to display account details here
            print("Here are your account details:")
            # Display the customer's account details
            # account_details = display_account_details(conn, existing_customer['id'])
            # print(account_details)
        elif acc == "open":
            account_number = input("Enter the account number you would like to open: ")
            balance = float(input("Enter the initial balance for your new account: "))
            create_account(conn, account_number, balance, existing_customer[0])
            print(f"New account opened for {firstName} {lastName}.")
        else:
            print("Goodbye!")
    else:
        # If customer doesn't exist, create a new customer
        create_customer(conn, firstName, lastName, email)
        print(f"Customer {firstName} {lastName} added successfully!")

        # Optionally, prompt to create an account for the new customer
        acc = input("Would you like to open an account? (Y/N): ").strip().upper()
        if acc == 'Y':
            account_number = input("Enter the account number you would like to open: ")
            balance = float(input("Enter the initial balance for your account: "))
            new_customer = check_customer_exists(conn, firstName, lastName, email)
            create_account(conn, account_number, balance, new_customer[0])
            print(f"Account opened for {firstName} {lastName}.")
        else:
            print("No account created.")
