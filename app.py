from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

def call_rest_endpoint(input_data):
    # REST endpoint URL
    url = 'http://b5610ccc-8191-4fe0-be4f-019def421b5f.westeurope.azurecontainer.io/score'

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        payload = {
            'Inputs': {
                'data': input_data
            },
            'GlobalParameters': 0.0
        }

        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()

        result = response.json()

        return result
    except requests.exceptions.RequestException as e:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Create a dictionary with default values of 0.0 for the input features
            input_data = {
                'Time': 'example_value',
                'Dry Weight': 0.0,
                'Moisture 1': 0.0,
                'Moisture 2': 0.0,
                'Coat Weight 1': 0.0,
                'Basis Weight': 0.0,
                'Coat Weight 2': 0.0,
                'Filler Flume Consistency': 0.0,
                'Dryer Control 1': 0.0,
                'Filler Amount': 0.0,
                'Nipload': 0.0,
                'Press Control': 0.0,
                'Speed': 0.0,
                'Dryer Control 2': 0.0,
                'Water Flow': 0.0
            }

            # Update the dictionary with user-provided values from the form
            for key in input_data.keys():
                if key in request.form:
                    input_data[key] = float(request.form[key])

            result = call_rest_endpoint([input_data])

            if result:
                # Process the result as needed
                return jsonify(result)
            else:
                return jsonify({"error": "Failed to call the REST endpoint."})
        except ValueError:
            return jsonify({"error": "Invalid input. Please enter valid numeric values."})
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)