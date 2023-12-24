from core.user.constants import UserRole
from infrastructure.db import db
from sqlalchemy import Enum, DateTime
from datetime import datetime

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))
    tweet = db.Column(db.String(255), nullable=False)
    published_at = db.Column(DateTime, default=datetime.utcnow, nullable=False)