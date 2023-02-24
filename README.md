# Treez assignment

### Setup backend
* Install python
* Navigate into `treez_assignment` folder
* Create a virtual environment to install the requirements
```
Windows
-------
> python -m pip install virtualenv
> virtualenv venv
> pip install requirements.txt
```
* Once the requirements are installed, we need to seed the database with initial data. This will create the required tables and seed the data.
```
> python manage.py migrate
```
* Now, we can run the server
```
> python manage.py runserver
```
* By default, server will start at port `8000`

### Setup frontend
* Install `Node.js`
* Navigate to `web_frontend` folder
* Run `yarn` to install the requirements mentioned in `package.json` file
```
> yarn
```
* Once the requirements are installed we can start the server
```
> yarn start
```
* By default, the frontend server will start at port `3000`
