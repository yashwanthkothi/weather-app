from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def weather():
    api_key = "YOUR_OPENWEATHER_API_KEY"  # Replace with a real API key
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        
        if 'main' not in data or 'temp' not in data['main']:
            return jsonify({"error": "Weather data unavailable"}), 502
            
        return f"Weather in {city}: {data['main']['temp']}°C"
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
