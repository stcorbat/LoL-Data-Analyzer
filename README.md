# LoL-Data-Analyzer
A web app that can display data in a comprehensive format from my League match database

### Flask
This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) application, which is a python framework to serve webpages. 

### Database
Since the database that holds all my League data is already defined, this application won't use `flask-sqlalchemy`.
Instead, it will use `mysql-connector` to read from the database.

### Deployment
The application is run behind a uWSGI instance and Nginx reverse proxy on my local server machine.
