from app import db

class User(db.model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    name = db.Column(db.String)

    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    def __repr__(self):
        return "<User %r>" % self.username

class Post(db.model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_key=user_id)

    def __init__(self, content, user_id,):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id
