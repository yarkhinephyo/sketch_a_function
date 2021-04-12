from flask import Flask, redirect, url_for, request, render_template, jsonify
import img_parser

# Import all the custom models
from models import *

app = Flask(__name__)

models = [
    PolynomialModel(),
    PolyLogarithmicModel(),
    ExponentialModel(),
    SineModel(),
    SinhModel(),
    CoshModel(),
    TanhModel(),
    ArctangentModel(),
    SigmoidModel()
]

# For display as checkboxes
model_names = get_all_names(models)

@app.route('/')
def index():
    return render_template("index.html", model_names=model_names)

@app.route('/get_best_fit', methods=['POST'])
def get_best_fit():
    payload = request.get_json()

    # Invalid if no drawing or no model selected
    if not payload['imgInput'] or not payload['selected_models']:
        return jsonify({"error": "Invalid inputs"})

    base64_string = payload['imgInput'].split(",")[1]
    complexity_level = int(payload['complexity'])
    selected_models = payload['selected_models'].split(",")

    # base64 PNG to X and Y arrays
    x0, y0 = img_parser.base64_to_x_y(base64_string)

    sorted_functions = sorted_functions_by_mse(models, selected_models, complexity_level, x0, y0)

    # If the list of valid functions is empty
    if not sorted_functions:
        return jsonify({"error": "Unable to fit"})

    best_function = sorted_functions[0]
    base64 = img_parser.x_y_to_base64((x0, y0), best_function.output)
    
    return jsonify({
        "imgOutput": base64, 
        "equation_string": best_function.equation_string,
        "model_name": best_function.model_name,
        "mse": best_function.mse,
        "error": "None"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)