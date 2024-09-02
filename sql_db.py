import sqlite3

def create_tables():
    create_tables_statements = [
        """CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            email TEXT NOT NULL
        )""",
        
        """CREATE TABLE IF NOT EXISTS account (
            account_id INTEGER PRIMARY KEY,
            account_number TEXT NOT NULL,
            balance REAL NOT NULL,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
        )"""
    ]
    

    try:        
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        for statement in create_tables_statements:
            cursor.execute(statement)
    except sqlite3.Error as e:
        print(e)
    
    print("Tables created successfully.")
    print("Account tables created successfully.")
    return conn


    


def create_account(conn, account_number, balance, customer_id):
    statement = """ INSERT INTO account (account_number, balance, customer_id)  VALUES (?, ?, ?)   """
    cursor = conn.cursor()
    cursor.execute(statement, (account_number, balance, customer_id))
    conn.commit()
    print("Account added successfully!")
    
   
def create_customer(conn, firstName, lastName, email):
    statement = """ INSERT INTO customer (firstName, lastName, email) VALUES (?, ?, ?) """
    cursor = conn.cursor()
    cursor.execute(statement, (firstName, lastName, email))
    print("Customer added successfully!")


def display_customer_table(conn):
    statement = """ SELECT * FROM customer  """
    cursor = conn.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    return result

def display_account_table(conn):
    statement = """ SELECT * FROM account  """
    cursor = conn.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    return result    

    
def check_customer_exists(conn, firstName, lastName, email):
    statement = """SELECT * FROM customer WHERE firstName = ? AND lastName = ? AND email = ?"""
    cursor = conn.cursor()
    cursor.execute(statement, (firstName, lastName, email))
    customer = cursor.fetchone()
        
    
    return customer

def check_customer_account(conn, account_number, balance):
    statement = """ SELECT * FROM account WHERE customer_id = ?"""
    cursor = conn.cursor()
    cursor.execute(statement, (account_number, balance))
    account = account.fetchone()
    return account
    