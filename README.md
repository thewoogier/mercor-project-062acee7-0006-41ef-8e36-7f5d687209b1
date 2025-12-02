# flask-api-template

![Python CI](https://github.com/DiljotSG/flask-api-template/workflows/Python%20application/badge.svg?branch=master)

This repository provides the basic tools for creating a Python REST API powered by [Flask](https://flask.palletsprojects.com/en/1.1.x/).

## What does it set-up for you?

This repo helps you quickly bootstrap a REST API using Flask. It also sets up the following things for you.

- File and code structure with one sample endpoint.
- `requirements.txt` already set up with everything you need to create a working virtual environment.
- A tests package for testing your API endpoints.
- A root python file (`index.py`) which makes launching your app simple on both your local machine and on some sort of serverless compute environment.
- GitHub Actions workflow to test and lint your application with `flake8`.
- A license.

## What does it NOT set-up for you?

We don't do everything for you, because your project requirements might be different than ours. We don't:

- Set-up any sort of serverless deployment via GitHub actions, I personally love AWS Lambda, but you may prefer some other cloud provider.
- Set-up tox to quickly test and lint your application on your local machine. Although [tox](https://tox.readthedocs.io/en/latest/) is awesome and you should do this.
- Set-up any sort of static analysis tool. Python3 has types and you should use them, should you decide to type your code, using a tool like [mypy](http://mypy-lang.org/) for static analysis and type-checking is awesome and you should consider doing this.
- Differentiate between application dependencies and development dependencies, it can be beneficial to do this, especially if you are deploying your app to a cloud provider, you can reduce your application's size this way.

# Setup

This codebase uses Python3.7.X/Python3.8.X. These setup instructions are for macOS using [Homebrew](https://brew.sh).

Installing these dependencies should be similar for other platforms with the appropriate package managers for that platform.

## Python3 Installation

1. Install python.

    ```shell
    brew install python
    sudo pip3 install virtualenv
    ```

## Environment Setup

These steps are required for development.

1. Create a Python virtual environment.

    ```shell
    virtualenv -p python3 venv
    ```

2. Activate the environment.

    ```shell
    . venv/bin/activate
    ```

3. Install Python dependencies.

    ```shell
    pip3 install -r requirements.txt
    ```

4. Run the flask application locally.

    ```shell
    python3 index.py
    ```

    Development Mode (Auto reloads on code changes):

    ```shell
    export FLASK_ENV=development

    python3 index.py
    ```

# Testing

You can quickly and easily run all the unit tests locally on your machine with the following command.

```shell
python -m unittest discover tests
```

## Error Handling
All errors must return a JSON object with the key `error` containing the message. Use the constants in `src/response_codes.py`.