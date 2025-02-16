from flask import Flask
from config import Config
from models import db, init_db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
init_db(app)

# Import and register Blueprints
from routes.diet_plan import diet_plan_bp
from routes.gamification import gamification_bp
from routes.water_tracker import water_tracker_bp
from routes.calorie_tracker import calorie_tracker_bp
from routes.daily_goals import daily_goals_bp
from routes.recipes import recipes_bp  # ✅ Import recipes

app.register_blueprint(diet_plan_bp, url_prefix='/diet')
app.register_blueprint(gamification_bp, url_prefix='/gamification')
app.register_blueprint(water_tracker_bp, url_prefix='/water')
app.register_blueprint(calorie_tracker_bp, url_prefix='/calories')
app.register_blueprint(daily_goals_bp, url_prefix='/goals')
app.register_blueprint(recipes_bp, url_prefix='/recipes')  # ✅ Register recipes API

if __name__ == '__main__':
    app.run(debug=True)
