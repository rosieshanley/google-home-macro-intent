from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "My dependency is up!"

if __name__ == "__main__":
    app.run()
