# fullstack-interview-test
Interview test for fullstack Software Engineers

## Welcome!
This project uses [Django](https://www.djangoproject.com/) for the backend, and [React](https://en.reactjs.org/) for its frontend.

Because both stacks are natively incompatible, and for further configuration of the repositories, this project is separated into two different repositories, this one for the backend and [this one](https://github.com/lalish99/flat-mx-frontend-interview-test/) for the frontend.

You need both projects running in order to see the completed project. Each repository contains instructions on how to run them and which stack is required.

## TODO: 
The project missed some of the requirements, the only part that's missing is the triggering of Pull Requests and attempting to merge two branches, as well as validating that the base and rebase branches of a pull request actually exist on the reopository and are available for merging.

----
## Releases:
For conviniece there is a release changelog, which can be accesed directly [on GitHub](https://github.com/lalish99/flat-mx-backend-interview-test/releases), or via the `CHANGELOG.md` [file](https://github.com/lalish99/flat-mx-backend-interview-test/blob/master/CHANGELOG.md). Both of this contain auto-generated releases, which are composed by all the commits between releases. Check [Semantic Release](https://github.com/semantic-release/semantic-release) for more information.

**Note:**This repository uses a GitHub action for the purpose of generating the semantic release, and given that this module is not directly implemented in python, the following marketplace job [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) was implemented.

----
## Requirements
First of all, you need to have python installed on your local machine, if you dont have it installed yet, go to: [https://www.python.org/downloads/](https://www.python.org/downloads/) and follow the instructions for your operating system.

**Important:** Make sure you have `python3` installed.

----
## Setup Instructions
Before anything we need to clone this repository to our local machine, if it's your first time I highly recommend checking GitHub's guide on [how to clone a repository](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository).

Move to the directory of the cloned repository and follow the next instructions for a virtual environment.

Now with python installed we can continue to setup our environment and local workspace for running this project. I highly suggest using some sort of virtual environment, but you can still install everythin directly into your root python installation, but that might generate versioning errors.

In this case I suggest using [virtualenv](https://virtualenv.pypa.io/en/latest/) which is easy to use and install, for instructions on how to install it you can check one of the following articles: [Official virtualenv docs](https://virtualenv.pypa.io/en/latest/installation.html), [Instalar Virtualenv usando pip3](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3), [How to install virtualenv on ubuntu](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b). 

**Important:** To prevent git from detecting the files of the virtual environment as code for the repository name your virtual environment as `.venv`.

----
Every virtual environment has its own configuration, but in case you used virtualenv, the following code should create you an environment with the appropiate name and python version: 
```bash
$ virtualenv .venv -p python3
```

With your virtual environment created, you can now initialize it with the following command (for MacOS):
```bash
$ . ./.venv/bin/activate
```

----
This should start your environment and you should now see the name of the environment on your terminal:
```bash
(.venv) $
```

Now it's time to intsall the dependencies for this project, to do so you simply need to run the following command:
```bash
(.venv) $ pip install -r requirements.txt
```
**Important:** Make sure you are inside the directory of the cloned repository, otherwise you might get an error saying that the file `requirements.txt` does not exist.

----
After you've completed the previous steps you should be able to run the django migrate command:
```bash
(.venv) $ ./manage.py migrate
```
This command will generate a `.sqlite` file, in order to simulate a database for all our models.

With the migration done, you can now initialize the server with Django's [runserver](https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver) command.
```bash
(.venv) $ ./manage.py runserver
```
**Important:** Make sure you are inside the directory of the cloned repository, otherwise you might get an error saying that the file `manage.py` does not exist.

If everything went well you should now see the following log in your terminal:
```bash
Django version 3.2.9, using settings 'flat_mx_backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
**Important:** The message must say `Starting development server at http://127.0.0.1:8000/` otherwise the server might be running on another port which will cause problems for the frontend connection. If you receive a message mentioning that another service is running on the same port, please terminate that service. This can be achieved bu closing the program that's running on that port (normally another web app or backend server).

----
## Documentation:
Once you've got your project started you might go to `http://127.0.0.1:8000/docs/swagger/` or `http://127.0.0.1:8000/docs/redoc/` to visualize an interactive representation of the api.
This schema visualization is auto-generated, thus on every update to the api this views will be automatically updated.
