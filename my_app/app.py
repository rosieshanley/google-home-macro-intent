from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
  requests.get('http://localhost:5000')
  return "My app is up because my dependency is up!"

if __name__ == "__main__":
  app.run()
