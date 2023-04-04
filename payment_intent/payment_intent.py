import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']

def create_payment_intent():
    try:
        data=json.loads(request.data)
        if "amount" in data:
            try:
                payment = stripe.PaymentIntent.create(amount=data["amount"], currency='inr')
                # return jsonify({"clientSecret": payment["client_secret"]})
                return payment
            except ValueError as e:
                return jsonify(error=str(e)), 400
        else:
            return jsonify(error="No amount to pay in request"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500


def retreive_payment_intent(id):
    try:
        payment = stripe.PaymentIntent.retrieve(id,)
        return payment
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_payment_intent(id):
    try:
        data = stripe.PaymentIntent.modify(id, metadata={"order_id": "6735"},)
        return data
    except Exception as e:
        return jsonify(error=str(e)), 500


def confirm_payment_intent(id):
    try:
        confirm_payment = stripe.PaymentIntent.confirm(id, payment_method="pm_card_visa",)
        return confirm_payment
    except Exception as e:
        return jsonify(error=str(e)), 500


def capture_payment_intent(id):
    try:
        capture_payment=stripe.PaymentIntent.capture(id, )
        return capture_payment
    except Exception as e:
        return jsonify(error=str(e)), 500


def cancel_payment_intent(id):
    try:
        cancel_payment = stripe.PaymentIntent.cancel(id,)
        return cancel_payment
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_payment_intents():
    try:
        list_payment_intent = stripe.PaymentIntent.list(limit=3)
        return list_payment_intent
    except Exception as e:
        return jsonify(error=str(e)), 500


def search_payment_intent(status, order_id):
    try:
        search_payment_intent = stripe.PaymentIntent.search(query="status:{status} AND metadata['order_id']:{order_id}",)
        return search_payment_intent
    except Exception as e:
        return jsonify(error=str(e)), 500
