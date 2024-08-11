from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/validatessl', methods=['GET'])
def validate_ssl():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    api_url = f"https://api.ssllabs.com/api/v3/analyze?host={url}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)