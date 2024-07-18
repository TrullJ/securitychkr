import requests
from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

emailValMicroService = 'http://127.0.0.1:65001/validateEmail/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_box = request.form.get('inputBox')
    
    if input_box:
        # Here you can add your logic to handle the URL or Email
        if '@' in input_box:
            return redirect(url_for('validate_email', email=input_box))
        else:
            return redirect(url_for('validate_url', url=input_box))

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
    # Placeholder function for URL validation. Implement your URL validation logic here.
    return jsonify({"url": url, "validation": "URL validation logic not implemented"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65000)