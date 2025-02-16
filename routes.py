from flask import Blueprint, request, jsonify
from models import add_review, get_all_reviews

reviews_bp = Blueprint("reviews", __name__)

# Route to add a review
@reviews_bp.route("/add", methods=["POST"])
def add_new_review():
    data = request.json
    if "name" in data and "review" in data and "rating" in data:
        add_review(data["name"], data["review"], data["rating"])
        return jsonify({"message": "Review added successfully!"}), 201
    return jsonify({"error": "Missing fields"}), 400

# Route to get all reviews
@reviews_bp.route("/get-all", methods=["GET"])
def fetch_reviews():
    reviews = get_all_reviews()
    return jsonify({"reviews": reviews}), 200
