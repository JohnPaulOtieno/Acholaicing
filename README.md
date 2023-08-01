# Achola's Icing

Cake Website

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- [Python3](https://www.python.org/downloads/)
- [Python Virtual Environment, virtualenv](https://docs.python.org/3/tutorial/venv.html)
- [Django](https://docs.djangoproject.com/en/4.1/intro/install/)
- Any other dependencies listed in requirements.txt

### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone the repository using

`git clone https://github.com/JohnPaulOtieno/Acholaicing.git`

OR

 `git clone git@github.com:JohnPaulOtieno/Acholaicing.git` if using SSH

2. You need to activate a virtual environment for the project, and every other time you want to make changes

 Here, [venv](https://docs.python.org/3/tutorial/venv.html) is included with python.

 Start with `python3 -m venv [replace with what you would like to call the virtual environment]`. You can do `python3 -m venv dev`

 Activate virtual environment using what you call your virtual environment. Ours was `dev`

`source dev/bin/activate`

 Then install requirements using `pip install -r requirements.txt`

3. Run migrations

`python manage.py makemigrations`

`python manage.py migrate`

4. Run the server:

`python manage.py runserver`

The server will be running on <http://127.0.0.1:8000/>

## Running the tests

We will update this part once we start writing tests for the code

`python manage.py test`

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Python](https://www.python.org/) - Programming Language

## Authors (Add Your Own)

- **[Wechuli Simiyu](https://github.com/wechu07)** - *Initial setup*

## License

This project is licensed under the [MIT](link) - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
