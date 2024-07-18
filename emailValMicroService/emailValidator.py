import requests
from flask import Flask, jsonify

app = Flask(__name__)

base_url = "http://emailrep.io/"

@app.route('/validateEmail/<email>', methods=['GET'])
def validateEmail(email):
    serviceURL = base_url + email
    response = requests.get(serviceURL)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=65001)