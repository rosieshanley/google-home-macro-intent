from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/health")
def health_check():
    # curl my_app
    requests.get('http://localhost:3000/')

    # curl my_app_dependency and rescue from error
    try:
        requests.get('http://localhost:5000')
    except Exception:
        # will execute if my_app_dependency is down
        return "My app is up but my dependency is down!"
    # will execute if my_app_dependency is up
    return "My app is up and so is my dependency!"

if __name__ == "__main__":
    app.run()
