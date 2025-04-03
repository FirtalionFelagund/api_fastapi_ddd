from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    email: str
    is_active: bool = Field(default=True)

class UserCreate(UserBase):
    password: str  # Campo adicional para criação

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str