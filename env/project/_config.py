import os
#__grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'x135\xd7|\xf4\xa1\x9f\x8a\xa3\x7f:0\x1a\xf8\x00\x87\xbb\xcc\x0b(<\x1e\x97\xa6'

#__ define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
