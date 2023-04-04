import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']


def create_subscriptions():
    try:
        data=json.loads(request.data)
        if "customer" and "items" in data:
            subscription=stripe.Subscription.create(customer=data["customer"], items=data["items"])
            return subscription
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_subscription(id):
    try:
        subscription=stripe.Subscription.retrieve(id,)
        return subscription
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_subscriptions(id):
    try:
        data=json.loads(request.data)
        subscription=stripe.Subscription.modify(id, metadata=data['metadata'])
        return subscription
    except Exception as e:
        return jsonify(error=str(e)), 500


def cancel_subscriptions(id):
    try:
        subscription=stripe.Subscription.delete(id)
        return subscription
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_subscriptions():
    try:
        subscription=stripe.Subscription.list(limit=3)
        return subscription
    except Exception as e:
        return jsonify(error=str(e)), 500
