from flask import Flask, redirect, url_for, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_best_fit', methods=['POST'])
def get_best_fit():
    print(request.get_json())
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)