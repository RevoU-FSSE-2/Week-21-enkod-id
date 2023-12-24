from core.user.constants import UserRole
from infrastructure.db import db
from sqlalchemy import Enum

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # expected to be hashed with bcrypt
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(Enum(UserRole), default=UserRole.JOB_SEEKER, nullable=False)
    bio = db.Column(db.String(150))  # new field