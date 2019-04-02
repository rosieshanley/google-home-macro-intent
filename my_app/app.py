from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello!"

@app.route("/health")
def health_check():
  requests.get('http://localhost:3000/')

  try:
    requests.get('http://localhost:5000')
  except Exception:
    return "My app is up but my dependency is down!"

  return "My app is up and so is my dependency!"

if __name__ == "__main__":
  app.run()
