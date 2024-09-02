import email
from sql_db import create_customer

class customer:
    def __init__(self, firstName, lastName):
        pass

    def open_account(self, firstName, lastName):
        create_customer(self.conn, firstName, lastName, email)
        print(f"Account opened for {firstName} {lastName}")
       

    
        
        
