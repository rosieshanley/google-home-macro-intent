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

3. Install [newman](https://learning.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman/):

```
$ npm install newman
```

### Running Instructions

This project is broken up into two directories: `my_app`, and `my_app_dependency`

1. `cd` into the my `my_app` directory and run:

```
$ flask run --host=0.0.0.0 --port=3000
```

2. Navigate to `http://localhost:3000/health` in your browser

3. `cd` into the `my_app_dependency` directory and run:

```
$ flask run --host=0.0.0.0 --port=5000
```

4. Refresh `http://localhost:3000/health`

5. To run the [Postman](https://learning.getpostman.com/docs/postman/launching_postman/installation_and_updates/) tests, run:

```
$ newman run own_your_innocence.postman_collection.json
```

6. To run the Postman tests via [cron](https://cron-job.org/en/) job, run:

```
$ crontab -e
```

and write the following code to the file:

```
PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin

* * * * * ~/code/innocence/bin/run_postman_tests
```

This job will run every minute and will print logs to the `logs` directory
