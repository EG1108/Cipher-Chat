from http.client import HTTPException
from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from database import SessionLocal
from models import MessageList
from routers.auth import get_current_user
router = APIRouter(
    prefix='/chats',
    tags=['chats']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class MessageListRequest(BaseModel):
    message_list_id : int
    user_id : int

@router.get("/", status_code=HTTP_200_OK)
async def get_all_message_lists(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(MessageList).filter(MessageList.message_list_id == user.get('user_id')).all()