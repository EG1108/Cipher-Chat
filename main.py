from fastapi import FastAPI
from models import Base
from database import engine
from routers import auth, users, messages, message_lists


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(messages.router)
app.include_router(message_lists.router)