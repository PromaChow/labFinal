from pydantic import BaseModel
from typing import Optional
import uuid



class User(BaseModel):
    username: str
    password: str
    

