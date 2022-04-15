from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Cathy",
                "email": "cathytol@live.nl",
            }
        }
