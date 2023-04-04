import os
import stripe

from balance.balance import retrieve_balance, retrieve_balance_transaction, list_balance_transactions
from payment_intent.payment_intent import create_payment_intent, retreive_payment_intent, update_payment_intent, confirm_payment_intent, capture_payment_intent, cancel_payment_intent, list_payment_intents, search_payment_intent
from payouts.payouts import create_payout, retrieve_payout, update_payout, list_payouts, cancel_payout
from customer.customer import create_customer, retrieve_customer, update_customer, delete_customer, list_customers
from paymentmethods.paymentmethods import create_payment_method, retrieve_payment_method, retrieve_customer_payment_method, update_payment_method,list_payment_methods, list_customer_payment_methods, attach_payment_method_to_customer, detach_payment_method_to_customer
from products.products import create_product, retrieve_product, update_product, list_products, delete_product, search_product
from price.price import create_price, retrieve_price, retrieve_price_list
from checkout_sessions.checkout_sessions import create_checkout_sessions, expire_checkout_session, retrieve_checkout_session, list_checkout_sessions, retrieve_checkout_session_list_line_items
from payment_link.payment_link import create_payment_link, retrieve_payment_link, update_payment_link, list_payment_links, retrieve_payment_link_line_items
from invoice.invoice import create_invoice, retrieve_invoice, update_invoice, delete_invoice, list_invoices
from subscriptions.subscriptions import create_subscriptions, retrieve_subscription, update_subscriptions, cancel_subscriptions, list_subscriptions

from flask import Flask, render_template, request

from dotenv import load_dotenv

load_dotenv()

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

# BALANCE ENDPOINTS

@app.route('/getBalance', methods=['GET'])
def balance_retreive():
    balance = retrieve_balance()
    return balance

@app.route('/balanceTransaction/<id>', methods=['GET'])
def balance_transaction_retreive(id):
    balance = retrieve_balance_transaction(id)
    return balance

@app.route('/balanceTransactionsList', methods=['GET'])
def balance_transactions_list():
    balance = list_balance_transactions()
    return balance

# PAYMENT INTENTS ENDPOINTS

@app.route('/createPaymentIntents', methods=['POST'])
def createPaymentIntent():
    paymentIntent = create_payment_intent()
    return paymentIntent
    
@app.route('/getPaymentIntent/<id>', methods=['GET'])
def retreivePaymentIntent(id):
    payment = retreive_payment_intent(id)
    return payment

@app.route('/updatePaymentIntent/<id>', methods=['POST'])
def updatePaymentIntent(id):
    payment = update_payment_intent(id)
    return payment

@app.route('/confirmPaymentIntent/<id>', methods=['POST'])
def confirmPaymentIntent(id):
    payment = confirm_payment_intent(id)
    return payment

@app.route('/capturePaymentIntent/<id>', methods=['POST'])
def capturePaymentIntent(id):
    payment = capture_payment_intent(id)
    return payment

@app.route('/cancelPaymentIntent/<id>', methods=['DELETE'])
def cancelPaymentIntent(id):
    payment = cancel_payment_intent(id)
    return payment

@app.route('/listPaymentIntents', methods=['GET'])
def listPaymentIntents():
    payments = list_payment_intents()
    return payments

@app.route('/searchPaymentIntent/<status>/<order_id>', methods=['GET'])
def searchPaymentIntent(status, order_id):
    payment = search_payment_intent(status, order_id)
    return payment

# PAYOUT ENDPOINTS

@app.route('/createPayout', methods=['POST'])
def createPayout():
    payout = create_payout()
    return payout

@app.route('/retrievePayout/<id>', methods=['GET'])
def retrievePayout(id):
    payout = retrieve_payout(id)
    return payout

@app.route('/updatePayout/<id>', methods=['POST'])
def updatePayout(id):
    payout = update_payout(id)
    return payout

@app.route('/listPayout', methods=['GET'])
def listPayout():
    payout = list_payouts()
    return payout

@app.route('/cancelPayout', methods=['POST'])
def cancelPayout(id):
    payout = cancel_payout(id)
    return payout

# CUSTOMER ENDPOINTS

@app.route('/createCustomer', methods=['POST'])
def createCustomer():
    customer = create_customer()
    return customer

@app.route('/retrieveCustomer/<id>', methods=['GET'])
def retrieveCustomer(id):
    customer = retrieve_customer(id)
    return customer

@app.route('/updateCustomer/<id>', methods=['POST'])
def updateCustomer(id):
    customer = update_customer(id)
    return customer

@app.route('/deleteCustomer/<id>', methods=['DELETE'])
def deleteCustomer(id):
    customer = delete_customer(id)
    return customer

@app.route('/listCustomer', methods=['GET'])
def listCustomer():
    customers = list_customers()
    return customers

# PAYMENT METHOD ENDPOINTS

@app.route('/createPaymentmethod', methods=['POST'])
def createPaymentmethod():
    payment_method = create_payment_method()
    return payment_method

@app.route('/retrievePaymentmethod/<id>', methods=['GET'])
def retrievePaymentmethod(id):
    payment_method = retrieve_payment_method(id)
    return payment_method

@app.route('/retrieveCustomerPaymentmethod/<cus_id>/<pm_id>', methods=['GET'])
def retrieveCustomerPaymentmethod(cus_id, pm_id):
    payment_method = retrieve_customer_payment_method(cus_id, pm_id)
    return payment_method

@app.route('/updatePaymentmethod/<id>', methods=['POST'])
def updatePaymentmethod(id):
    payment_method = update_payment_method(id)
    return payment_method

@app.route('/listPaymentmethods/<id>', methods=['GET'])
def listPaymentmethods(id):
    payment_method = list_payment_methods(id)
    return payment_method

