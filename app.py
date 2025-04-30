from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def weather():
    api_key = "YOUR_OPENWEATHER_API_KEY"  # Replace with a real API key
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return f"Weather in {city}: {response['main']['temp']}°C"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)