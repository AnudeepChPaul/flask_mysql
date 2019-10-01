SERVER_CONFIG = {
    'DEV': {
        'host': 'localhost',
        'port': 3000,
        'debug': True
    }
}

APP_MODE = 'DEV'

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# Mysql database configuration
DATABASE_CONNECT_OPTIONS = {
    # defines the db username
    'user': 'root',
    # defines the db password for defined username
    'password': '12345678',
    # hostname of mysqld instance running on local machine
    'host': '127.0.0.1',
    # port number of mysqld instance running on hostname
    'port': 3306,
    # the db the application should use ( It must exists )
    'database': 'flask'
}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
# CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
# SECRET_KEY = "secret"
