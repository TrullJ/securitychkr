import requests
from flask import Flask

app = Flask(__name__)

base_url = "http://emailrep.io/"

@app.route('/validateEmail/<email>', methods=['GET'])
def validateEmail(email):
    serviceURL = base_url + email
    print(serviceURL)
    response = requests.get(serviceURL)
    return response.json()

@app.route('/', methods=['GET'])
def home():
    return "<p>Welcome to home page</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")