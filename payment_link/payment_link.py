import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']


def create_payment_link():
    try:
        data = json.loads(request.data)
        if 'line_items' in data:
            payment_link=stripe.PaymentLink.create(line_items=data['line_items'])
            return payment_link
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_payment_link(id):
    try:
        payment_link=stripe.PaymentLink.retrieve(id,)
        return payment_link
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_payment_link(id):
    try:
        data=json.loads(request.data)
        payment_link=stripe.PaymentLink.modify(id, active=data['active'],)
        return payment_link
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_payment_links():
    try:
        payment_link=stripe.PaymentLink.list()
        return payment_link
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_payment_link_line_items(id):
    try:
        payment_link=stripe.PaymentLink.list_line_items(id, limit=3)
        return payment_link
    except Exception as e:
        return jsonify(error=str(e)), 500
