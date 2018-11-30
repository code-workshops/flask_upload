from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)

    def __repr__(self):
        return f"<Image {self.id} | {self.name}>"


def connect_to_db(app):
    """Helper function to configure the database with the flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_uploads'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # An application context is required to connect to the database!
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    # Create tables ...
    db.create_all()
    print('Connected to database.')
