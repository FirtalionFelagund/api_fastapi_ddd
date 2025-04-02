from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.users import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass


    # @abstractmethod
    # def get_by_email(self, email: str) -> Optional[User]:
    #     pass

    @abstractmethod
    def add(self, user: User) -> User:
        pass
