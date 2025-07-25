from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

## uncomment for local development
# from models.database.models import User, Base
# from models.pydantic import models as pydantic_models
# from database import SessionMaker, engine

## comment for local development
from app.models.database.models import User, Base
from app.models.pydantic import models as pydantic_models
from app.database import SessionMaker, engine

import uvicorn


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


@app.get("/user", response_model=List[pydantic_models.User])
def get_user(id: int, session: Session = Depends(get_db_session)):
    user = session.query(User).filter(User.id == id).all()
    if user is None:
        raise HTTPException(status_code=404, detail=f"No user found with id {id}.")
    return user

@app.get("/user_by_name", response_model=List[pydantic_models.User])
def get_user_by_name(name: str, session: Session = Depends(get_db_session)):
    users = session.query(User).filter(User.name == name).all()
    if users is None:
        raise HTTPException(status_code=404, detail=f"No user found with name {name}.")
    return users

@app.get("/users", response_model=List[pydantic_models.User])
def get_all_users(session: Session = Depends(get_db_session)):
    users = session.query(User).all()
    return users


@app.post("/create", response_model=pydantic_models.User)
def add_user(user: pydantic_models.User, session: Session = Depends(get_db_session)):
    newUser = User(id=user.id, name=user.name, email=user.email)
    session.add(newUser)
    session.commit()
    return newUser


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
