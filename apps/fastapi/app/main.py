from typing import List
import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

## uncomment for local development
from models.database.models import User, Base
from models.pydantic import models as pydantic_models
from database import SessionMaker, engine

## comment for local development
# from app.models.database.models import User, Base
# from app.models.pydantic import models as pydantic_models
# from app.database import SessionMaker, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db_session():
    session = SessionMaker()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def index():
    return {"Hello, world!"}

# TODO: create get and post endpoints to query/post data from/to the database
#  - /user: get user by id
#  - /user_by_name: get user by name
#  - /users: get all users
#  - /create: create user


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
