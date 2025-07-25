from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import os

# get password and db-name from environment variables
db_root_password = os.environ.get('db_root_password')
db_name = os.environ.get('db_name')

# db_root_password = 'halloditiseenwachtwoord'
# db_name = 'users'


# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
SQLALCHEMY_DATABASE_URL = f"mariadb+mariadbconnector://root:{db_root_password}@mariadb:3306"


if 'maria' in SQLALCHEMY_DATABASE_URL:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=True
    )

    create_str = f"CREATE DATABASE IF NOT EXISTS {db_name} ;"
    engine.execute(create_str)
    engine.execute(f"USE {db_name};")
    drop_table_str = "DROP TABLE IF EXISTS User"
    engine.execute(drop_table_str)
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )


SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
