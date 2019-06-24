from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/health")
def health_check():
    return "My website is up!"

@app.route("/action", methods=['GET', 'POST'])
def action():
    req = request.get_json()
    if req is None:
        return 'Nah'
 
    print(req) 
    print(req.get('queryResult').get('queryText'))
    return 'HEY'

 

if __name__ == "__main__":
    app.run()
