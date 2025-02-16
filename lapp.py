from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash  # For checking hashed passwords
import re
from flask_cors import CORS

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/nutrition-app"  # Your local MongoDB URI
mongo = PyMongo(app)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def index():
    return render_template('signup.html')  # Render the sign-up form

# Sign-up route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    full_name = data.get('fullName')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    # Validation checks
    if not full_name or not email or not password:
        return jsonify({'error': 'Please fill out all fields'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Check if the user already exists
    user_collection = mongo.db.users
    existing_user = user_collection.find_one({'email': email})

    if existing_user:
        return jsonify({'error': 'User already exists'}), 400

    # Save the new user to MongoDB
    user_data = {
        'fullName': full_name,
        'email': email,
        'password': hashed_password
    }
    user_collection.insert_one(user_data)

    return jsonify({'message': 'User created successfully'}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    # Get data from the frontend (login form)
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Please provide both email and password.'}), 400

    # Find user by email
    user_collection = mongo.db.users
    user = user_collection.find_one({'email': email})

    if not user:
        return jsonify({'error': 'Invalid email or password.'}), 400

    # Check if the password is correct (compare hashed password)
    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid email or password.'}), 400

    return jsonify({'message': 'Login successful!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
