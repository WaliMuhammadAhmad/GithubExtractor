from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return jsonify({"message": "Welcome to the JUnit Extractor API!"})

@main_routes.route('/api/test')
def test():
    return jsonify({"message": "This is a test endpoint!"})