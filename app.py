from flask import Flask, render_template, request, redirect, url_for
from sql_db import (
    create_tables,
    create_customer,
    create_account,
    display_customer_table,
    display_account_table,
)

app = Flask(__name__)

# Initialize database connection
conn = create_tables()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers')
def customers():
    customers = display_customer_table(conn)
    return render_template('customers.html', customers=customers)


@app.route('/accounts')
def accounts():
    accounts = display_account_table(conn)
    return render_template('accounts.html', accounts=accounts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        create_customer(conn, first_name, last_name, email)
        conn.commit()
        return redirect(url_for('customers'))
    return render_template('register.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account_route():
    if request.method == 'POST':
        account_number = request.form['account_number']
        balance = float(request.form['balance'])
        customer_id = request.form['customer_id']
        create_account(conn, account_number, balance, customer_id)
        conn.commit()
        return redirect(url_for('accounts'))
    customers = display_customer_table(conn)
    return render_template('create_account.html', customers=customers)


if __name__ == '__main__':
    app.run(debug=True)
