# VALR Simple Python Client

A Simple Python Library to integrate with [VALR API](https://docs.valr.com).

## Cloning source

Get this package by:

```shell
$ git clone https://github.com/VALR-Tech/Valr-simple-client.git
```

Activate the virtual environment with venv before coding, testing & packaging:

```shell
$ cd .
$ python3 -m venv .dev_env
$ source .dev_env/bin/activate
$ python3 -m pip install -r requirements.txt
```

Required `ENVIRONMENT` variables:

```dotenv
VALR_KEY='valr_key'
VALR_SECRET='valr_secret'
```

Example Usage, See `example.py` file:

```shell
$ python3 example.py
```

## Installing Package

To use this as a package in your project simply run:

```shell
git clone https://github.com/VALR-Tech/Valr-simple-client.git
cd Valr-simple-client
python3 setup.py install
```

Then import:

```python
from valr import Valr

# Initiate a client
valr_client = Valr(key='YOUR_VALR_KEY', secret='YOUR_VALR_SECRET')

# Access the endpoint your want to use.
valr_client.public.server_time()
```

