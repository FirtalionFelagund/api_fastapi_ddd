from passlib.context import CryptContext

from application.dto.users import UserCreateDTO
from domain.models.users import User
from domain.repository.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCreate:
    pass


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    def create_user(self, user_dto: UserCreateDTO) -> User:
        hashed_password = pwd_context.hash(user_dto.password)
        user = User(
            name=user_dto.name,
            email=user_dto.email,
            hashed_password=hashed_password
        )
        return self.repository.add(user)
    
    def get_user(self, user_id: int) -> User:
        return self.repository.get_by_id(user_id)
    
    def get_users(self) -> list[User]:
        return self.repository.get_all()
    