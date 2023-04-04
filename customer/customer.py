import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']


def create_customer():
    try:
        data = json.loads(request.data)
        customer = stripe.Customer.create(description=data['description'],)
        return customer
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_customer(id):
    try:
        customer = stripe.Customer.retrieve(id)
        return customer
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_customer(id):
    try:
        customer = stripe.Customer.modify(id, metadata={"order_id": "6735"},)
        return customer
    except Exception as e:
        return jsonify(error=str(e)), 500


def delete_customer(id):
    try:
        customer = stripe.Customer.delete(id)
        return customer
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_customers():
    try:
        customers = stripe.Customer.list(limit=3)
        return customers
    except Exception as e:
        return jsonify(error=str(e)), 500
