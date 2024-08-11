import requests
from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

# Define microservice URLs and API keys
emailValMicroService = 'http://127.0.0.1:65001/validateEmail/'
sslValMicroService = 'http://127.0.0.1:5555/validatessl'
VIRUSTOTAL_API_KEY = '<ENTER YOUR API KEY>'
VIRUSTOTAL_URL = 'https://www.virustotal.com/vtapi/v2/url/report'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_box = request.form.get('inputBox')
    action = request.form.get('action')

    if input_box:
        if action == 'validateEmail' and '@' in input_box:
            return redirect(url_for('validate_email', email=input_box))
        elif action == 'validateURL':
            return redirect(url_for('validate_url', url=input_box))
        elif action == 'validateSSL':
            return redirect(url_for('validate_ssl', url=input_box))
        else:
            return jsonify({"error": "Invalid input or action"}), 400

@app.route('/validateEmail/<email>')
def validate_email(email):
    try:
        response = requests.get(emailValMicroService + email)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
    validation_result = response.json()
    return render_template('validation_result.html', result=validation_result)

@app.route('/validateURL/<path:url>')
def validate_url(url):
    try:
        params = {
            'apikey': VIRUSTOTAL_API_KEY,
            'resource': url
        }
        response = requests.get(VIRUSTOTAL_URL, params=params)
        response.raise_for_status()
        result = response.json()
        return render_template('validation_result.html', result=result)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/validateSSL/<path:url>')
def validate_ssl(url):
    try:
        response = requests.get(f"{sslValMicroService}?url={url}")
        response.raise_for_status()
        data = response.json()
        return render_template('validation_result.html', result=data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65000)