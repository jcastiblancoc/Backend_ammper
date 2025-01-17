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
5. Run tests
<code>pytest --path ./test --junitxml=test-report.xml --cov=src --cov-report=xml</code>


# Important commands
## Run migrations
<code>alembic revision -m "message" --head=nitro@head</code>