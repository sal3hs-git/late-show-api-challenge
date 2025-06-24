

import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret"
