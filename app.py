from flask import Flask, jsonify,render_template,requests
import requests
import os

app = Flask(__name__)
api_key = os.getenv('OWM_API_KEY')  # Use the environment variable

@app.route('/')
def weather():
    api_key = os.getenv('OWM_API_KEY')  # Ensure your API key is set
    city = "London"
    if not api_key:
         error = "API key is missing"
         return jsonify({"error": error}) if request.headers.get('Accept') == 'application/json' else render_template('index.html', city=city, error=error)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'main' not in data or 'temp' not in data['main']:
            error = "Weather data unavailable"
            return jsonify({"error": error}) if request.headers.get('Accept') == 'application/json' else render_template('index.html', city=city, error=error)

        temperature = data['main']['temp']
        return jsonify({"city": city, "temperature": temperature}) if request.headers.get('Accept') == 'application/json' else render_template('index.html', city=city, temperature=temperature)

    except requests.exceptions.RequestException as e:
         error = str(e)
        return jsonify({"error": error}), 500 if request.headers.get('Accept') == 'application/json' else render_template('index.html', city=city, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
