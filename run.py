from app import app
from config import APP_MODE, SERVER_CONFIG

app = app

if __name__ == '__main__':
    config = SERVER_CONFIG[ APP_MODE ]
    app.run(**config)
