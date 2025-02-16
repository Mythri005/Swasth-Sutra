from db import reviews_collection

# Function to insert a review
def add_review(name, review, rating):
    review_data = {"name": name, "review": review, "rating": rating}
    return reviews_collection.insert_one(review_data)

# Function to fetch all reviews
def get_all_reviews():
    return list(reviews_collection.find({}, {"_id": 0}))  # Hide MongoDB _id
