from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<YourModel {self.name}>'
from extensions import db  # Import db from extensions

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class PhishingAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), db.ForeignKey('department.name'), nullable=False)
    scenario = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), db.ForeignKey('department.name'), nullable=False)
    attempt_id = db.Column(db.Integer, db.ForeignKey('phishing_attempt.id'), nullable=False)
    response = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
