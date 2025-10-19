from fastapi import APIRouter, HTTPException, status

from app.core.database import users_collection
from app.core.security import hash_password, verify_password
from app.schemas.user_schema import UserResponse, UserRegister, UserLogin
from app.utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserRegister):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )

    hashed_password = hash_password(user.password)

    user_dict = user.model_dump()
    user_dict["password"] = hashed_password
    await users_collection.insert_one(user_dict)

    token = create_access_token({"email": user.email})

    return {"token": token}

@router.post("/login", response_model=UserResponse)
async def login_user(user: UserLogin):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token({"email": user.email})
    return {"token": token}
