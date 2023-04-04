import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']

def create_price():
    try:
        data=json.loads(request.data)
        price=stripe.Price.create(
            unit_amount=data["unit_amount"],
            currency=data["currency"],
            recurring=data["recurring"],
            product=data["product"],
        )
        return price
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_price(id):
    try:
        price=stripe.Price.retrieve(id,)
        return price
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_price_list():
    try:
        price=stripe.Price.list(limit=3)
        return price
    except Exception as e:
        return jsonify(error=str(e)), 500
