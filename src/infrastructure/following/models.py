from infrastructure.db import db

class Following(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    following_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationships
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('followings', lazy=True))
    following_user = db.relationship('User', foreign_keys=[following_user_id], backref=db.backref('followers', lazy=True))