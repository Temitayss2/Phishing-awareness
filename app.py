from models import db, YourModel  # Ensure YourModel matches the class name in models.py
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, YourModel  # Make sure 'models.py' has your database models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Adjust this to your database URI
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db.init_app(app)

# Set up the admin interface
admin = Admin(app, name='Dashboard', template_mode='bootstrap3')

# Add your models to the admin interface
admin.add_view(ModelView(YourModel, db.session))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, YourModel  # Ensure 'models.py' contains your models
from flask import Flask, render_template, request, redirect, url_for
from extensions import db  # Import db from extensions
import matplotlib.pyplot as plt
import io
import base64

print("Initializing Flask app...")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with the Flask app
db.init_app(app)

print("Database initialized.")

# Import models after db initialization to avoid circular imports
from models import Department, PhishingAttempt, Response

print("Models imported.")

# Example route
@app.route('/')
def index():
    return "Flask app is running!"

if __name__ == '__main__':
    print("Starting the Flask app...")
    app.run(debug=True)
