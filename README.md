# FlaskBoilerplate

## Description

This is a bare minimum boilerplate for a Flask application. The Bootstrap
frontend is also included and pre-configured by default.

The purpose of this boilerplate is to have Flask applications up and running
very quickly.

## Dependencies

No Flask extensions have been added to this boilerplate.

Therefore, the only dependencies are Python and Flask itselves.

On Ubuntu, those dependencies can be installed with the following commands:
I will make use of `virtualenv`.

```bash
$ sudo apt update && sudo apt upgrade
$ sudo apt install python3 python3-flask
```

However, it could be interesting to create a virtual environment.
In that case, an additional dependency is required:

```bash
$ sudo apt install python3-virtualenv
```

## Execution

If no _virtualenv_ is used, the application can be directly executed as follows:

```bash
$ python app.py
```

Otherwise, you will need to execute the following commands.

Initialize and activate a virtualenv:

```bash
$ virtualenv env
$ source env/bin/activate
```

Install required dependencies:

```bash
(env) $ pip install -r requirements.txt
```

Run the development server:

```bash
(env) $ python app.py
```

Finally, navigate to [http://localhost:5000](http://localhost:5000).

## References

Boostrap was obtained from [getbootstrap.com](https://getbootstrap.com).
