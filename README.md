### Setup Instructions

##### Requirements:

* *Python3* and *pip*
* *npm*

1. Install [flask](http://flask.pocoo.org):

```
$ pip install flask
```

2. Install [requests](http://docs.python-requests.org/en/master/):

```
$ pip install requests
```

### Running Instructions

1. `cd` into the my `my_app` directory and run:

```
$ flask run --host=0.0.0.0 --port=3000
```

2. run `ngrok` to port your application to a public facing URL:

```
$ ngrok http 3000
```

3. In Dialogflow, update the Fulfillment Webhook URL to your `https://[your-ngrok-url]` for your intent.
