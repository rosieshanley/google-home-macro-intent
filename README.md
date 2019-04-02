### Running Instructions

#### Set Up

First, you need to make sure you have python installed:

`$ brew install python`

Then, you need to install pip:

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
```

Finally, install requests:

`$ pip install requests`

#### My App and its Depenency

This project is broken up into two directories: `my_app`, and `my_app_dependency`.

To run `my_app`, `cd` into the my `my_app` directory and run:

`$ flask run --host=0.0.0.0 --port=3000`

You will see an internal server error in the browser. This is because `my_app` is dependent on `my_app_dependency`. To fix this, `cd` into the `my_app_dependency` directory and run:

`$ flask run --host=0.0.0.0 --port=5000`

