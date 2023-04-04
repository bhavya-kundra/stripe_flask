import json
import os
import stripe

from flask import jsonify, request

from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ['SECRET_KEY']


def create_product():
    try:
        data = json.loads(request.data)
        if "name" in data:
            product = stripe.Product.create(name=data["name"])
            return product
        else:
            return {"msg": "No name found to create product"}
    except Exception as e:
        return jsonify(error=str(e)), 500


def retrieve_product(id):
    try:
        product = stripe.Product.retrieve(id)
        return product
    except Exception as e:
        return jsonify(error=str(e)), 500


def update_product(id):
    try:
        data=json.loads(request.data)
        product=stripe.Product.modify(id, metadata=data['metadata'],)
        return product
    except Exception as e:
        return jsonify(error=str(e)), 500


def list_products():
    try:
        product = stripe.Product.list(limit=3)
        return product
    except Exception as e:
        return jsonify(error=str(e)), 500


def delete_product(id):
    try:
        product = stripe.Product.delete(id,)
        return product
    except Exception as e:
        return jsonify(error=str(e)), 500


def search_product():
    try:
        product=stripe.Product.search(query="active:'{active}' AND metadata['order_id']:'{order_id}'")
        return product
    except Exception as e:
        return jsonify(error=str(e)), 500
