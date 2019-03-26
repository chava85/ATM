from flask import Flask
from flask import render_template, request, url_for, redirect



from atm import Account, app
from faker import Faker


@app.route("/", methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		account_number = request.form['account-number']
		pin = request.form['pin']

		account = Account.query.filter_by(account_number=account_number).first()
		if account.pin == int(request.form['pin']):
			return redirect(url_for('menu',account_number = account_number))


	return render_template('index.html')

@app.route('/menu/<int:account_number>/')
def menu(account_number):
	account = Account.query.filter_by(account_number=account_number).first()
	return render_template('menu.html', balance=account.balance)





# Web ATM project

# Create a web interface for an ATM using Bootstrap
# We should be able to login with a account number and PIN
# We do not need to have a signup form, you can insert the data in the db manually
# When a user tries to log in, you need to check that their account number and PIN are correct based on the info you have in the db
# When the add / remove money from the account you need to take it off or add it to the balance