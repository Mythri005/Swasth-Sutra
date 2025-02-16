from flask import Blueprint, jsonify
import json
import os

recipes_bp = Blueprint('recipes', __name__)

# Use absolute path for recipes.json
RECIPES_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../recipes.json"))

def load_recipes():
    try:
        with open(RECIPES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": f"File not found at {RECIPES_FILE}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in recipes.json"}

@recipes_bp.route('/get-all', methods=['GET'])
def get_all_recipes():
    recipes = load_recipes()
    if "error" in recipes:
        return jsonify(recipes), 500
    return jsonify({"recipes": list(recipes.keys())})

@recipes_bp.route('/get/<string:recipe_name>', methods=['GET'])
def get_recipe(recipe_name):
    recipes = load_recipes()
    recipe_name = recipe_name.replace("-", " ")  # Handle URL spacing
    if "error" in recipes:
        return jsonify(recipes), 500
    if recipe_name in recipes:
        return jsonify({recipe_name: recipes[recipe_name]})
    return jsonify({"error": "Recipe not found"}), 404
