import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']


def create_invoice():
    try:
        data=json.loads(request.data)
        if "customer" in data:
            invoice=stripe.Invoice.create()
            return invoice
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_invoice(id):
    try:
        invoice=stripe.Invoice.retrieve(id,)
        return invoice
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_invoice(id):
    try:
        data=json.loads(request.data)
        invoice=stripe.Invoice.modify(id, data['metadata'],)
        return invoice
    except Exception as e:
        return jsonify(error=str(e)), 500


def delete_invoice(id):
    try:
        invoice=stripe.Invoice.delete(id)
        return invoice
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_invoices():
    try:
        invoice=stripe.Invoice.list()
        return invoice
    except Exception as e:
        return jsonify(error=str(e)), 500
