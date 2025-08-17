from pydantic import BaseModel


class UserData(BaseModel):
    user_name: str
    password: str

    model_config = {
        "from_attributes": True
    }


class ShowUser(BaseModel):
    user_name: str

    model_config = {
        "from_attributes": True
    }