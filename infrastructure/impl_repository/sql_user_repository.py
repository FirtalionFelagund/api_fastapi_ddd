from typing import Optional

from sqlmodel import select
from domain.models.users import User
from domain.repository.user_repository import UserRepository
from infrastructure.database import database


class SQLModelUserRepository(UserRepository):
    def get_by_id(self, user_id: int) -> Optional[User]:
        with database.get_session() as session:
            return session.get(User, user_id)

    def add(self, user: User) -> User:
        with database.get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        
    def get(self, user_id: int) -> Optional[User]:
        with database.get_session() as session:
            return session.get(User, user_id)
        
    def get_all(self) -> list[User]:
        with database.get_session() as session:
            return session.exec(select(User)).all()
        