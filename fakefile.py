

import random
from atm import Account, db
from faker import Faker



def fake_account_number():
	account_number = random.randint(100000, 999999)
	while Account.query.filter_by(account_number=account_number).first() != None:
		account_number = random.randint(100000, 999999)
	return account_number


def fake_pin():
	return random.randint(100, 999)

def fake_balance():
	return random.randint(0, 10000)

def fake_account():
	return Account(
		account_number=fake_account_number(),
		pin=fake_pin(),
		balance=fake_balance()
		)
def generate_accounts(max_n):
	for n in range(max_n):
		account = fake_account()
		db.session.add(account)

	db.session.commit()

def generate_names():
	
	fake = Faker()
	accounts = Account.query.all()
	for account in accounts:
		account.names = fake.name()

		# account.creditcard_number = fake.credit_card_number()
	db.session.commit()





	




# generate_accounts(1000)
generate_names()




		









