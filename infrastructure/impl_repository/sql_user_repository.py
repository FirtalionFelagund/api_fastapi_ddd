from typing import Optional, List

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

    def find_all(self) -> List[User]:
        with database.get_session() as session:
            statement = select(User)
            results = session.exec(statement)
            return results.all()
