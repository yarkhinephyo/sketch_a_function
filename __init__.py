from flask import Flask, redirect, url_for, request, render_template, jsonify
import img_parser

from models import *

app = Flask(__name__)

models = [
    PolynomialModel(),
    LogarithmicModel(),
    ExponentialModel(),
    SineModel()
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_best_fit', methods=['POST'])
def get_best_fit():
    payload = request.get_json()

    if not payload['imgInput']:
        return jsonify({"error": "empty"})

    base64_string = payload['imgInput'].split(",")[1]
    complexity_level = int(payload['complexity'])
    x0, y0 = img_parser.base64_to_x_y(base64_string)

    sorted_functions = sorted_functions_by_mse(models, complexity_level, x0, y0)
    best_function = sorted_functions[0]

    base64 = img_parser.x_y_to_base64((x0, y0), best_function.output)
    
    return jsonify({
        "imgOutput": base64, 
        "equation_string": best_function.equation_string,
        "model_name": best_function.model_name,
        "mse": best_function.mse,
        "error": "none"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)