from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)
api_key = os.getenv('OWM_API_KEY')  # Use the environment variable

@app.route('/')
def weather():
    api_key = os.getenv('OWM_API_KEY')  # Fetch API key from environment variable
    if not api_key:
        return jsonify({"error": "API key is missing"}), 400  # Return a 400 error if API key is missing

    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        
        if 'main' not in data or 'temp' not in data['main']:
            return jsonify({"error": "Weather data unavailable"}), 502  # Return 502 if weather data is unavailable
            
        return f"Weather in {city}: {data['main']['temp']}°C"
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

