from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field( description="User email", example="abc@xyz.com", max_length=100, min_length=5, regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    username: str
    password: str
    is_active: bool = True # default value is True
    first_name: str | None = None # default value is None
    last_name: str | None = None # default value is None
    