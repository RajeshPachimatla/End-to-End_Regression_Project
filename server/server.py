from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_rent', methods=['GET', 'POST'])
def predict_house_rent():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    furnish = int(request.form['furnish'])

    response = jsonify({
        'estimated_rent': util.get_estimated_rent(location,total_sqft,bhk,furnish)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For House Rent Prediction...")
    util.load_saved_artifacts()
    app.run()