@app.route('/listCustomerPaymentmethods/<id>', methods=['GET'])
def listCustomerPaymentmethods(id):
    payment_method = list_customer_payment_methods(id)
    return payment_method

@app.route('/attachCustomerPaymentmethod/<id>', methods=['POST'])
def attachCustomerPaymentmethod(id):
    payment_method = attach_payment_method_to_customer(id)
    return payment_method

@app.route('/detachCustomerPaymentmethod/<id>', methods=['POST'])
def detachCustomerPaymentmethod(id):
    payment_method = detach_payment_method_to_customer(id)
    return payment_method

# PRODUCT ENDPOINTS

@app.route('/createProduct', methods=['POST'])
def createProduct():
    product = create_product()
    return product

@app.route('/retrieveProduct/<id>', methods=['GET'])
def retrieveProduct(id):
    product = retrieve_product(id)
    return product

@app.route('/updateProduct/<id>', methods=['POST'])
def updateProduct(id):
    product = update_product(id)
    return product

@app.route('/listProduct', methods=['GET'])
def listProducts():
    product = list_products()
    return product

@app.route('/deleteProduct/<id>', methods=['DELETE'])
def deleteProduct(id):
    product = delete_product(id)
    return product

@app.route('/searchProduct/<active>/<order_id>', methods=['GET'])
def searchProduct(active, order_id):
    product=search_product()
    return product

# PRICE ENDPOINTS

@app.route('/createPrice', methods=['POST'])
def createPrice():
    price = create_price()
    return price

@app.route('/retrievePrice/<id>', methods=['GET'])
def retrievePrice(id):
    price=retrieve_price(id)
    return price

@app.route('/retrievePriceList', methods=['GET'])
def retrievePriceList():
    price=retrieve_price_list()
    return price

# CHECKOUT SESSION ENDPOINTS

@app.route('/createCheckoutSession', methods=['POST'])
def createCheckoutSession():
    checkout_session = create_checkout_sessions()
    return checkout_session

@app.route('/expireCheckoutSession/<id>', methods=['GET'])
def expireCheckoutSession(id):
    checkout_session=expire_checkout_session(id)
    return checkout_session

@app.route('/retrieveCheckoutSession/<id>', methods=['GET'])
def retrieveCheckoutSession(id):
    checkout_session=retrieve_checkout_session(id)
    return checkout_session

@app.route('/listCheckoutSessions', methods=['GET'])
def listCheckoutSessions():
    checkout_session=list_checkout_sessions()
    return checkout_session

@app.route('/listCheckoutSessionsLineitems/<id>', methods=['GET'])
def listCheckoutSessionsLineitems(id):
    checkout_session=retrieve_checkout_session_list_line_items(id)
    return checkout_session

# PAYMENT LINKS

@app.route('/createPaymentLink', methods=['POST'])
def createPaymentLink():
    payment_link=create_payment_link()
    return payment_link

@app.route('/retrievePaymentLink/<id>', methods=['GET'])
def retrievePaymentLink(id):
    payment_link=retrieve_payment_link(id)
    return payment_link

@app.route('/updatePaymentLink/<id>', methods=['POST'])
def updatePaymentLin(id):
    payment_link=update_payment_link(id)
    return payment_link

@app.route('/listPaymentLinks', methods=['GET'])
def listPaymentLinks():
    payment_link=list_payment_links()
    return payment_link

@app.route('/listPaymentLinkLineItems', methods=['GET'])
def listPaymentLinkLineItems(id):
    payment_link=retrieve_payment_link_line_items(id)
    return payment_link

# INVOICE ENDPOINTS

@app.route('/createInvoice', methods=['POST'])
def createInvoice():
    invoice=create_invoice()
    return invoice

@app.route('/retrieveInvoice/<id>', methods=['GET'])
def retrieveInvoice(id):
    invoice=retrieve_invoice(id)
    return invoice

@app.route('/updateInvoice/<id>', methods=['POST'])
def updateInvoice(id):
    invoice=update_invoice(id)
    return invoice

@app.route('/deleteInvoice/<id>', methods=['DELETE'])
def deleteInvoice(id):
    invoice=delete_invoice(id)
    return invoice

@app.route('/listInvoice', methods=['GET'])
def listInvoice():
    invoice=list_invoices()
    return invoice

# SUBSCRIPTION ENDPOINTS

@app.route('/createSubscription', methods=['POST'])
def createSubscription():
    invoice=create_subscriptions()
    return invoice

@app.route('/retrieveSubscription/<id>', methods=['GET'])
def retrieveSubscription(id):
    invoice=retrieve_subscription(id)
    return invoice

@app.route('/updateSubscription/<id>', methods=['POST'])
def updateSubscription(id):
    invoice=update_subscriptions(id)
    return invoice

@app.route('/deleteSubscription/<id>', methods=['DELETE'])
def deleteSubscription(id):
    invoice=cancel_subscriptions(id)
    return invoice

@app.route('/listSubscription', methods=['GET'])
def listSubscription():
    invoice=list_subscriptions()
    return invoice

# @app.route('/')
# def index():
#     return render_template('index.html', key=stripe_keys['publishable_key'])

# @app.route('/charge', methods=['POST'])
# def charge():
#     # Amount in cents
#     amount = 500

#     customer = stripe.Customer.create(
#         description="My First Test Customer (created for API docs at https://www.stripe.com/docs/api)",
#         # source=request.form['stripeToken']
#     )

#     charge = stripe.Charge.create(
#         customer=customer.id,
#         amount=amount,
#         currency='usd',
#         description='Flask Charge'
#     )

#     return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)