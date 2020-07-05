from flask import Flask, redirect, url_for, request, render_template, jsonify
import img_parser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_best_fit', methods=['POST'])
def get_best_fit():
    payload = request.get_json()
    if not payload['imgInput']:
        return jsonify({"error": "empty"})

    base64_string = payload['imgInput'].split(",")[1]
    y_values = img_parser.base64_to_y_values(base64_string)

    ## Models here ##

    ## ##

    base64 = img_parser.y_values_to_base64(y_values)
    
    return jsonify({"imgOutput": base64})

if __name__ == "__main__":
    app.run(debug=True, port=5000)