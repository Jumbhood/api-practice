import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SQL_USERNAME = os.environ.get("SQL_USERNAME")
SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_HOST = os.environ.get("SQL_HOST")
SQL_DATABASE = os.environ.get("SQL_DATABASE")

class Config:
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DB_URL = 'mysql+pymysql://{user}:{pw}@{url}:3306/{db}'.format(user=SQL_USERNAME,pw=SQL_PASSWORD,url=SQL_HOST,db=SQL_DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URL