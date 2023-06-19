# URL_Shortner_Shortify

The project is a Flask web application that focuses on URL shortening functionality. It utilizes SQLite as the database and SQLAlchemy as the Object-Relational Mapping (ORM) tool for interacting with the database.

![image](https://github.com/MohneetKaur/URL_Shortner_Shortify/assets/84201530/b0b795b8-98b1-4c7a-b102-3612f833b97b)


Here is a brief explanation of the project steps:

Setup SQLite Database in Flask App:

A Flask application is created.
SQLAlchemy is configured to work with the Flask app.
The Flask app is passed to SQLAlchemy.
Creating a Model in Flask App:

A model class is created, which inherits from the db.Model class provided by SQLAlchemy.
The table name and column names are defined.
Column types and primary key are set.
A constructor (__init__) and __repr__ method are added to the model class.
Database Migration:

Three commands are executed in the command prompt (run as administrator): Flask db init, Flask db migrate, and Flask db upgrade.
These commands initialize the database, create migration scripts, and upgrade the database schema based on the model definition.
Detailed Approach to the Flask Application:

Necessary modules are imported, including Flask and other required modules.
The Flask application is initialized, assigning an instance of the Flask class to a variable.
Routes and views are defined for the web application. In this case, routes for the home page and history page are created.
The home page contains a form for the user to submit a URL. Upon submission, the URL is shortened and saved to the database.
The history page displays a list of original URLs and their corresponding shortened URLs retrieved from the database.
The Flask application is run using the run() method.
In summary, the project is a Flask web application that allows users to submit URLs and generates shortened URLs. The application uses SQLite as the database and SQLAlchemy for database management. It provides functionality for URL shortening, storing the original and shortened URLs, and displaying the history of shortened URLs.
