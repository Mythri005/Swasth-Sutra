import pickle
import numpy as np
import random
from collections import OrderedDict


# ✅ Load the trained ML model
def load_model():
    with open("ml_model/model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# ✅ Meal plans for different health conditions
diet_plans = {
    "Diabetes": [
        {"breakfast": "Ragi dosa", "lunch": "Bajra khichdi", "dinner": "Foxtail millet soup"},
        {"breakfast": "Jowar roti", "lunch": "Quinoa salad", "dinner": "Brown rice & dal"},
        {"breakfast": "Millet porridge", "lunch": "Sprouts salad", "dinner": "Grilled tofu"}
    ],
    "Heart Disease": [
        {"breakfast": "Oats upma", "lunch": "Vegetable millet pulao", "dinner": "Dal khichdi"},
        {"breakfast": "Cornflakes with millet milk", "lunch": "Sprout salad", "dinner": "Grilled vegetables"},
        {"breakfast": "Ragi idli", "lunch": "Foxtail millet curry", "dinner": "Millet dosa"}
    ],
    "High BP": [
        {"breakfast": "Fruit salad", "lunch": "Millet chapati with curry", "dinner": "Vegetable stew"},
        {"breakfast": "Egg omelet", "lunch": "Rice and dal", "dinner": "Sautéed greens"},
        {"breakfast": "Smoothie bowl", "lunch": "Chickpea salad", "dinner": "Grilled tofu"}
    ],
    "Low BP": [
        {"breakfast": "Banana smoothie", "lunch": "Coconut rice", "dinner": "Pumpkin soup"},
        {"breakfast": "Peanut butter toast", "lunch": "Rajma rice", "dinner": "Vegetable soup"},
        {"breakfast": "Chia seed pudding", "lunch": "Spinach dal", "dinner": "Sweet potato stir-fry"}
    ],
    "Menstrual Health": [
        {"breakfast": "Ragi malt", "lunch": "Paneer paratha", "dinner": "Palak dal"},
        {"breakfast": "Sprouted moong salad", "lunch": "Pumpkin soup", "dinner": "Mixed millet roti"},
        {"breakfast": "Sesame seed smoothie", "lunch": "Chickpea curry", "dinner": "Dal tadka"}
    ]
}

def generate_meal_plan(predicted_category, days=30):
    print(f"📢 Generating {days}-day meal plan for: {predicted_category}")

    if predicted_category not in diet_plans:
        print("⚠️ WARNING: Predicted category not found, defaulting to Diabetes")
        predicted_category = "Diabetes"

    selected_meals = diet_plans.get(predicted_category, [])

    if not selected_meals:
        print("❌ ERROR: No meals found for predicted category!")
        return {}

    # ✅ Use OrderedDict to maintain order
    meal_plan = OrderedDict((f"Day {day}", random.choice(selected_meals)) for day in range(1, days + 1))

    print(f"✅ Generated meal plan for {days} days: {meal_plan}")
    return meal_plan

# ✅ Function to predict & recommend diet
def recommend_diet(user_data, days=30):  # Default to 30 days
    model = load_model()

    all_features = ["age", "gender", "weight", "low_bp", "high_bp", "sugar", "diabetes", "heart_disease", "menstrual_health"]

    gender_map = {"male": 0, "female": 1}
    user_data["gender"] = gender_map.get(user_data.get("gender", "male"), 0)

    input_data = np.array([[user_data.get(field, 0) for field in all_features]], dtype=float)

    predicted_category = model.predict(input_data)[0]
    print(f"🔍 DEBUG: Model Predicted -> {predicted_category}")

    # ✅ Pass `days` correctly to `generate_meal_plan`
    return generate_meal_plan(predicted_category, days=days)
