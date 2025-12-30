from http.client import HTTPException
from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from starlette.status import HTTP_200_OK
from database import SessionLocal
from models import MessageList, Messages
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

class MessageRequest(BaseModel):
    message_id: int
    message_list_id: int


@router.get("/", status_code=HTTP_200_OK)
async def get_all_message_lists(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(MessageList).filter(MessageList.user_id == user.get('id')).all()

@router.get("/{message_list_id}/messages", status_code=HTTP_200_OK)
async def get_messages_from_list(user: user_dependency, db: db_dependency, message_list_id: int):
    return db.query(Messages).join(MessageList, Messages.message_list_id == MessageList.message_list_id) \
            .filter(Messages.message_list_id == message_list_id).filter(MessageList.user_id == user.get("id")).all()

@router.get("/message/{message_id}", status_code=HTTP_200_OK)
async def get_message(user: user_dependency, db: db_dependency, message_id: int):
    return db.query(Messages).join(MessageList, Messages.message_list_id == MessageList.message_list_id) \
            .filter(Messages.message_id == message_id).filter(MessageList.user_id == user.get("id")).all()