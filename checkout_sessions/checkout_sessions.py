import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']

def create_checkout_sessions():
    try:
        data=json.loads(request.data)
        checkout_session = stripe.checkout.Session.create(
            success_url=data["success_url"],
            line_items=data["line_items"],
            mode=data["mode"],)
        return checkout_session
    except Exception as e:
        return jsonify(error=str(e)), 500


def expire_checkout_session(id):
    try:
        checkout_session=stripe.checkout.Session.expire(id,)
        return checkout_session
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_checkout_session(id):
    try:
        checkout_session=stripe.checkout.Session.retrieve(id,)
        return checkout_session
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_checkout_sessions():
    try:
        checkout_session=stripe.checkout.Session.list(limit=3)
        return checkout_session
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_checkout_session_list_line_items(id):
    try:
        checkout_session=stripe.checkout.Session.list_line_items(id, limit=5)
        return checkout_session
    except Exception as e:
        return jsonify(error=str(e)), 500
    