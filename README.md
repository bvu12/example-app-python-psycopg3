# example-app-python-psycopg3

This repo has a simple CRUD Python application that uses the [`psycopg3`](https://www.psycopg.org/psycopg3/docs/) driver to talk to a CockroachDB cluster.

For details on creating a CockroachDB cluster and running the code, see [this tutorial](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-psycopg3.html).

## Before you begin

To run this example you must have:

- Python 3
- `pip` version 20.3 or greater

## Install the dependencies

In a terminal run the following command:

~~~ shell
pip install -r requirements.txt
~~~

## Environment variables
You'll need to have a value for `COCKROACH_CONNECTION_STRING` - this shouldn't be publically shared I'll give it to you via Discord.


## Run the example

To run the example, in a terminal run the following command:

~~~ shell
python3 main.py
~~~

Then nvaigate to [the interactive api docs](http://127.0.0.1:8000/docs#/default/get_accounts_accounts_get), try running the `GET /accounts` endpoint to see if it worked.
