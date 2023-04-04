import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']

def create_payout():
    try:
        data = json.loads(request.data)
        if "amount" in data:
            try:
                payout = stripe.Payout.create(amount=data["amount"], currency="inr")
                return payout
            except ValueError as e:
                return jsonify(error=str(e)), 400
        else:
            return jsonify(error="No amount to pay in request"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_payout(id):
    try:
        payout = stripe.Payout.retrieve(id,)
        return payout
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_payout():
    try:
        payout = stripe.Payout.modify(id,
        metadata={"order_id": "6735"},)
        return payout
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_payouts():
    try:
        payout_list = stripe.Payout.list(limit=3)
        return payout_list
    except Exception as e:
        return jsonify(error=str(e)), 500


def cancel_payout(id):
    try:
        payout_cancel = stripe.Payout.cancel(id)
        return payout_cancel
    except Exception as e:
        return jsonify(error=str(e)), 500
