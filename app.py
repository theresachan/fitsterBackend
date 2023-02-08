# from flask import Flask, request, jsonify
# import joblib

# app = Flask(__name__)

# # Load the pcos prediction model
# pcos_model = joblib.load('pcos_model.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Retrieve the input variables from the request body
#     input_data = request.get_json()
#     name = input_data['name']
#     age = input_data['age']
#     over_weight = input_data['over_weight']
#     weight_gain = input_data['weight_gain']
#     periods = input_data['periods']
#     conceiving = input_data['conceiving']
#     chin_hair = input_data['chin_hair']
#     cheeks_hair = input_data['cheeks_hair']
#     upper_lips_hair = input_data['upper_lips_hair']
#     between_breasts_hair = input_data['between_breasts_hair']
#     arms_hair = input_data['arms_hair']
#     inner_thigh_hair = input_data['inner_thigh_hair']
#     acne_or_skin_tag = input_data['acne_or_skin_tag']
#     hair_thinning = input_data['hair_thinning']
#     dark_patches = input_data['dark_patches']
#     tiredness = input_data['tiredness']
#     mood_swings = input_data['mood_swings']
#     exercise = input_data['exercise']
#     eat_outside = input_data['eat_outside']
#     canned_food = input_data['canned_food']
#     city = input_data['city']
#     diagnose = input_data['diagnose']
    
#     # Prepare the input data as a list
#     input_vars = [age, over_weight, weight_gain, periods, conceiving, chin_hair, cheeks_hair, upper_lips_hair, between_breasts_hair, arms_hair, inner_thigh_hair, acne_or_skin_tag, hair_thinning, dark_patches, tiredness, mood_swings, exercise, eat_outside, canned_food, city, diagnose]
    
#     # Make a prediction using the loaded model
#     prediction = pcos_model.predict([input_vars])[0]
    
#     # Return the prediction result as a JSON response
#     return jsonify({'name': name, 'prediction': prediction})

# if __name__ == '__main__':
#     app.run()

# from flask import Flask, request, jsonify
# import joblib

# app = Flask(__name__)

# # Load the PCOS prediction model
# pcos_model = joblib.load('pcos_model.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Retrieve the input variables from the request body
#     input_data = request.get_json()
#     name = input_data['name']
#     weight_gain = input_data['Weightgain']
#     hair = input_data['Hair']
#     patches = input_data['Patches']
#     pimples = input_data['Pimples']
#     depression = input_data['Depression']
#     family_diabetes = input_data['FamilyDiabetes']
#     maintaining_body_weight = input_data['MaintainingBodyWeight']
#     oily_skin = input_data['OilySkin']
#     hair_thinning = input_data['Hairthinning']
#     hostel = input_data['Hostel']
#     personal_problems = input_data['PersonalProblems']
#     peer_pressure = input_data['PeerPressure']
#     dietary_habits = input_data['DietryHabits']
#     eat_fast_foods = input_data['EatFastFoods']
#     periods = input_data['Periods']
#     wake_up = input_data['WakeUp']
#     sleep_after = input_data['SleepAfter']
    
#     # Prepare the input data as a list
#     input_vars = [weight_gain, hair, patches, pimples, depression, family_diabetes, maintaining_body_weight, oily_skin, hair_thinning, hostel, personal_problems, peer_pressure, dietary_habits, eat_fast_foods, periods, wake_up, sleep_after]
    
#     # Make a prediction using the loaded model
#     prediction = pcos_model.predict([input_vars])[0]
    
#     # Return the prediction result as a JSON response
#     return jsonify({'name': name, 'prediction': prediction})

# if __name__ == '__main__':
#     app.run()











# from flask import Flask, request, jsonify
# from flask_ngrok import run_with_ngrok
# import joblib

# app = Flask(__name__)
# run_with_ngrok(app)

# # Load the PCOS prediction model
# pcos_model = joblib.load('pcos_model.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Retrieve the input variables from the request body
#     input_data = request.get_json()
#     name = input_data['name']
#     weight_gain = input_data['weight_gain']
#     hair = input_data['hair']
#     patches = input_data['patches']
#     pimples = input_data['pimples']
#     depression = input_data['depression']
#     family_diabetes = input_data['family_diabetes']
#     maintaining_body_weight = input_data['maintaining_body_weight']
#     oily_skin = input_data['oily_skin']
#     hair_thinning = input_data['hair_thinning']
#     hostel = input_data['hostel']
#     personal_problems = input_data['personal_problems']
#     peer_pressure = input_data['peer_pressure']
#     dietary_habits = input_data['dietary_habits']
#     eat_fast_foods = input_data['eat_fast_foods']
#     periods = input_data['periods']
#     wake_up = input_data['wake_up']
#     sleep_after = input_data['sleep_after']
    
#     # Prepare the input data as a list
#     input_vars = [weight_gain, hair, patches, pimples, depression, family_diabetes, maintaining_body_weight, oily_skin, hair_thinning, hostel, personal_problems, peer_pressure, dietary_habits, eat_fast_foods, periods, wake_up, sleep_after]
#     print(input_vars)
    
#     # Make a prediction using the loaded model
#     prediction = pcos_model.predict([input_vars])[0]
    
#     # Return the prediction result as a JSON response
#     prediction = str(prediction) # Convert numpy.bool_ to int
#     return jsonify({'name': name, 'prediction': prediction})


# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import joblib

app = Flask(__name__)
run_with_ngrok(app)

# Load the PCOS prediction model
pcos_model = joblib.load('clf1.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input variables from the request body
    input_data = request.get_json()
    name = input_data['name']
    age = input_data['age']
    over_weight = input_data['over_weight']
    weight_gain = input_data['weight_gain']
    periods = input_data['periods']
    conceiving = input_data['conceiving']
    chin_hair = input_data['chin_hair']
    cheeks_hair = input_data['cheeks_hair']
    upper_lips_hair = input_data['upper_lips_hair']
    between_breasts_hair = input_data['between_breasts_hair']
    arms_hair = input_data['arms_hair']
    inner_thigh_hair = input_data['inner_thigh_hair']
    acne_or_skin_tag = input_data['acne_or_skin_tag']
    hair_thinning = input_data['hair_thinning']
    dark_patches = input_data['dark_patches']
    tiredness = input_data['tiredness']
    mood_swings = input_data['mood_swings']
    exercise = input_data['exercise']
    eat_outside = input_data['eat_outside']
    canned_food = input_data['canned_food']
    city = input_data['city']
    diagnose=input_data['diagnose']
    
    # Prepare the input data as a list
    input_vars = [age, over_weight, weight_gain, periods, conceiving, chin_hair, cheeks_hair, upper_lips_hair, between_breasts_hair, arms_hair, inner_thigh_hair, acne_or_skin_tag, hair_thinning, dark_patches, tiredness, mood_swings, exercise, eat_outside, canned_food, 
    city, diagnose]
    
    # Make a prediction using the loaded model
    prediction = pcos_model.predict([input_vars])[0]
    
    # Return the prediction result as a JSON response
    prediction = str(prediction) # Convert numpy.bool_ to int
    return jsonify({'name': name, 'prediction': prediction})


if __name__ == '__main__':
    app.run()
