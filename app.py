from flask import Flask, send_from_directory, jsonify
from data_aggregator import fetch_and_classify_data

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/get-disasters')
def get_disasters():
    data = fetch_and_classify_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
