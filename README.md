### Setup Instructions

1. First, you need to make sure you have python installed:

```
$ brew install python3
```

2. Then, you need to install pip:

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
```

3. Finally, install requests:

```
$ pip install requests
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

