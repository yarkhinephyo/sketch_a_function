from flask import Flask, redirect, url_for, request, render_template, jsonify
import img_parser

from models.PolynomialModel import PolynomialModel

app = Flask(__name__)

polyModel = PolynomialModel()

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

    ## Models here ##

    func1 = polyModel.get_best_fit(complexity_level, x0, y0)

    ## ##

    base64 = img_parser.x_y_to_base64((x0, y0), func1.output)
    
    return jsonify({"imgOutput": base64})

if __name__ == "__main__":
    app.run(debug=True, port=5000)