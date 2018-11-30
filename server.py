from views import app
from models import connect_to_db


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'secretzzz'
    connect_to_db(app)

    app.run()
