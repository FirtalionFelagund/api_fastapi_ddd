from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from application.service.user_service import UserService
from domain.models.users import User
from interface.dependencies import get_user_service
from interface.schema.users import UserCreateSchema

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreateSchema,
    service: UserService = Depends(get_user_service)
):
    user = service.create_user(user_data)
    return user

@router.get("/", response_model=List[User])
async def list_users(
    service: UserService = Depends(get_user_service)
):
    return service.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user