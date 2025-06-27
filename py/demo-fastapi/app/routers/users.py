from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app import crud, schemas

router = APIRouter()

@router.post("/users/", response_model=schemas.UserRead)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created = await crud.create_user(db, user)
    if not created:
        raise HTTPException(status_code=400, detail="Could not create user")
    return created

@router.get("/users/", response_model=list[schemas.UserRead])
async def list_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db, skip=skip, limit=limit)
