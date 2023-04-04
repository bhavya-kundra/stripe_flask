import os
import stripe

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']

def retrieve_balance():
    balance = stripe.Balance.retrieve()
    return balance


def retrieve_balance_transaction(id):
    balance_transaction = stripe.BalanceTransaction.retrieve(id,)
    return balance_transaction


def list_balance_transactions():
    list_transactions = stripe.BalanceTransaction.list(limit=3)
    print(list_transactions)
    return list_transactions


# "txn_1032HU2eZvKYlo2CEPtcnUvl"

# retrieve_balance_transaction("txn_1032HU2eZvKYlo2CEPtcnUvl")

# list_balance_transactions()