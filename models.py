from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON  # Ensure JSON support


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class DietPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    plan_type = db.Column(db.String(10))  # "30-day" or "60-day"
    meal_plan = db.Column(db.JSON)  # ✅ Ensure full 30/60 days are stored

class WaterTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, nullable=False)
    water_intake = db.Column(db.Float, nullable=False)  # Liters

class CalorieTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, nullable=False)
    calories = db.Column(db.Integer, nullable=False)  # Total calories for the day

class DailyGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    goal_description = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)  # ✅ Track if goal is completed

class Gamification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    points = db.Column(db.Integer, default=0)  # ✅ Tracks total reward points
    badges = db.Column(db.String(255), default="")  # ✅ Stores earned badges

def init_db(app):
    """Initialize the database with the application context."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
