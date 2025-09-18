import yaml
from my import jwt_secret_key, db_password, db_host

with open("config/config.yml", "r") as file:
    config = yaml.safe_load(file)

class Config:
    JWT_TOKEN_LOCATION = config["jwt"]["token_location"]
    JWT_HEADER_NAME = config["jwt"]["header_name"]
    JWT_HEADER_TYPE = config["jwt"]["header_type"]
    JWT_SECRET_KEY = jwt_secret_key

    DB_USER = config["database"]["user"]
    DB_PASSWORD = db_password
    DB_HOST = db_host
    DB_PORT = config["database"]["port"]
    DB_NAME = config["database"]["name"]
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
