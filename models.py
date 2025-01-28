'''Modelos de datos para aplicacion CRUD'''

from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

class Role(str, Enum):
    admin = "admin"
    user = "user"

class Usuario(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    last_name: str
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]