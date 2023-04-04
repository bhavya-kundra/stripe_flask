import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']


def create_payment_method():
    try:
        data = json.loads(request.data)
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
            "number": data["number"],
            "exp_month": data["exp_month"],
            "exp_year": data["exp_year"],
            "cvc": data["cvc"]
            },
        )
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_payment_method(id):
    try:
        payment_method = stripe.PaymentMethod.retrieve(id,)
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_customer_payment_method(cus_id, pm_id):
    try:
        payment_method = stripe.Customer.retrieve_payment_method(cus_id, pm_id)
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_payment_method(id):
    try:
        data = json.loads(request.data)
        payment_method = stripe.PaymentMethod.modify(id, metadata=data['metadata'],)
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_payment_methods(id):
    try:
        payment_method = stripe.PaymentMethod.list(
            customer=id,
            type="card",)
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500
    

def list_customer_payment_methods(id):
    try:
        payment_method = stripe.Customer.list_payment_methods(
        id, type="card",)
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500


def attach_payment_method_to_customer(id):
    try:
        data = json.loads(request.data)
        if "customer" in data:
            payment_method = stripe.PaymentMethod.attach(id, customer=data["customer"],)
            return payment_method
        else:
            return {
                "msg": "No customer found to be attached by payment method"
            }
    except Exception as e:
        return jsonify(error=str(e)), 500


def detach_payment_method_to_customer(id):
    try:
        payment_method = stripe.PaymentMethod.detach(id,)
        return payment_method
    except Exception as e:
        return jsonify(error=str(e)), 500
