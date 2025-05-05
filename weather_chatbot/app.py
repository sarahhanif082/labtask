from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Optionally use OpenWeatherMap API
API_KEY = "your_openweathermap_api_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    
    # Uncomment below to use live API
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # response = requests.get(url).json()
    
    # Dummy response for demo
    response = {
        "name": city,
        "main": {"temp": 25},
        "weather": [{"description": "clear sky"}]
    }

    if "main" in response:
        weather_info = {
            "city": response["name"],
            "temperature": response["main"]["temp"],
            "description": response["weather"][0]["description"]
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "City not found!"})

if __name__ == '__main__':
    app.run(debug=True)
