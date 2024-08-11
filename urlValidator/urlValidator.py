from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VIRUSTOTAL_API_KEY = '<ENTER YOUR API KEY>'
VIRUSTOTAL_URL = 'https://www.virustotal.com/vtapi/v2/url/report'

@app.route('/validateURL', methods=['GET'])
def validateURL():
    url = request.args.get('url')

    if not url:
    	return jsonify({"error": "URL is required"}), 400

    params = {
    	'apikey': VIRUSTOTAL_API_KEY,
    	'resource': url
    }

    response = requests.get(VIRUSTOTAL_URL, params=params)

    if response.status_code != 200:
    	return jsonify({"error": "Error connecting to VirusTotal API"}), 500

    result = response.json()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=65000)