# Backend_ammper
Backend Python for Ammper Knowledge Test

# Steps to configure this project
## Previous steps
1. Install python and pip

## Steps
1. Create virtual environment in the root of the project
<code>python -m venv ./venv</code>
2. Add important paths to $PYTHONPATH (advise: add it in ./venv/bin/activate)
<code>export PYTHONPATH="$HOME_PATH/packages/python:$HOME_PATH/db/python:$HOME_PATH/shared/python:$HOME_PATH"</code>
3. Install dependencies
<code>pip install -t packages/python -r requirements.txt</code>
4. Set environment variables en a .env file

This project is built with Python using the FastAPI framework and deployed on AWS EC2 instances.

It is connected to a PostgreSQL database.

## View the demo here:
[Ver el video en YouTube](https://youtu.be/mVudxepPZfk)


To connect to test go to http://3.81.228.234:5173/login
# Important commands
## Run migrations
<code>alembic revision -m "message" --head=nitro@head</code>